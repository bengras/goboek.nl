Title: Beagle from scratch, or: adventures in JTAG, part 1
Date: 2014-04-21 1:46
Category: Blog
Tags: beagle,jtag,rtems
Summary: Executing code on a BeagleBoard XM without any bootcode.

I am working on a
[BSP](http://www.rtems.org/wiki/index.php/Board_Support_Packages) for the
[Beagle](http://www.beagleboard.org) family of products for
[RTEMS](http://www.rtems.org). In other words, a port of RTEMS to the
beagles; specifically the BeagleBoard XM, BeagleBone 'White,' and the
BeagleBone Black.

My friend [Chris](https://github.com/kiwichris), in testing
my BSP, has introduced me to the powerful notion of what I might
call running-from-scratch. Specifically, getting the hardware, after
reset, into a state where it can load and run an RTEMS binary, absent
a boot loader.

Without boot code such as [U-Boot](http://www.denx.de/wiki/U-Boot)
running first, very little is actually working. Most noticeably,
there is no usable UART or external RAM, and quite a lot of
initialization is necessary before they are both in a usable state.
The only available RAM is 128kB that is on the SOC itself.

The usual case is that on reset, the ROM boot code searches boot
devices to find the second-stage bootloader to be executed from the
128kB RAM. Its only task is to initialize RAM and other necessary
peripherals so that the next stage bootloader can be loaded and
executed.

Running without boot code affords us full control. The full system
state is known, which has as advantage that once it works for us,
it should work everywhere. The bootloader is eliminated as a
dependency in determining the system state once the RTEMS binary
starts running. The disadvantage is that we have to figure out how
to get the hardware into a usable state.
