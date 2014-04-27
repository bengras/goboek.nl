Title: Beagle from scratch, or: adventures in JTAG, part 1
Date: 2014-04-26 15:11
Category: Blog
Tags: beagle,jtag,rtems
Summary: Executing code on a BeagleBoard XM without any bootcode.

Below is a story of what I've learned about what it takes to
boot a Beagleboard.

## BeagleBoard XM on reset - a barren wasteland

Without boot code such as [U-Boot](http://www.denx.de/wiki/U-Boot)
running first, very little is actually working. Most noticeably,
there is no usable UART or external RAM, and quite a lot of
initialization is necessary before they are both in a usable state.
The only available RAM is 128kB that is on the SOC itself. There is
also some ROM that contains code which is the first thing that
starts executing on reset.

## How initialization can be done

The usual case is that on reset, the ROM boot code searches boot
devices to find the second-stage bootcode to be executed from the
128kB RAM. Its only task is to initialize RAM and other necessary
peripherals so that the next stage bootloader can be loaded and
executed. This executable is called MLO in TI parlance and it
can be fulfilled by an SPL build of U-Boot. The ROM boot code
is smart enough to parse a partition table and FAT filesystem
and load the MLO to the 128kB on-SOC RAM if there is an MLO on
the MMC. Other boot devices are possible also.

## What MLO then does

The U-Boot MLO initializes whatever PLLs, clocks, controllers and
RAM is necessary to get a working UART, external RAM and MMC device.
It is then able to load the full U-Boot from the MMC device into RAM
and execute it. Full U-Boot has much more peripheral support and
other supporting features to load the next step, i.e. the
operating system or application.

## What we want so we can test RTEMS

[As mentioned](|filename|005_rtems.class.md), I am working on a
[BSP](http://www.rtems.org/wiki/index.php/Board_Support_Packages) for the
[Beagle](http://www.beagleboard.org) family of products for
[RTEMS](http://www.rtems.org). In other words, a port of RTEMS to the
beagles; specifically the BeagleBoard XM, BeagleBone 'White,' and the
BeagleBone Black.

My friend [Chris](https://github.com/kiwichris), in testing
my BSP, has introduced me to the powerful notion of what I might
call running-from-scratch. Specifically, getting the hardware, after
reset, into a state where it can load and run an RTEMS binary, absent
a boot loader. This eliminates a lot of dependency on what kind of
state a bootloader might leave the hardware in. And it also eliminates
needing any external software to load & run RTEMS for unattended
testing. We have taken to doing this with 
[JTAG](http://en.wikipedia.org/wiki/Joint_Test_Action_Group).

Running without boot code affords us full control. The full system
state is known, which has as advantage that once it works for us,
it should work everywhere. The bootloader is eliminated as a
dependency in determining the system state once the RTEMS binary
starts running. The disadvantage is that we have to figure out how
to load the RTEMS executable, and how to get the hardware into a
usable state without the help of MLO or U-Boot. We can do all this
with JTAG.

## Initializing the board with JTAG

My approach has been to duplicate the initialization procedure that U-Boot
SPL (i.e. their MLO) does with JTAG. I executed it in qemu and traced all
memory i/o operations it uses to initialize the hardware. Then I could
recreate then in OpenOCD as a series of writes and so reset the board
and initialize it on every GDB attachment. Now we can run RTEMS
executables over JTAG without any additional software needed!

## Code

[The RTEMS code is here](https://github.com/bengras/rtems/tree/beaglebone-wip). It contains
the OpenOCD configuration to initialize the beagleboard.

[The RTEMS tester code is here](https://github.com/bengras/rtems-tools). It contains the
gdb configuration necessary to control OpenOCD properly to load & execute binaries, while
also setting the proper breakpoints to let the tests pass.

I will post a full tutorial on how to build and run everything in the future.

## Running RTEMS tests

The next step is to build and run all RTEMS tests on the Beagleboard XM
unattended. I will also post an update on how the tests are running.
