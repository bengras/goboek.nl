Title: Exciting RTEMS GSOC projects for beagle announced
Date: 2015-06-03 23:50
Category: Blog
Tags: rtems,gsoc
Summary: A new RTEMS project - GSOC 2015!

Google Summer of Code 2015 has started. RTEMS is a participating
organisation, and the set of accepted proposals was just announced
some time ago. And it's a big deal. Not in the least for the RTEMS
Beagle support!

Google Summer of Code Projects
==============================

Google Summer of Code is a Google-sponsored program intended to get
people into the world of open source. Google pays a stipend to let
a student work on an open source project in the summer holidays.
The project is with an open source organisation ('org' in GSOC
parlance). The student then needn't take a summer job but learns
about how contributing to open source works instead.

Participating in the community, proposing ideas and designs and
working with the community to implement them and merge them with
the project is all part of the experience. This is done under the
guidance of a org-appointed mentor. The mentor knows the org and
the project well enough to guide the students through this process.
Hopefully, the students will stay and continue to contribute to the
project after GSOC is over.

Coding has started
==================

As the GSOC 2015 Timeline shows, coding has started. At RTEMS we
have weekly IRC meetings with students & mentors at which students
present their progress, sticking points, and plans for the next
week.

I am mentoring
==============

I am co-mentoring 3 projects. And I'm very excited about their
potential. A full table of projects is in the tracking table on the
RTEMS GSOC page.

Beagleboard.org is generously donating
======================================

Jason Kridner of Beagleboard.org has contacted us and stated that
Beagleboard.org will donate a Beaglebone Black to students working
on Beaglebone projects for GSOC, even for non-Beagleboard org GSOC
projects. He has shipped all 3 students working on the RTEMS Beagle
BSP a Beaglebone Black. Fantastic initiative! We're grateful to
Beagleboard for this contribution and I hope it will benefit the
students greatly, in their GSOC project and afterwards.

Beagle peripheral improvement by Ketul Shah
===========================================

Ketul is going to be improving peripheral support for the Beagle
BSP. He already has a lot of GPIO functionality working and we are
working on making a nice clean GPIO API that is sufficiently general
to be a BSP-independent API for GPIO for RTEMS. We intend to align
it with the Raspberry Pi GPIO API as well, i.e. make it actually
generic for those two BSPs already. That would be quite an advanced
contribution for a GSOC project in itself!  Beagle peripheral
improvement by Ragunath

Ragunath's first priority is going to be getting an Ethernet driver
working for the Beaglebones. He will be using the FreeBSD code and
RTEMS' libbsd to build it. He already has it building and interfacing
to the hardware to a great extent, very impressive rate of progress!
Ethernet functionality will really help the BSP grow up tremendously.

BSD-licensed bootloader by Jarielle Catbagan
============================================

Jarielle is working on a BSD (or similarly liberal) licensed
bootloader for the Beagle BSP. Currently booting an RTEMS image for
the Beagles relies on uboot which is GPL-licensed. Unfortunately
the GPL is a big problem for many users and clients of RTEMS and
RTEMS prefers to provide a full set of software that will get you
from poweron to running RTEMS without a license that is something
of a liability. Jarielle is already very far with building & running
Micromonitor on the Beaglebone so that is very encouraging. We're
lucky to have Ed Sutter, author of umon, to co-mentor this project.

Uboot is part of the reason some Beagle changes (in the rtems tools
and rtems source builder repositories) aren't fully merged yet with
mainline. A significant side-effect of this project is hopefully
to provide a full boot without uboot and merge the result with rtems
tools and rtems source builder.

Big changes
===========

All of these projects together will bring about a big improvement
to the Beagle BSP on RTEMS. The Beagle BSP has attracted quite some
attention to RTEMS which is great. Making it more fully featured
and within just a few months is just fantastic. I'm thrilled to be
a part of it.
