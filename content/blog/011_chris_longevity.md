Title: Software Longevity - It's Neither Fire Nor Forget - Guest Post by Chris
Date: 2014-08-10 23:44
Category: Blog
Tags: rtems,software,embedded
Summary: Chris talks about long-term software maintenance.
Author: Chris

Software Longevity - It's Neither Fire Nor Forget - Guest Post by Chris
===============================================================

What's this about?
------------------

My friend Chris recently wrote about a rarely highlighted aspect
of software engineering - long term support. A real story from a
real experienced person about a fairly tough technical problem you
might not think about until it's too late is always worth listening
to. It made me stop and think so I want to share it with you.

What's going on
---------------

Chris is a highly specialized software consultant and as such works
for highly demanding clients, and much of the time his work is not
in the public eye. To software professionals that work in the public,
these demands may be unusual and so it is worth talking about.

The issue is of supporting systems software in the long term.  A
reliable build means reproducible - the build environment shouldn't
matter, the result must be the same to ensure the same behaviour
of the resulting system.

Therefore the software has to be built reliably, i.e. reproducibly,
in two dimensions

  *  Different OSes and distributions must be able to build the system with the same result
  *  Old OSes and distributions must be able to build the system with the same result

and everything needed to build it reliably, i.e., reproducibly.
Most significantly, this means also building the tools reliably
needed to build the system. 

So in a way, we want to support RTEMS in two dimensions - many OSes
and many versions of these OSes.

And all tools needed to produce an RTEMS system, i.e. the complete
toolchain. Have you ever compiled a 15-year-old GCC and verified
it produces the same output, byte by byte? Can you be sure you can
deliver and test a bugfix for such a system? That would be GCC 2.6.0
now. These are challenges that must be addressed in long-life-cycle
projects such as spaceflight projects.

What's the situation
--------------------

RTEMS provided Fedora packages via yum for years. For a large part
of this time there was no other distro supported, and this was not
great for RTEMS users. Attempts to get the packages upstream into
the distros fail, and for good reason. The dependencies are specific
to a niche and difficult to manage; i.e. newlib with the RTEMS
kernels.  The upstream distro people could not test what was being
produced, and it is not good for them to release something they
cannot test.

Over time the tools maintainer for RTEMS became a packaging expert
for Fedora and the RTEMS tools started to rot but it was expertly
packaged.

While this was happening I had to build my tools by myself
because FreeBSD and MacOS were not supported.

What's the Solution - The birth of the RTEMS Source Builder
-----------------------------------------------------------

This is where the RSB came from. I took it from my private hack to
something general and useful so we could start to clean up the
tools. The end result is something that builds tools for a wide
range of operating systems and distros. RTEMS could never be able
to provide enough hardware and bandwidth to do that at the binary
package level.

The Time Factor
--------------------------------------------------

There is another side to this, and to the RSB. RTEMS is used in
long life-cycle projects. I have code in flight today that is still
to be maintained that I suspect was written around the time or even
before many readers were born.

The only way this is maintained is due to being able to build
everything in flight from source, including the tools. The last bug
fix I did almost 14 years ago required a new version of Linux because
the archived kernel would not boot on the then-current hardware and
VMs were not option and IMO are still not.  A few simple patches,
and gcc built, and I byte verified the build, made the fix and
released the code. The final systems shipped in 2009 and should
operate for 20 years. The last version of the system this one
replaced did.

Building from source is very important and the RSB formalises this
for all users.

