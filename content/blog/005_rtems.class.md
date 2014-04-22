Title: Back to school - RTEMS Class
Date: 2014-04-22 13:31
Category: Blog
Tags: beagle,rtems
Summary: I followed a class on the RTEMS OS and wrote a BSP for the Beagles for it in about that time.

[As mentioned](|filename|002_rtems.md), I am interested in
diversifying my OS knowledge further.
[Joel](http://rtemsramblings.blogspot.nl/) mentioned he was
teaching an [RTEMS](http://www.rtems.org) [Open Class](http://www.rtems.org)
in Munich so that was a perfect opportunity to take part in.

It was a great experience. For many reasons!

Reasons the class was great, one: I learned a lot about RTEMS
-------------------------------------------------------------
Both usage and its internal structure, and real-time systems in general.
I had done some preparation beforehand so that I would get the most out of
the class, but both were something of a first for me.

![Joel teaching]({filename}/images/joel-teach.jpg)

Pictured above: Joel in front of the projection screen.

Two: I got to socialize with Joel
---------------------------------
He lives in the US so we don't see each other much. It was great to
catch up a bit and talk about subjects ranging from technical RTEMS
subjects, to life and happiness and such things in general.

![Having a beer with Joel]({filename}/images/socialize.jpg)

We all know socializing is simply fancier-sounding code for drinking
beer together, no?

Three: the Beagle BSP
---------------------
Based on Joel's suggestion beforehand I had set myself the goal of
writing a [BSP](http://www.rtems.org/wiki/index.php/Board_Support_Packages)
for the [Beagle](http://www.beagleboard.org) family of products for
RTEMS. In other words, a port of RTEMS to the beagles; specifically
the BeagleBoard XM, BeagleBone 'White,' and the BeagleBone Black.
Joel mentioned this at the start of the 4-day class to the other
participants, so that raised the pressure to succeed within the class
timeframe significantly!

I hacked on it as much as I could between classes and socializing and
"on the last day" I got it working.

![Joel demonstrating RTEMS on my beaglebone black]({filename}/images/demo.jpg)

Where to go
-----------

[The Beagleboard XM RTEMS Wiki page](http://www.rtems.org/wiki/index.php/Beagleboard) contains something of a history of the RTEMS Beagleboard port. 

[Claas Ziemke](https://github.com/claas) started an RTEMS BSP for
the original Beagleboard for a GSOC project, so he wrote the basis
for that page. 

[Chris](https://github.com/kiwichris) started the wonderfully-named section 
"Ben and Chris's Big Beagleboard Adventure" - I couldn't have phrased it
better, that's really what it feels like!

The work-in-progress code is at
[my github RTEMS fork](https://github.com/bengras/rtems/tree/beaglebone-wip).

What next
---------

I'm really delighted with how far the BSP has come, as it's a first
for me to do something with RTEMS, and indeed get any new OS working
almost-from-scratch on a new piece of hardware. I have spent a lot
of time since then running the full test suite, cleaning it up
(mostly: minimizing), and working with
[Chris](https://github.com/kiwichris) to get the RTEMS executable
booting from scratch using JTAG. But that is a topic of another,
similarly exciting, post.

