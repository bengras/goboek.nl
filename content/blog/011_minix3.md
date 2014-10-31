Title: Minix 3.3.0 is released, is unforking, and is visiting EuroBSDcon 2014
Date: 2014-09-24 23:50
Category: Blog
Tags: minix,bsd
Summary: Some background on the Minix 3.3.0 release and the Minix delegation to EuroBSDcon 2014 in Sofia.

Minix 3.3.0 and building up to that
===================================

A little over a week ago, Minix 3.3.0 [was
announced](http://www.minix3.org/330.html).  It is the culmination
of a lot of hard work over the past 1.5 year or so.

Notable is that in that period we took the tough decision to break
the userland ABI. This is a big no-no in OS circles of course.
Nevertheless it was decided the tradeoff was positive. We could make
a lot of changes to make the userland more like NetBSD without
worrying about compatability - often the source of a lot of work
and complexity. We broke a lot of things in once so the pain is
felt just once. As a result many things are cleaner and more like
NetBSD now, and more future-proof; things like bigger C types (off_t,
time_t, and several others) and a bigger IPC message (64 bytes instead
of 36 bytes).

There are many more improvements in 3.3.0, such as the first good
multi-architecture release - x86 and ARM. All in all a huge leap from
where we were 1.5 years ago and I'm proud of it.

Something supernatural happened - we are unforking from NetBSD
==============================================================

Something very unusual happened in this Minix release. It was another
huge leap in adopting the NetBSD code and infrastructure. The imported
code is so clean w.r.t. NetBSD now that we have adopted the NetBSD
hierarchy completely with the exception of a top-level minix/ directory.
So in a way, we are *merging* with NetBSD. The *opposite* of forking.
So we are challenging not only the common movement in open source,
which is to fork, but also the second law of thermodynamics. Admittedly
we are putting in a lot of energy to make this happen, but still. We
are *unforking*.

Not only in source but also in real life: EuroBSDcon 2014
=========================================================

Not only are we meeting in source, we are also 
meeting in real life at EuroBSDcon 2014. AST is
[giving a talk](http://2014.eurobsdcon.org/talks-and-schedule/talks/#AndrewTanenbaum) with technical updates on our journey in BSD land. Myself and Lionel
are there. In fact I am typing this while about to board my flight to Sofia.

I'm looking forward greatly to the conference, attending talks and meeting
BSD folks. See you all there!
