Starting Test 1, iterate...
auid=4294967295
interp auid=unset
auid=848
interp auid=unknown(848)
auid=848
interp auid=unknown(848)
Test 1 Done

Starting Test 2, walk events, records, and fields...
event 1 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=1 file=None
    event time: 1143146623.787:142, host=(null)
        type=LOGIN (LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=848 (unknown(848))

event 2 has 1 records
    record 1 of type 1300(SYSCALL) has 24 fields
    line=2 file=None
    event time: 1143146623.875:143, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=188 (setxattr)
        success=yes (yes)
        exit=0 (0)
        a0=7fffffa9a9f0 (0x7fffffa9a9f0)
        a1=3958d11333 (0x3958d11333)
        a2=5131f0 (0x5131f0)
        a3=20 (0x20)
        items=1 (1)
        pid=2027 (2027)
        auid=848 (unknown(848))
        uid=0 (root)
        gid=0 (root)
        euid=0 (root)
        suid=0 (root)
        fsuid=0 (root)
        egid=0 (root)
        sgid=0 (root)
        fsgid=0 (root)
        tty=tty3 (tty3)
        comm="login" (login)
        exe="/bin/login" (/bin/login)
        subj=system_u:system_r:local_login_t:s0-s0:c0.c255 (system_u:system_r:local_login_t:s0-s0:c0.c255)

event 3 has 1 records
    record 1 of type 1112(USER_LOGIN) has 10 fields
    line=3 file=None
    event time: 1143146623.879:146, host=(null)
        type=USER_LOGIN (USER_LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=848 (unknown(848))
        uid=848 (unknown(848))
        exe="/bin/login" (/bin/login)
        hostname=? (?)
        addr=? (?)
        terminal=tty3 (tty3)
        res=success (success)

Test 2 Done

Starting Test 3, walk events, records of 1 buffer...
event has 1 records
    record 1 of type 1112(USER_LOGIN) has 10 fields
    line=1 file=None
    event time: 1143146623.879:146, host=(null)

Test 3 Done

Starting Test 4, walk events, records of 1 file...
event 1 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=AVC
        seresult=denied
        seperms=read,write
        pid=13010
        comm="pickup"
        name="maildrop"
        dev=hda7
        ino=14911367
        scontext=system_u:system_r:postfix_pickup_t:s0
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0
        tclass=dir

    record 2 of type 1300(SYSCALL) has 26 fields
    line=2 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=2
        success=no
        exit=-13
        a0=5555665d91b0
        a1=10800
        a2=5555665d91b8
        a3=0
        items=1
        ppid=2013
        pid=13010
        auid=4294967295
        uid=890
        gid=890
        euid=890
        suid=890
        fsuid=890
        egid=890
        sgid=890
        fsgid=890
        tty=(none)
        comm="pickup"
        exe="/usr/libexec/postfix/pickup"
        subj=system_u:system_r:postfix_pickup_t:s0
        key=(null)

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=CWD
        cwd="/var/spool/postfix"

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=PATH
        item=0
        name="maildrop"
        inode=14911367
        dev=03:07
        mode=040730
        ouid=890
        ogid=891
        rdev=00:00
        obj=system_u:object_r:postfix_spool_maildrop_t:s0

event 2 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=test.log
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT
        pid=13015
        uid=0
        auid=4294967295
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 3 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=test.log
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ
        pid=13015
        uid=0
        auid=4294967295
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 4 has 3 records
    record 1 of type 1006(LOGIN) has 10 fields
    line=7 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=LOGIN
        pid=2288
        uid=0
        subj=system_u:system_r:init_t:s0
        old-auid=4294967295
        auid=42
        tty=(none)
        old-ses=4294967295
        ses=1
        res=1

    record 2 of type 1300(SYSCALL) has 27 fields
    line=8 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=1
        success=yes
        exit=2
        a0=8
        a1=7fffa7aede20
        a2=2
        a3=0
        items=0
        ppid=1
        pid=2288
        auid=42
        uid=0
        gid=0
        euid=0
        suid=0
        fsuid=0
        egid=0
        sgid=0
        fsgid=0
        tty=(none)
        ses=1
        comm="(systemd)"
        exe="/usr/lib/systemd/systemd"
        subj=system_u:system_r:init_t:s0
        key=(null)

    record 3 of type 1327(PROCTITLE) has 2 fields
    line=9 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=PROCTITLE
        proctitle="(systemd)"

event 5 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=10 file=test.log
    event time: 1170021601.344:297, host=(null)
        type=USER_START
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 6 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=11 file=test.log
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 7 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=12 file=test.log
    event time: 1170021601.366:299, host=(null)
        type=USER_END
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

Test 4 Done

Starting Test 5, walk events, records of 2 files...
event 1 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=test2.log
    event time: 1170021493.977:283, host=(null)
        type=AVC
        seresult=denied
        seperms=read
        pid=13010
        comm="pickup"
        name="maildrop"
        dev=hda7
        ino=14911367
        scontext=system_u:system_r:postfix_pickup_t:s0
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0
        tclass=dir

    record 2 of type 1300(SYSCALL) has 26 fields
    line=2 file=test2.log
    event time: 1170021493.977:283, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=2
        success=no
        exit=-13
        a0=5555665d91b0
        a1=10800
        a2=5555665d91b8
        a3=0
        items=1
        ppid=2013
        pid=13010
        auid=4294967295
        uid=890
        gid=890
        euid=890
        suid=890
        fsuid=890
        egid=890
        sgid=890
        fsgid=890
        tty=(none)
        comm="pickup"
        exe="/usr/libexec/postfix/pickup"
        subj=system_u:system_r:postfix_pickup_t:s0
        key=(null)

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test2.log
    event time: 1170021493.977:283, host=(null)
        type=CWD
        cwd="/var/spool/postfix"

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=test2.log
    event time: 1170021493.977:283, host=(null)
        type=PATH
        item=0
        name="maildrop"
        inode=14911367
        dev=03:07
        mode=040730
        ouid=890
        ogid=891
        rdev=00:00
        obj=system_u:object_r:postfix_spool_maildrop_t:s0

event 2 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=test2.log
    event time: 1170021601.340:284, host=(null)
        type=USER_ACCT
        pid=13015
        uid=0
        auid=4294967295
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 3 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=test2.log
    event time: 1170021601.342:285, host=(null)
        type=CRED_ACQ
        pid=13015
        uid=0
        auid=4294967295
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 4 has 3 records
    record 1 of type 1006(LOGIN) has 10 fields
    line=7 file=test2.log
    event time: 1170021601.343:286, host=(null)
        type=LOGIN
        pid=2288
        uid=0
        subj=system_u:system_r:init_t:s0
        old-auid=4294967295
        auid=42
        tty=(none)
        old-ses=4294967295
        ses=1
        res=1

    record 2 of type 1300(SYSCALL) has 27 fields
    line=8 file=test2.log
    event time: 1170021601.343:286, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=1
        success=yes
        exit=2
        a0=8
        a1=7fffa7aede20
        a2=2
        a3=0
        items=0
        ppid=1
        pid=2288
        auid=42
        uid=0
        gid=0
        euid=0
        suid=0
        fsuid=0
        egid=0
        sgid=0
        fsgid=0
        tty=(none)
        ses=1
        comm="(systemd)"
        exe="/usr/lib/systemd/systemd"
        subj=system_u:system_r:init_t:s0
        key=(null)

    record 3 of type 1327(PROCTITLE) has 2 fields
    line=9 file=test2.log
    event time: 1170021601.343:286, host=(null)
        type=PROCTITLE
        proctitle="(systemd)"

event 5 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=10 file=test2.log
    event time: 1170021601.344:287, host=(null)
        type=USER_START
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 6 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=11 file=test2.log
    event time: 1170021601.364:288, host=(null)
        type=CRED_DISP
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 7 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=12 file=test2.log
    event time: 1170021601.366:289, host=(null)
        type=USER_END
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 8 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=AVC
        seresult=denied
        seperms=read,write
        pid=13010
        comm="pickup"
        name="maildrop"
        dev=hda7
        ino=14911367
        scontext=system_u:system_r:postfix_pickup_t:s0
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0
        tclass=dir

    record 2 of type 1300(SYSCALL) has 26 fields
    line=2 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=2
        success=no
        exit=-13
        a0=5555665d91b0
        a1=10800
        a2=5555665d91b8
        a3=0
        items=1
        ppid=2013
        pid=13010
        auid=4294967295
        uid=890
        gid=890
        euid=890
        suid=890
        fsuid=890
        egid=890
        sgid=890
        fsgid=890
        tty=(none)
        comm="pickup"
        exe="/usr/libexec/postfix/pickup"
        subj=system_u:system_r:postfix_pickup_t:s0
        key=(null)

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=CWD
        cwd="/var/spool/postfix"

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=PATH
        item=0
        name="maildrop"
        inode=14911367
        dev=03:07
        mode=040730
        ouid=890
        ogid=891
        rdev=00:00
        obj=system_u:object_r:postfix_spool_maildrop_t:s0

event 9 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=test.log
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT
        pid=13015
        uid=0
        auid=4294967295
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 10 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=test.log
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ
        pid=13015
        uid=0
        auid=4294967295
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 11 has 3 records
    record 1 of type 1006(LOGIN) has 10 fields
    line=7 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=LOGIN
        pid=2288
        uid=0
        subj=system_u:system_r:init_t:s0
        old-auid=4294967295
        auid=42
        tty=(none)
        old-ses=4294967295
        ses=1
        res=1

    record 2 of type 1300(SYSCALL) has 27 fields
    line=8 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=1
        success=yes
        exit=2
        a0=8
        a1=7fffa7aede20
        a2=2
        a3=0
        items=0
        ppid=1
        pid=2288
        auid=42
        uid=0
        gid=0
        euid=0
        suid=0
        fsuid=0
        egid=0
        sgid=0
        fsgid=0
        tty=(none)
        ses=1
        comm="(systemd)"
        exe="/usr/lib/systemd/systemd"
        subj=system_u:system_r:init_t:s0
        key=(null)

    record 3 of type 1327(PROCTITLE) has 2 fields
    line=9 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=PROCTITLE
        proctitle="(systemd)"

event 12 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=10 file=test.log
    event time: 1170021601.344:297, host=(null)
        type=USER_START
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 13 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=11 file=test.log
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 14 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=12 file=test.log
    event time: 1170021601.366:299, host=(null)
        type=USER_END
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

Test 5 Done

Starting Test 6, search...
auid = 500 not found...which is correct
auid exists...which is correct
Testing BUFFER_ARRAY, stop on field
Found auid = 848
Testing BUFFER_ARRAY, stop on record
Found type = SYSCALL
Testing BUFFER_ARRAY, stop on event
Found type = SYSCALL
Testing test.log, stop on field
Found auid = 4294967295
Testing test.log, stop on record
Found type = SYSCALL
Testing test.log, stop on event
Found type = AVC
Test 6 Done

Starting Test 7, compound search...
Found type = USER_START
Found auid = 42
Test 7 Done

Starting Test 8, regex search...
Doing regex match...

Test 8 Done

Starting Test 9, buffer feed...
event 1 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=1 file=None
    event time: 1143146623.787:142, host=(null)
        type=LOGIN
        pid=2027
        uid=0
        auid=4294967295
        auid=848

event 2 has 1 records
    record 1 of type 1300(SYSCALL) has 24 fields
    line=2 file=None
    event time: 1143146623.875:143, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=188
        success=yes
        exit=0
        a0=7fffffa9a9f0
        a1=3958d11333
        a2=5131f0
        a3=20
        items=1
        pid=2027
        auid=848
        uid=0
        gid=0
        euid=0
        suid=0
        fsuid=0
        egid=0
        sgid=0
        fsgid=0
        tty=tty3
        comm="login"
        exe="/bin/login"
        subj=system_u:system_r:local_login_t:s0-s0:c0.c255

event 3 has 1 records
    record 1 of type 1112(USER_LOGIN) has 10 fields
    line=3 file=None
    event time: 1143146623.879:146, host=(null)
        type=USER_LOGIN
        pid=2027
        uid=0
        auid=848
        uid=848
        exe="/bin/login"
        hostname=?
        addr=?
        terminal=tty3
        res=success

Test 9 Done

Starting Test 10, file feed...
event 1 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=None
    event time: 1170021493.977:293, host=(null)
        type=AVC
        seresult=denied
        seperms=read,write
        pid=13010
        comm="pickup"
        name="maildrop"
        dev=hda7
        ino=14911367
        scontext=system_u:system_r:postfix_pickup_t:s0
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0
        tclass=dir

    record 2 of type 1300(SYSCALL) has 26 fields
    line=2 file=None
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=2
        success=no
        exit=-13
        a0=5555665d91b0
        a1=10800
        a2=5555665d91b8
        a3=0
        items=1
        ppid=2013
        pid=13010
        auid=4294967295
        uid=890
        gid=890
        euid=890
        suid=890
        fsuid=890
        egid=890
        sgid=890
        fsgid=890
        tty=(none)
        comm="pickup"
        exe="/usr/libexec/postfix/pickup"
        subj=system_u:system_r:postfix_pickup_t:s0
        key=(null)

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=None
    event time: 1170021493.977:293, host=(null)
        type=CWD
        cwd="/var/spool/postfix"

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=None
    event time: 1170021493.977:293, host=(null)
        type=PATH
        item=0
        name="maildrop"
        inode=14911367
        dev=03:07
        mode=040730
        ouid=890
        ogid=891
        rdev=00:00
        obj=system_u:object_r:postfix_spool_maildrop_t:s0

event 2 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=None
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT
        pid=13015
        uid=0
        auid=4294967295
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 3 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=None
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ
        pid=13015
        uid=0
        auid=4294967295
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 4 has 3 records
    record 1 of type 1006(LOGIN) has 10 fields
    line=7 file=None
    event time: 1170021601.343:296, host=(null)
        type=LOGIN
        pid=2288
        uid=0
        subj=system_u:system_r:init_t:s0
        old-auid=4294967295
        auid=42
        tty=(none)
        old-ses=4294967295
        ses=1
        res=1

    record 2 of type 1300(SYSCALL) has 27 fields
    line=8 file=None
    event time: 1170021601.343:296, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=1
        success=yes
        exit=2
        a0=8
        a1=7fffa7aede20
        a2=2
        a3=0
        items=0
        ppid=1
        pid=2288
        auid=42
        uid=0
        gid=0
        euid=0
        suid=0
        fsuid=0
        egid=0
        sgid=0
        fsgid=0
        tty=(none)
        ses=1
        comm="(systemd)"
        exe="/usr/lib/systemd/systemd"
        subj=system_u:system_r:init_t:s0
        key=(null)

    record 3 of type 1327(PROCTITLE) has 2 fields
    line=9 file=None
    event time: 1170021601.343:296, host=(null)
        type=PROCTITLE
        proctitle="(systemd)"

event 5 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=10 file=None
    event time: 1170021601.344:297, host=(null)
        type=USER_START
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 6 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=11 file=None
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

event 7 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=12 file=None
    event time: 1170021601.366:299, host=(null)
        type=USER_END
        pid=13015
        uid=0
        auid=0
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023
        acct=root
        exe="/usr/sbin/crond"
        hostname=?
        addr=?
        terminal=cron
        res=success

Test 10 Done

Starting Test 11, walk LONG event records from a file...
event 1 has 7 records
    record 1 of type 1300(SYSCALL) has 26 fields
    line=1 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=59
        success=yes
        exit=0
        a0=8c403a0
        a1=8c3e8b0
        a2=fffffb6cc5b0
        a3=0
        items=3
        ppid=105182
        pid=105183
        auid=573
        uid=583
        gid=583
        euid=583
        suid=583
        fsuid=583
        egid=583
        sgid=583
        fsgid=583
        tty=pts2
        ses=2632
        comm="ld"
        exe="/bin/sh4"
        key=(null)

    record 2 of type 1309(EXECVE) has 50 fields
    line=2 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=EXECVE
        argc=48
        a0="/bin/sh"
        a1="-efu"
        a2="/usr/bin/ld"
        a3="-plugin"
        a4="/usr/libexec/gcc/aarch64-alt-linux/8/liblto_plugin.so"
        a5="-plugin-opt=/usr/libexec/gcc/aarch64-alt-linux/8/lto-wrapper"
        a6="-plugin-opt=-fresolution=/usr/src/tmp/cchyHiZN.res"
        a7="-plugin-opt=-pass-through=-lgcc"
        a8="-plugin-opt=-pass-through=-lgcc_s"
        a9="-plugin-opt=-pass-through=-lc"
        a10="-plugin-opt=-pass-through=-lgcc"
        a11="-plugin-opt=-pass-through=-lgcc_s"
        a12="--build-id"
        a13="--no-add-needed"
        a14="--eh-frame-hdr"
        a15="--hash-style=gnu"
        a16="--as-needed"
        a17="-shared"
        a18="-X"
        a19="-EL"
        a20="-maarch64linux"
        a21="-o"
        a22="ztest105133.so"
        a23="/usr/lib64/gcc/aarch64-alt-linux/8/../../../../lib64/crti.o"
        a24="/usr/lib64/gcc/aarch64-alt-linux/8/crtbeginS.o"
        a25="-L/usr/lib64/gcc/aarch64-alt-linux/8"
        a26="-L/usr/lib64/gcc/aarch64-alt-linux/8/../../../../lib64"
        a27="-L/lib/../lib64"
        a28="-L/usr/lib/../lib64"
        a29="-L/usr/lib64/gcc/aarch64-alt-linux/8/../../.."
        a30="-soname"
        a31="libz.so.1"
        a32="--version-script"
        a33="zlib.map"
        a34="ztest105133.o"
        a35="-lgcc"
        a36="--push-state"
        a37="--as-needed"
        a38="-lgcc_s"
        a39="--pop-state"
        a40="-lc"
        a41="-lgcc"
        a42="--push-state"
        a43="--as-needed"
        a44="-lgcc_s"
        a45="--pop-state"
        a46="/usr/lib64/gcc/aarch64-alt-linux/8/crtendS.o"
        a47="/usr/lib64/gcc/aarch64-alt-linux/8/../../../../lib64/crtn.o"

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=CWD
        cwd="/usr/src/RPM/BUILD/zlib-1.2.11-alt1"

    record 4 of type 1302(PATH) has 15 fields
    line=4 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=PATH
        item=0
        name="/usr/bin/ld"
        inode=40854
        dev=00:30
        mode=0100755
        ouid=582
        ogid=582
        rdev=00:00
        nametype=NORMAL
        cap_fp=0
        cap_fi=0
        cap_fe=0
        cap_fver=0
        cap_frootid=0

    record 5 of type 1302(PATH) has 15 fields
    line=5 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=PATH
        item=1
        name="/bin/sh"
        inode=33238
        dev=00:30
        mode=0100755
        ouid=582
        ogid=582
        rdev=00:00
        nametype=NORMAL
        cap_fp=0
        cap_fi=0
        cap_fe=0
        cap_fver=0
        cap_frootid=0

    record 6 of type 1302(PATH) has 15 fields
    line=6 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=PATH
        item=2
        name="/lib64/ld-linux-aarch64.so.1"
        inode=33874
        dev=00:30
        mode=0100755
        ouid=582
        ogid=582
        rdev=00:00
        nametype=NORMAL
        cap_fp=0
        cap_fi=0
        cap_fe=0
        cap_fver=0
        cap_frootid=0

    record 7 of type 1327(PROCTITLE) has 2 fields
    line=7 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=PROCTITLE
        proctitle=2F62696E2F7368002D656675002F7573722F62696E2F6C64002D706C7567696E002F7573722F6C6962657865632F6763632F616172636836342D616C742D6C696E75782F382F6C69626C746F5F706C7567696E2E736F002D706C7567696E2D6F70743D2F7573722F6C6962657865632F6763632F616172636836342D616C742D

event 2 has 6 records
    record 1 of type 1300(SYSCALL) has 26 fields
    line=8 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=SYSCALL
        arch=c000003e
        syscall=59
        success=yes
        exit=0
        a0=1a407f50
        a1=1a401cd0
        a2=1a3ed090
        a3=0
        items=2
        ppid=105932
        pid=105933
        auid=573
        uid=583
        gid=583
        euid=583
        suid=583
        fsuid=583
        egid=583
        sgid=583
        fsgid=583
        tty=pts2
        ses=2632
        comm="m4"
        exe="/usr/bin/m4"
        key=(null)

    record 2 of type 1309(EXECVE) has 218 fields
    line=9 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=EXECVE
        argc=216
        a0="/usr/bin/m4"
        a1="--nesting-limit=1024"
        a2="--gnu"
        a3="--include=/usr/share/autoconf-2.60"
        a4="--debug=aflq"
        a5="--fatal-warning"
        a6="--debugfile=autom4te.cache/traces.0t"
        a7="--trace=AC_CHECK_LIBM"
        a8="--trace=AC_CONFIG_MACRO_DIR"
        a9="--trace=AC_CONFIG_MACRO_DIR_TRACE"
        a10="--trace=AC_DEFUN"
        a11="--trace=AC_DEFUN_ONCE"
        a12="--trace=AC_DEPLIBS_CHECK_METHOD"
        a13="--trace=AC_DISABLE_FAST_INSTALL"
        a14="--trace=AC_DISABLE_SHARED"
        a15="--trace=AC_DISABLE_STATIC"
        a16="--trace=AC_ENABLE_FAST_INSTALL"
        a17="--trace=AC_ENABLE_SHARED"
        a18="--trace=AC_ENABLE_STATIC"
        a19="--trace=AC_LIBLTDL_CONVENIENCE"
        a20="--trace=AC_LIBLTDL_INSTALLABLE"
        a21="--trace=AC_LIBTOOL_COMPILER_OPTION"
        a22="--trace=AC_LIBTOOL_CONFIG"
        a23="--trace=AC_LIBTOOL_CXX"
        a24="--trace=AC_LIBTOOL_DLOPEN"
        a25="--trace=AC_LIBTOOL_DLOPEN_SELF"
        a26="--trace=AC_LIBTOOL_F77"
        a27="--trace=AC_LIBTOOL_FC"
        a28="--trace=AC_LIBTOOL_GCJ"
        a29="--trace=AC_LIBTOOL_LANG_CXX_CONFIG"
        a30="--trace=AC_LIBTOOL_LANG_C_CONFIG"
        a31="--trace=AC_LIBTOOL_LANG_F77_CONFIG"
        a32="--trace=AC_LIBTOOL_LANG_GCJ_CONFIG"
        a33="--trace=AC_LIBTOOL_LANG_RC_CONFIG"
        a34="--trace=AC_LIBTOOL_LINKER_OPTION"
        a35="--trace=AC_LIBTOOL_OBJDIR"
        a36="--trace=AC_LIBTOOL_PICMODE"
        a37="--trace=AC_LIBTOOL_POSTDEP_PREDEP"
        a38="--trace=AC_LIBTOOL_PROG_CC_C_O"
        a39="--trace=AC_LIBTOOL_PROG_COMPILER_NO_RTTI"
        a40="--trace=AC_LIBTOOL_PROG_COMPILER_PIC"
        a41="--trace=AC_LIBTOOL_PROG_LD_HARDCODE_LIBPATH"
        a42="--trace=AC_LIBTOOL_PROG_LD_SHLIBS"
        a43="--trace=AC_LIBTOOL_RC"
        a44="--trace=AC_LIBTOOL_SETUP"
        a45="--trace=AC_LIBTOOL_SYS_DYNAMIC_LINKER"
        a46="--trace=AC_LIBTOOL_SYS_GLOBAL_SYMBOL_PIPE"
        a47="--trace=AC_LIBTOOL_SYS_HARD_LINK_LOCKS"
        a48="--trace=AC_LIBTOOL_SYS_LIB_STRIP"
        a49="--trace=AC_LIBTOOL_SYS_MAX_CMD_LEN"
        a50="--trace=AC_LIBTOOL_SYS_OLD_ARCHIVE"
        a51="--trace=AC_LIBTOOL_WIN32_DLL"
        a52="--trace=AC_LIB_LTDL"
        a53="--trace=AC_LTDL_DLLIB"
        a54="--trace=AC_LTDL_DLSYM_USCORE"
        a55="--trace=AC_LTDL_ENABLE_INSTALL"
        a56="--trace=AC_LTDL_OBJDIR"
        a57="--trace=AC_LTDL_PREOPEN"
        a58="--trace=AC_LTDL_SHLIBEXT"
        a59="--trace=AC_LTDL_SHLIBPATH"
        a60="--trace=AC_LTDL_SYMBOL_USCORE"
        a61="--trace=AC_LTDL_SYSSEARCHPATH"
        a62="--trace=AC_LTDL_SYS_DLOPEN_DEPLIBS"
        a63="--trace=AC_PATH_MAGIC"
        a64="--trace=AC_PATH_TOOL_PREFIX"
        a65="--trace=AC_PROG_EGREP"
        a66="--trace=AC_PROG_LD"
        a67="--trace=AC_PROG_LD_GNU"
        a68="--trace=AC_PROG_LD_RELOAD_FLAG"
        a69="--trace=AC_PROG_LIBTOOL"
        a70="--trace=AC_PROG_NM"
        a71="--trace=AC_WITH_LTDL"
        a72="--trace=AM_AUTOMAKE_VERSION"
        a73="--trace=AM_AUX_DIR_EXPAND"
        a74="--trace=AM_CONDITIONAL"
        a75="--trace=AM_DEP_TRACK"
        a76="--trace=AM_DISABLE_SHARED"
        a77="--trace=AM_DISABLE_STATIC"
        a78="--trace=AM_ENABLE_SHARED"
        a79="--trace=AM_ENABLE_STATIC"
        a80="--trace=AM_INIT_AUTOMAKE"
        a81="--trace=AM_MAKE_INCLUDE"
        a82="--trace=AM_MISSING_HAS_RUN"
        a83="--trace=AM_MISSING_PROG"
        a84="--trace=AM_OUTPUT_DEPENDENCY_COMMANDS"
        a85="--trace=AM_PROG_CC_C_O"
        a86="--trace=AM_PROG_INSTALL_SH"
        a87="--trace=AM_PROG_INSTALL_STRIP"
        a88="--trace=AM_PROG_LD"
        a89="--trace=AM_PROG_LIBTOOL"
        a90="--trace=AM_PROG_NM"
        a91="--trace=AM_RUN_LOG"
        a92="--trace=AM_SANITY_CHECK"
        a93="--trace=AM_SET_CURRENT_AUTOMAKE_VERSION"
        a94="--trace=AM_SET_DEPDIR"
        a95="--trace=AM_SET_LEADING_DOT"
        a96="--trace=AM_SILENT_RULES"
        a97="--trace=AM_SUBST_NOTMAKE"
        a98="--trace=AU_DEFUN"
        a99="--trace=LTDL_CONVENIENCE"
        a100="--trace=LTDL_INIT"
        a101="--trace=LTDL_INSTALLABLE"
        a102="--trace=LTOBSOLETE_VERSION"
        a103="--trace=LTOPTIONS_VERSION"
        a104="--trace=LTSUGAR_VERSION"
        a105="--trace=LTVERSION_VERSION"
        a106="--trace=LT_AC_PROG_EGREP"
        a107="--trace=LT_AC_PROG_GCJ"
        a108="--trace=LT_AC_PROG_RC"
        a109="--trace=LT_AC_PROG_SED"
        a110="--trace=LT_CMD_MAX_LEN"
        a111="--trace=LT_CONFIG_LTDL_DIR"
        a112="--trace=LT_FUNC_ARGZ"
        a113="--trace=LT_FUNC_DLSYM_USCORE"
        a114="--trace=LT_INIT"
        a115="--trace=LT_LANG"
        a116="--trace=LT_LIB_DLLOAD"
        a117="--trace=LT_LIB_M"
        a118="--trace=LT_OUTPUT"
        a119="--trace=LT_PATH_LD"
        a120="--trace=LT_PATH_NM"
        a121="--trace=LT_PROG_GCJ"
        a122="--trace=LT_PROG_GO"
        a123="--trace=LT_PROG_RC"
        a124="--trace=LT_SUPPORTED_TAG"
        a125="--trace=LT_SYS_DLOPEN_DEPLIBS"
        a126="--trace=LT_SYS_DLOPEN_SELF"
        a127="--trace=LT_SYS_DLSEARCH_PATH"
        a128="--trace=LT_SYS_MODULE_EXT"
        a129="--trace=LT_SYS_MODULE_PATH"
        a130="--trace=LT_SYS_SYMBOL_USCORE"
        a131="--trace=LT_WITH_LTDL"
        a132="--trace=_AC_AM_CONFIG_HEADER_HOOK"
        a133="--trace=_AC_PROG_LIBTOOL"
        a134="--trace=_AM_AUTOCONF_VERSION"
        a135="--trace=_AM_CONFIG_MACRO_DIRS"
        a136="--trace=_AM_DEPENDENCIES"
        a137="--trace=_AM_IF_OPTION"
        a138="--trace=_AM_MANGLE_OPTION"
        a139="--trace=_AM_OUTPUT_DEPENDENCY_COMMANDS"
        a140="--trace=_AM_PROG_CC_C_O"
        a141="--trace=_AM_PROG_TAR"
        a142="--trace=_AM_SET_OPTION"
        a143="--trace=_AM_SET_OPTIONS"
        a144="--trace=_AM_SUBST_NOTMAKE"
        a145="--trace=_LTDL_SETUP"
        a146="--trace=_LT_AC_CHECK_DLFCN"
        a147="--trace=_LT_AC_FILE_LTDLL_C"
        a148="--trace=_LT_AC_LANG_CXX"
        a149="--trace=_LT_AC_LANG_CXX_CONFIG"
        a150="--trace=_LT_AC_LANG_C_CONFIG"
        a151="--trace=_LT_AC_LANG_F77"
        a152="--trace=_LT_AC_LANG_F77_CONFIG"
        a153="--trace=_LT_AC_LANG_GCJ"
        a154="--trace=_LT_AC_LANG_GCJ_CONFIG"
        a155="--trace=_LT_AC_LANG_RC_CONFIG"
        a156="--trace=_LT_AC_LOCK"
        a157="--trace=_LT_AC_PROG_CXXCPP"
        a158="--trace=_LT_AC_PROG_ECHO_BACKSLASH"
        a159="--trace=_LT_AC_SHELL_INIT"
        a160="--trace=_LT_AC_SYS_COMPILER"
        a161="--trace=_LT_AC_SYS_LIBPATH_AIX"
        a162="--trace=_LT_AC_TAGCONFIG"
        a163="--trace=_LT_AC_TAGVAR"
        a164="--trace=_LT_AC_TRY_DLOPEN_SELF"
        a165="--trace=_LT_CC_BASENAME"
        a166="--trace=_LT_COMPILER_BOILERPLATE"
        a167="--trace=_LT_COMPILER_OPTION"
        a168="--trace=_LT_DLL_DEF_P"
        a169="--trace=_LT_LIBOBJ"
        a170="--trace=_LT_LINKER_BOILERPLATE"
        a171="--trace=_LT_LINKER_OPTION"
        a172="--trace=_LT_PATH_TOOL_PREFIX"
        a173="--trace=_LT_PREPARE_SED_QUOTE_VARS"
        a174="--trace=_LT_PROG_CXX"
        a175="--trace=_LT_PROG_ECHO_BACKSLASH"
        a176="--trace=_LT_PROG_F77"
        a177="--trace=_LT_PROG_FC"
        a178="--trace=_LT_PROG_LTMAIN"
        a179="--trace=_LT_REQUIRED_DARWIN_CHECKS"
        a180="--trace=_LT_WITH_SYSROOT"
        a181="--trace=_m4_warn"
        a182="--trace=include"
        a183="--trace=m4_include"
        a184="--trace=m4_pattern_allow"
        a185="--trace=m4_pattern_forbid"
        a186="--reload-state=/usr/share/autoconf-2.60/autoconf/autoconf.m4f"
        a187="--undefine=__m4_version__"
        a188="-"
        a189="/usr/share/aclocal-1.16/internal/ac-config-macro-dirs.m4"
        a190="/usr/share/libtool/aclocal/libtool.m4"
        a191="/usr/share/libtool/aclocal/ltargz.m4"
        a192="/usr/share/libtool/aclocal/ltdl.m4"
        a193="/usr/share/libtool/aclocal/ltoptions.m4"
        a194="/usr/share/libtool/aclocal/ltsugar.m4"
        a195="/usr/share/libtool/aclocal/ltversion.m4"
        a196="/usr/share/libtool/aclocal/lt~obsolete.m4"
        a197="/usr/share/aclocal-1.16/amversion.m4"
        a198="/usr/share/aclocal-1.16/auxdir.m4"
        a199="/usr/share/aclocal-1.16/cond.m4"
        a200="/usr/share/aclocal-1.16/depend.m4"
        a201="/usr/share/aclocal-1.16/depout.m4"
        a202="/usr/share/aclocal-1.16/init.m4"
        a203="/usr/share/aclocal-1.16/install-sh.m4"
        a204="/usr/share/aclocal-1.16/lead-dot.m4"
        a205="/usr/share/aclocal-1.16/make.m4"
        a206="/usr/share/aclocal-1.16/missing.m4"
        a207="/usr/share/aclocal-1.16/options.m4"
        a208="/usr/share/aclocal-1.16/prog-cc-c-o.m4"
        a209="/usr/share/aclocal-1.16/runlog.m4"
        a210="/usr/share/aclocal-1.16/sanity.m4"
        a211="/usr/share/aclocal-1.16/silent.m4"
        a212="/usr/share/aclocal-1.16/strip.m4"
        a213="/usr/share/aclocal-1.16/substnot.m4"
        a214="/usr/share/aclocal-1.16/tar.m4"
        a215="configure.ac"

    record 3 of type 1307(CWD) has 2 fields
    line=10 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=CWD
        cwd="/usr/src/RPM/BUILD/zlib-1.2.11-alt1/contrib/minizip"

    record 4 of type 1302(PATH) has 15 fields
    line=11 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=PATH
        item=0
        name="/usr/bin/m4"
        inode=40839
        dev=00:30
        mode=0100755
        ouid=582
        ogid=582
        rdev=00:00
        nametype=NORMAL
        cap_fp=0
        cap_fi=0
        cap_fe=0
        cap_fver=0
        cap_frootid=0

    record 5 of type 1302(PATH) has 15 fields
    line=12 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=PATH
        item=1
        name="/lib64/ld-linux-aarch64.so.1"
        inode=33874
        dev=00:30
        mode=0100755
        ouid=582
        ogid=582
        rdev=00:00
        nametype=NORMAL
        cap_fp=0
        cap_fi=0
        cap_fe=0
        cap_fver=0
        cap_frootid=0

    record 6 of type 1327(PROCTITLE) has 2 fields
    line=13 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=PROCTITLE
        proctitle=2F7573722F62696E2F6D34002D2D6E657374696E672D6C696D69743D31303234002D2D676E75002D2D696E636C7564653D2F7573722F73686172652F6175746F636F6E662D322E3630002D2D64656275673D61666C71002D2D666174616C2D7761726E696E67002D2D646562756766696C653D6175746F6D3474652E63616368

Test 11 Done

Finished non-admin tests

