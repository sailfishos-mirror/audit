# Makefile.am -- 
# Copyright 2025 Red Hat Inc.
# All Rights Reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# 
# Authors:
#   Steve Grubb <sgrubb@redhat.com>
#

CONFIG_CLEAN_FILES = *.loT *.rej *.orig *.cur
check_PROGRAMS = fgets_test
TESTS = $(check_PROGRAMS)
AM_CPPFLAGS = -I${top_srcdir}/common -I${top_srcdir}/lib
fgets_test_SOURCES = fgets-test.c
lookup_test_LDFLAGS = -static
lookup_test_LDADD = ${top_builddir}/common/audit_fgets.o

