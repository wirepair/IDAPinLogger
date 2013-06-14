IDAPinLogger:
================================

Author: @_wirepair / isaac.dawson{}gmail.com.

Keeps a hit count for every instruction executed in a specified module.
If no module is specified, we use the main executable image.
After the program finishes running, we write the buffer of hits out to a file which
then needs to be imported into IDA Pro using dereko's (?) loadlog.py IDAPython script.


I feel this method is a bit more simpiler then his (and I was having problems with
certain executables). But who knows maybe i'm doing something wrong :).

Update: It is now possible to specify when logging should begin/end by giving an offset
to an instruction where, after it is called logging should start. Also by specifying
an end instruction, logging will stop. This makes it much easier to identify code paths
that are taken after a certain point with in the applications life cycle.


How to build:
-------------------------

Copy this project into your pin source directory:
%pin%\source\tools\IDAPinLogger
Open Visual Studio (2008) and build.

How to run:
-------------------------

Log all hits in nc.exe module:

c:\pin\pin.exe -t C:\pin\IDAPinLogger.dll -m nc.exe -- nc.exe -l -v -p 999

or (main exe assumed)

c:\pin\pin.exe -t C:\pin\IDAPinLogger.dll -- nc.exe -l -v -p 999

Log all hits in supporting module (note case sensitive!):

c:\pin\pin.exe -t C:\pin\IDAPinLogger.dll -m KERNEL32.DLL -- nc.exe -l -v -p 999

Only start logging hits after instruction at base+0x991c is hit, stop logging after base+0x4242 is hit:
c:\pin\pin.exe -t C:\pin\IDAPinLogger.dll -s 0x991c -e 0x4242 -- nc.exe -l -v -p 999