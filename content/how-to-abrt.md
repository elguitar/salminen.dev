Title: How to ABRT 
Date: 2019-11-20 20:22
Modified: 2019-11-20 20:22
Slug: how-to-abrt 
Authors: Petri Salminen
Summary: How to use ABRT program on Fedora and be a good citizen

## Description of the problem

I ran into problems with [FreeCAD](https://freecadweb.org) on [Fedora](https://getfedora.org). I was following a tutorial about [BIM Modeling with FreeCAD](https://www.freecadweb.org/wiki/Manual:BIM_modeling), when FreeCAD crashed when I tried to switch to Arch Workbench.

## Finding the right binary

A common way to troubleshoot a situation like this is to try to run the application from the command line. I first tried `freecad`, but it didn't work. Next, since I new that there is a `.desktop` file for FreeCAD executable, I went and inspected it. One of my favourite command line tools is [ag](https://github.com/ggreer/the_silver_searcher). It is pretty much like recursive grep, but faster and prettier.

```
petri:~/ $ ag freecad /usr/share/applications
/usr/share/applications/org.freecadweb.FreeCAD.desktop
2:Name=FreeCAD
3:Name[de]=FreeCAD
4:Name[pl]=FreeCAD
10:Exec=FreeCAD %F
13:Icon=org.freecadweb.FreeCAD
```

`ag` did its job and found the `.desktop`-file. On line 10, there is the `Exec`-line, which tells which binary is run when the `.desktop`-file is called. It seems that `FreeCAD` is the way to go!

## Running

```
$ FreeCAD
# Normal output suppressed
FreeCAD: malloc.c:2389: sysmalloc: Assertion `(old_top == initial_top (av) && old_size == 0) || ((unsigned long) (old_size) >= MINSIZE && prev_inuse (old_top) && ((unsigned long) old_end & (pagesize - 1)) == 0)' failed.
[1]    5410 abort (core dumped)  FreeCAD
$
```

Sometimes a reboot helps if something gets a [segmentation fault](https://en.wikipedia.org/wiki/Segmentation_fault). However, it didn't work out this time :( I tried to find a similar problems with a certain search engine, but was unable to find any. I decided to report the bug using ABRT.

## ABRT

ABRT is an abbrevation for [Automatic Bug Reporting Tool](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-abrt). It is a program developed by Red Hat to make it easier to report bugs. It comes pre-installed on Red Hat -based systems (Fedora, CentOS, Red Hat).

First, I ran `abrt` from the command line just to see if the segfault was registered in `abrt`:

```
$ abrt
a0d9190 3x freecad 2019-11-20 20:07:16
```

Cool! `abrt` managed to register the segfault that already happened. To file the bug, just run `abrt report`.

NOTE! The report can take a long time and can install lots of debuginfo -libraries, which are not usually needed for "normal" computerstuff.

```
$ abrt report
Reporting problem a0d9190

no actions matching this problem found for event 'collect_vimrc_system'
no actions matching this problem found for event 'collect_GConf'
('report_uReport' completed successfully)
Element 'xsession_errors' saved
no actions matching this problem found for event 'collect_vimrc_user'
Ok to upload core dump? (It may contain sensitive data). If your answer is 'No', a stack trace will be generated locally. (It may download a huge amount of data). [y/N/f/e] y
Querying server settings
Preparing an archive to upload
You are going to upload 18.0 MiB. Continue? [y/N] y
Uploading 18.0 MiB
Upload successful
Retrace job started
Analyzing crash data
.....................
Preparing environment for backtrace generation
................................
Generating backtrace
...
Cleaning environment after backtrace generation
Retrace job finished successfully
Looking for similar problems in bugzilla
Bugzilla User name: salminen.petri.m@gmail.com
Bugzilla Password:

The report has been updated
Logging into Bugzilla at https://bugzilla.redhat.com
Checking for duplicates
Can't generate stacktrace description (no crash thread?)
Creating a new bug
New bug id: 1774705
Adding External URL to bug 1774705
Adding attachments to bug 1774705
Logging out
Status: NEW https://bugzilla.redhat.com/show_bug.cgi?id=1774705
('post_report' completed successfully)
```

## Conclusion

WOW! I never new that bug reporting was this easy. Please remember to report bugs whenever possible to make Fedora better in the long run!
