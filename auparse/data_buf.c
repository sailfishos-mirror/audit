/* data_buf.c --
 * Copyright 2007,2011 Red Hat Inc
 * All Rights Reserved.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Authors:
 *      John Dennis <jdennis@redhat.com>
 */

/*
 * gcc -DTEST -g data_buf.c -o data_buf
 * gcc -DTEST -g data_buf.c -o data_buf && valgrind --leak-check=yes ./data_buf
 */

/*****************************************************************************/
/******************************** Documentation ******************************/
/*****************************************************************************/

/*****************************************************************************/
/******************************* Include Files *******************************/
/*****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h> // for memmove()
#include <assert.h>
#include <stdarg.h>
#include <errno.h>
#include "data_buf.h"

/*****************************************************************************/
/****************************** Internal Defines *****************************/
/*****************************************************************************/

#ifndef MIN
#define MIN(a,b) (((a)<=(b))?(a):(b))
#endif

#ifndef MAX
#define MAX(a,b) (((a)>=(b))?(a):(b))
#endif

//#define DEBUG 1

#ifdef DEBUG
#define DATABUF_VALIDATE(db)                            \
{                                                       \
    if (db->alloc_ptr == NULL || db->alloc_size == 0) { \
        assert(db->alloc_ptr == NULL);                  \
        assert(db->alloc_size == 0);                    \
        assert(db->len == 0);                           \
    } else {                                            \
        assert(db->offset         <= db->alloc_size);   \
        assert(db->len            <= db->alloc_size);   \
        assert(db->offset+db->len <= db->alloc_size);   \
    }                                                   \
}
#else
#define DATABUF_VALIDATE(db)
#endif

/*****************************************************************************/
/************************** Internal Type Definitions ************************/
/*****************************************************************************/

/*****************************************************************************/
/**********************  External Function Declarations  *********************/
/*****************************************************************************/

/*****************************************************************************/
/**********************  Internal Function Declarations  *********************/
/*****************************************************************************/

static int databuf_shift_data_to_beginning(DataBuf *db);

/*****************************************************************************/
/*************************  External Global Variables  ***********************/
/*****************************************************************************/

/*****************************************************************************/
/*************************  Internal Global Variables  ***********************/
/*****************************************************************************/

#ifdef DEBUG
static int debug = 0;
#endif

/*****************************************************************************/
/****************************  Inline Functions  *****************************/
/*****************************************************************************/
static inline char *databuf_end(const DataBuf *db)
{return (db->alloc_ptr == NULL) ? NULL : db->alloc_ptr+db->offset+db->len;}

static inline unsigned databuf_tail_size(const DataBuf *db)
{return db->alloc_size - (db->offset+db->len);}

static inline unsigned databuf_tail_available(DataBuf *db, size_t append_len)
{return append_len <= databuf_tail_size(db);}

/*****************************************************************************/
/***************************  Internal Functions  ****************************/
/*****************************************************************************/

static int databuf_shift_data_to_beginning(DataBuf *db)
{
    DATABUF_VALIDATE(db);
    if (db->flags & DATABUF_FLAG_PRESERVE_HEAD) return -1;
    if (databuf_beg(db) == NULL) return 1;
    if (db->offset) {
        memmove(db->alloc_ptr, databuf_beg(db), db->len);
        db->offset = 0;
    }
    DATABUF_VALIDATE(db);
    return 1;
}

/*****************************************************************************/
/****************************  Exported Functions  ***************************/
/*****************************************************************************/

void databuf_print(const DataBuf *db, int print_data, char *fmt, ...)
{
    va_list ap;
    va_start(ap, fmt);
    if (fmt) {
        vprintf(fmt, ap);
    }
    printf("%salloc_size=%zu alloc_ptr=%p offset=%zu beg=%p len=%zu max_len=%zu flags=[",
           fmt?" ":"", db->alloc_size, db->alloc_ptr, db->offset, databuf_beg(db), db->len, db->max_len);

    if (db->flags & DATABUF_FLAG_PRESERVE_HEAD) printf("PRESERVE_HEAD ");
    printf("]");
    
    if (print_data) {
        printf(" [");
        fwrite(databuf_beg(db), 1, db->len, stdout);
        printf("]");
    }
    printf("\n");
    va_end(ap);
}

int databuf_init(DataBuf *db, size_t size, unsigned flags)
{
    db->alloc_ptr  = NULL;
    db->alloc_size = 0;
    db->offset     = 0;
    db->len        = 0;
    db->max_len    = 0;
    db->flags      = flags;

    if (size) {
        if ((db->alloc_ptr = malloc(size))) {
            db->alloc_size = size;
            return 1;
        } else {
            return -1;
        }
    }

    return 1;
}

void databuf_free(DataBuf *db)
{
    DATABUF_VALIDATE(db);

    if (db->alloc_ptr != NULL) {
        free(db->alloc_ptr);
    }

    db->alloc_ptr  = NULL;
    db->alloc_size = 0;
    db->offset     = 0;
    db->len        = 0;
    db->max_len    = 0;

    DATABUF_VALIDATE(db);
}

int databuf_append(DataBuf *db, const char *src, size_t src_size)
{
	size_t new_len, required_size;

	DATABUF_VALIDATE(db);

	if (src == NULL || src_size == 0)
		return 0;

	new_len = db->len + src_size;

#ifdef DEBUG
	if (debug)
		databuf_print(db, 1, "databuf_append() size=%zd", src_size);
#endif

	/* If we can shift data to the beginning do so before any size checks */
	if (!(db->flags & DATABUF_FLAG_PRESERVE_HEAD) &&
				!databuf_tail_available(db, src_size))
		databuf_shift_data_to_beginning(db);

	required_size = db->offset + new_len;
	if (required_size > db->alloc_size) {
		void *new_alloc;
		size_t new_alloc_size = db->alloc_size ?
			db->alloc_size * 2 : required_size;

		if (new_alloc_size < required_size)
			new_alloc_size = required_size;

		new_alloc = realloc(db->alloc_ptr, new_alloc_size);
		if (!new_alloc)
			return -1;           /* realloc failed */

		db->alloc_ptr  = new_alloc;
		db->alloc_size = new_alloc_size;
        }
#ifdef DEBUG
	if (debug)
		databuf_print(db, 1, "databuf_append() about to memmove()");
#endif
	/* pointers all set up and room available, move the data and update */
	memmove(databuf_end(db), src, src_size);
	db->len = new_len;
	db->max_len = MAX(db->max_len, new_len);
#ifdef DEBUG
	if (debug)
		databuf_print(db, 1, "databuf_append() conclusion");
#endif
	DATABUF_VALIDATE(db);
	return 1;
}

int databuf_replace(DataBuf *db, const char *src, size_t src_size)
{
    DATABUF_VALIDATE(db);

    if (src == NULL || src_size == 0) return 0;

    db->len = 0;
    return databuf_append(db, src, src_size);
}

int databuf_advance(DataBuf *db, size_t advance)
{
    size_t actual_advance;
    DATABUF_VALIDATE(db);

#ifdef DEBUG
    if (debug) databuf_print(db, 1, "databuf_advance() enter, advance=%zd", advance);
#endif
    actual_advance = MIN(advance, db->len);
    db->offset += actual_advance;
    db->len -= actual_advance;

#ifdef DEBUG
    if (debug) databuf_print(db, 1, "databuf_advance() leave, actual_advance=%zd", actual_advance);
#endif
    DATABUF_VALIDATE(db);
    if (advance == actual_advance) {
        return 1;
    } else {
        errno = ESPIPE; // Illegal seek
        return -1;
    }
}

int databuf_reset(DataBuf *db)
{
#ifdef DEBUG
    if (debug) databuf_print(db, 1, "databuf_reset() entry");
#endif
    if (!(db->flags & DATABUF_FLAG_PRESERVE_HEAD)) return -1;
    db->offset = 0;
    db->len = MIN(db->alloc_size, db->max_len);
#ifdef DEBUG
    if (debug) databuf_print(db, 1, "databuf_reset() exit");
#endif
    return 1;
}

/*****************************************************************************/
/*******************************  Test Program  ******************************/
/*****************************************************************************/

#ifdef TEST
static char *make_data(size_t size, const char *fill) {
    int n=0;
    char *data = malloc(size);

    if (data == NULL) {
        fprintf(stderr, "ERROR: make_data malloc failed\n");
        exit(1);
    }

    n += snprintf(data, size, "%d", size);
    while (n < size) {
        n += snprintf(data+n, size-n, "%s", fill);
    }
    return data;
}

int main(int argc, char **argv)
{
    size_t size = 0;
    DataBuf buf;
    char *data;
    int rc;

    rc = databuf_init(&buf, size, 0);
    assert(rc);
    databuf_print(&buf, 1, "after init size=%d", size);

    databuf_free(&buf);

#if 0
    assert(databuf_init(&buf, size, 0));
    databuf_print(&buf, 1, "after init size=%d", size);

    size = 8;
    data = make_data(size, "a");
    assert(databuf_append(&buf, data, size));
    databuf_print(&buf, 1, "after append size=%d", size);
    assert(databuf_append(&buf, data, size));
    free(data);
    databuf_print(&buf, 1, "after append size=%d", size);

    assert(databuf_advance(&buf, 4));
    databuf_print(&buf, 1, "after databuf_advance(%d", 4);

    size = 5;
    data = make_data(size, "b");
    assert(databuf_append(&buf, data, size));
    free(data);
    databuf_print(&buf, 1, "after append size=%d", size);
    size = 7;
    data = make_data(size, "c");
    assert(databuf_append(&buf, data, size));
    free(data);
    databuf_print(&buf, 1, "after append size=%d", size);

    databuf_free(&buf);
#endif
    exit(0);
}
#endif
