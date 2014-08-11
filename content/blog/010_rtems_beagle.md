Title: Beagleboard xM, Beaglebone black and everything else RTEMS on the Beagles
Date: 2014-07-22 09:15
Category: Blog
Tags: beagle,beaglebone,beagleboard,rtems
Summary: How to get everything RTEMS running on everything Beagle from scratch.

Everything about RTEMS on Beagleboards & Beaglebones
====================================================

![Beagleboard]({filename}/images/beagle.jpg)

Welcome to the 10th post!

Purpose of this post
--------------------
Don't have anything RTEMS installed on your machine but want to get it running on the Beaglebone? Or curious about how it runs, but don't have the hardware and want to run it in an emulator? Read on.

Who am I kidding. Everyone wants that!

This post will show you in detail how to get RTEMS applications running from scratch on the BeagleBoard xM, Beaglebone and Beaglebone Black. Actually it should work on the original BeagleBoard too but I don't have that hardware to test it.

Introduction
------------

As faithful readers know, I am working on RTEMS support for the Beagleboard, Beaglebone and Beaglebone Black. There has been quite some interest in Beagle support for RTEMS on the RTEMS mailing lists recently, quite suddenly I thought. That made me decide to offer the current state of the BSP for merging with RTEMS mainline. The alternative is to keep polishing it and improving support out-of-tree. But that is better done from RTEMS mainline now.

So as mentioned, the purpose of this post is to start from nothing RTEMS-specific and build everything needed to run an RTEMS app on your Beagle target. As you'll see it isn't labour-intensive.

Acknowledgements
----------------
Chris Johns helped guide the polishing of the BSP a lot when I first came
up with it (he didn't call it Ben and Chris's Big Beagleboard Adventure for
nothing!). Brandon Matthews asked a question about running RTEMS on the
Beaglebone once and has since been very patient and helpful in collaborating
to move the process along. Claas Ziemke
started the, as-yet unmerged, original Beagleboard BSP for GSoC in 2012.

About Where the Code Is
-----------------------
There are 3 repo's to be concerned with:

  *  The RTEMS Source builder, or RSB, which builds a bunch of tools and dependencies to build RTEMS itself
  *  RTEMS itself; hardware-specific code (the BSP's) and generic code (RTEMS core)
  *  RTEMS tools. We use it to automatically execute the RTEMS test suite.

All these repositories have work in them by me to support building
& testing the BSP. Currently they are not merged with RTEMS official
repositories. If and when they are, I will update this post to
reflect the official locations.

First: build the toolchain, uboot, qemu and supporting utilities
----------------------------------------------------------------

The toolchain is needed to actually compile code to run on the Beagles. Fortunately the [RTEMS Source Builder](http://www.rtems.org/wiki/index.php/RTEMS_Source_Builder) provides a way to do this in an automated, repeatable fashion. Also called the RSB. I have added some packages to the RSB to facilitate testing and preparing an SD card image to boot and run on Beagle targets.

This is combined in the bset 'beagle' and is all built with the following simple commands. We start by creating the directory all the RTEMS-specific stuff wil happen in, both binaries and sources. I am choosing $HOME/development/rtems/.

        % mkdir -p development/rtems/sources
        % cd development/rtems/sources

The RSB has bsets you can choose from which are a set of tools with all needed dependencies. There is a toolchain bset for instance. I added a beagle bset which contains the toolchain and all other utilities and software we need.

Check you have the dependencies the RSB itself depends on. Go to the
[RTEMS Source Builder Host Setups](http://www.rtems.org/ftp/pub/rtems/people/chrisj/source-builder/source-builder.html#_host_setups) section and look for your OS.
I've tested this on Ubuntu and FreeBSD and it doesn't quite go out-of-the-box otherwise.

Now fetch the RSB.

        % git clone -b beagle https://github.com/bengras/rtems-source-builder.git
        Cloning into 'rtems-source-builder'...
        remote: Reusing existing pack: 3999, done.
        remote: Counting objects: 16, done.
        remote: Compressing objects: 100% (15/15), done.
        remote: Total 4015 (delta 2), reused 3 (delta 1)
        Receiving objects: 100% (4015/4015), 2.96 MiB | 1.13 MiB/s, done.
        Resolving deltas: 100% (2361/2361), done.

First verify the basic dependencies are on the system.

	% ./rtems-source-builder/source-builder/sb-check 
	RTEMS Source Builder - Check, v0.3.0
	Environment is ok

Then build the beagle bset. We tell RSB to install the binaries under the $HOME/development/rtems/4.11 prefix.

        % cd rtems-source-builder/rtems
        % ../source-builder/sb-set-builder --log=beagle.txt --prefix=$HOME/development/rtems/4.11 devel/beagle.bset

Ok, great. This will have built the toolchain with the right target, qemu, uboot, and some supporting utilities needed to prepare the SD card. They are all under $HOME/development/rtems/4.11. We will use these soon enough.

Next: build RTEMS, Beagle BSPs and test suite
---------------------------------------------
Time for the main act - the RTEMS code itself. We enable the Beagle BSP, build all the RTEMS code. 

At configure time, we can specify any set of four Beagle sub-BSPs: beagleboard, beagleboardxm, beaglebonewhite and beagleboneblack. beaglebonewhite is the original beaglebone but it's sometimes called white to dis-ambiguate it. In the BSP code there are only two cases but hardware-specific changes might change that in the future; so we have 4 cases now so the usage needn't change.

OK let's build the beagleboardxm and beagleboneblack BSPs!

First set the $PATH to include the built tools:

    % cd $HOME/development/rtems
    % export PATH=$HOME/development/rtems/4.11/bin:$PATH

Now fetch the code:

        % git clone -b beaglebone-wip https://github.com/bengras/rtems.git rtems-src
        Cloning into 'rtems-src'...
        remote: Counting objects: 450470, done.
        remote: Compressing objects: 100% (81722/81722), done.
        remote: Total 450470 (delta 359488), reused 450131 (delta 359253)
        Receiving objects: 100% (450470/450470), 68.41 MiB | 1.58 MiB/s, done.
        Resolving deltas: 100% (359488/359488), done.
        % cd rtems-src 
    
The bootstrap step to generate the configure files:

        % ./bootstrap; ./bootstrap -p
        % cd ..    
    
Configure everything, selecting the beagleboneblack and the beagleboardxm modes. We also tell it to build the full test suite (--enable-tests) and for this reason we make the console operate in polled mode, a requirement for the tests to be run. On this BSP that is accomplished by setting CONSOLE_POLLED=1 at configure time. The default is interrupt-driven mode.

        % mkdir b-beagle ; cd b-beagle
        % CONSOLE_POLLED=1 ../rtems-src/configure --target=arm-rtems4.11 --enable-rtemsbsp="beagleboneblack beagleboardxm" --enable-tests
        % make

If all went according to plan, you have a bunch of .exe files in the $HOME/development/rtems/b-beagle/arm-rtems4.11/c hierarchy. The full set twice - once linked with the beagleboardxm BSP, and once with the beagleboneblack BSP.

Aside - How to run an ELF RTEMS image on a Beagle
-------------------------------------------------
Something that isn't actually so obvious. We have an ELF-formatted .exe file now. How will that be loaded and executed on our targets? That is highly target-specific, and out of scope for RTEMS itself. Somehow the hardware has to be initialized. The file has to be loaded into memory in the right place and with the right initialization. Then the cpu has to be sent there. All this is not done by RTEMS itself, it can't. Usually we rely on a bootloader to do this.

There are many options, but to get started, this page shows you how to write an SD card with an RTEMS image and a boot loader on it, completely self-contained.

Other options are netbooting (so you don't have to write an SD card every time you want to boot something else) or loading with JTAG (no SD card or bootloader needed at all).

We need uboot and several other tools to prepare a partitioned  SD card with a filesystem on it.

It would be a chore to make the user re-invent this all the time, so we rely on a script that is in the RTEMS tree already.

Run the test suite
------------------
To track whether all code actually performs as expected with this BSP, we can automatically run all the RTEMS tests. Every piece of test code is linked with this BSP and executed. These are currently 501 tests. Each one is considered a success (passed) if it displays the start and end banner as its output. 

It is a great correctness baseline to establish, as future regressions (whether caused by changes in the BSP itself or not) can then be automatically caught. We simulate this execution so the target hardware isn't required to run the test set.

First we fetch RTEMS tools, containing the testing code:

        % cd $HOME/development/rtems
        % git clone -b bbxm-wip https://github.com/bengras/rtems-tools.git rtems-tools

Earlier, the RTEMS source builder has fetched and built a lot of required tools to actually run a test. There is a script in the RTEMS tester tree that takes an RTEMS executable, processes it into an image that uboot will load (using objdump and mkimage), put it together with MLO and uboot on a filesystem, and write an SD card image with it.

We can then simulate its execution with the Linaro fork of qemu, which emulates a beagleboard xM in software.

This is invoked automatically for every test executable by the RTEMS beagleboardxm_qemu tester. Here we go:

        % cd rtems-tools/tester
        % ./rtems-test --log=bbxm.log --report-mode=all --rtems-bsp=beagleboardxm_qemu --rtems-tools=$HOME/development/rtems/4.11 $HOME/development/rtems/b-beagle/arm-rtems4.11/c/beagleboardxm

This will (on my machine) run for 30 minutes, executing all the tests, with parallelism even, a very nice system. The output in my case:

        Passed:   497
        Failed:     3
        Timeouts:   1
        Invalid:    0
        Total:    501
        Average test time: 0:00:03.534494
        Testing time     : 0:29:30.781935

So there are a few tests I should still diagnose before the baseline is as clean as it should be. But a pretty good start I'd say!

Writing an SD card image for the Beaglebone Black
-------------------------------------------------

In the RTEMS source tree itself there is a similar script to the above that lets you write an SD card image with a specific RTEMS executable on it. Let's write one for the Beaglebone Black:

        % cd $HOME/development/rtems/rtems-src/c/src/lib/libbsp/arm/beagle/simscripts
        % sh sdcard.sh $HOME/development/rtems/4.11 $HOME/development/rtems/b-beagle/arm-rtems4.11/c/beagleboneblack/testsuites/samples/hello/hello.exe

The script should give you a whole bunch of output, ending in:

        Result is in bone_hello.exe-sdcard.img.

There you go. dd that to an SD card .. (/dev/mmcblk0 in my case. careful!)

	# dd if=bone_hello.exe-sdcard.img of=/dev/mmcblk0 bs=4096

.. and boot!

		# picocom -b 115200 /dev/ttyUSB0
		U-Boot SPL 2014.04-00015-gb4422bd (Apr 22 2014 - 13:24:29)
		reading args
		spl_load_image_fat_os: error reading image args, err - -1
		reading u-boot.img
		reading u-boot.img
		
		
		U-Boot 2014.04-00015-gb4422bd (Apr 22 2014 - 13:24:29)
		
		I2C:   ready
		DRAM:  512 MiB
		NAND:  0 MiB
		MMC:   OMAP SD/MMC: 0, OMAP SD/MMC: 1
		*** Warning - readenv() failed, using default environment
		
		Net:   <ethaddr> not set. Validating first E-fuse MAC
		cpsw, usb_ether
		Hit any key to stop autoboot:  0 
		gpio: pin 53 (gpio 53) value is 1
		mmc0 is current device
		gpio: pin 54 (gpio 54) value is 1
		SD/MMC found on device 0
		reading uEnv.txt
		99 bytes read in 5 ms (18.6 KiB/s)
		gpio: pin 55 (gpio 55) value is 1
		Loaded environment from uEnv.txt
		Importing environment from mmc ...
		Checking if uenvcmd is set ...
		gpio: pin 56 (gpio 56) value is 1
		Running uenvcmd ...
		reading rtems-app.img
		58629 bytes read in 11 ms (5.1 MiB/s)
		## Booting kernel from Legacy Image at 80800000 ...
		   Image Name:   RTEMS
		   Image Type:   ARM RTEMS Kernel Image (gzip compressed)
		   Data Size:    58565 Bytes = 57.2 KiB
		   Load Address: 80000000
		   Entry Point:  80000000
		   Verifying Checksum ... OK
		   Uncompressing Kernel Image ... OK
		## Transferring control to RTEMS (at address 80000000) ...
		
		RTEMS Beagleboard: am335x-based
		
		
		*** BEGIN OF TEST HELLO WORLD ***
		Hello World
		*** END OF TEST HELLO WORLD ***
		

The script needs to know whether it's for a Beagleboard xM or one of the
Beaglebones. This is to know which uboot to use. It will detect this from the
path the executable is in, so you have to specify the full path.

Running with the Beagleboard xM over JTAG
-----------------------------------------
This is a slightly more advanced use. Connect a flyswatter or flyswatter2 to a Beagleboard xM and you can load and run RTEMS executables on it without any other dependencies - Beagle from scratch. No bootloader, nothing. You will need openocd for this.

Still from the simscripts dir, first start openocd. I have a flywatter but you can also specify a flyswatter2.cfg:

		% cd $HOME/development/rtems/rtems-src/c/src/lib/libbsp/arm/beagle/simscripts
		% openocd -f interface/ftdi/flyswatter.cfg -f bbxm.cfg -c'reset init'

openocd should now be talking to your bbxm and be offering a gdb interface. Using gdb we can load and run RTEMS executables.

Try it:

        # mkdir bbxm-gdb
        # cd bbxm-gdb 
        # cp ../gdbinit.bbxm .gdbinit
        # arm-rtems4.11-gdb $HOME/development/rtems/b-beagle/arm-rtems4.11/c/beagleboardxm/testsuites/samples/ticker/ticker.exe
        GNU gdb (GDB) 7.7
        -snip-
        Breakpoint 10 at 0x80015dcc: file ../../../../../../rtems-src/c/src/../../cpukit/libcsupport/src/newlibc_exit.c, line 37.
        (gdb)

The executable is now ready to run but halted. Start with 'continue':

        (gdb) c
        Continuing.
        Breakpoint 10, _exit (status=0)
            at ../../../../../../rtems-src/c/src/../../cpukit/libcsupport/src/newlibc_exit.c:37
        37      {
        (gdb)

The gdb interface is very powerful as the loading & running is convenient, full debug info is available,  breakpoints all work and the build & run cycle is very short.

Running the full test suite over JTAG
-------------------------------------

Doing the above in batch mode lets us run the full test suite on hardware, the only real test of course. We specify the beagleboardxm bsp insteadof the beagleboardxm_qemu bsp. This one will talk to gdb to load and run the executable each time.

        # cd $HOME/development/rtems/rtems-tools/tester
        # ./rtems-test --log=bbxm-jtag.log --report-mode=all --rtems-bsp=beagleboardxm --rtems-tools=$HOME/development/rtems/4.11 $HOME/development/rtems/b-beagle/arm-rtems4.11/c/beagleboardxm

That is it! Everything RTEMS on Beagle!

What I've Tested
----------------
I have personally tested everything in the above procedure, i.e.

  1. That building all the tools and utilities from scratch work, using the RTEMS Source Builder repository (Ubuntu + FreeBSD).
  1. That building the beaglebone and bbxm BSPs and linking them with all the testsuite programs works (Ubuntu + FreeBSD).
  1. That the beaglexm-emulating linaro qemu executes all of those tests properly, invoked using a single command line with the scripts in the RTEMS tools repository, even though not all pass currently (Ubuntu + FreeBSD).
  1. That loading & running over JTAG works, both interactively with gdb and in a batch using gdb and the test runner.
  1. That running RTEMS executables using u-boot on the beaglebones from sd card work; both with and without MMU enabled at RTEMS start time.

Additionally, I've also tested the work by Claas Ziemke rebased on
current rtems mainline builds. My changes are in a separate commit in order
to preserve credit where it's due.

What's next
-----------
Gee don't put me on the spot!

I want to diagnose the failure reasons of the tests in the emulator and on
hardware (different).

Some form of continuous integration to keep verifying the BSP with future
commits would be a good idea too!

Also I want to get JTAG working on the beaglebone white, which would be an
extremely powerful setup - console, power and jtag all over one USB cable?
God have mercy.

When I'm feeling brave I'd like to get the ethernet hardware working on the
Beaglebones. But first things first. Let me know if you enjoy the BSP!
