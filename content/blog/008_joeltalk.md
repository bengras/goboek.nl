Title: Video of talk about real-time, embedded, software in space, and SMP threads scheduling.
Date: 2014-05-17 22:45
Category: Blog
Tags: rtems
Summary: Dr Joel of RTEMS came to visit the VU University and gave a great talk on Embedded, Realtime, RTEMS and SMP. I made a video of it.

![Embedded device]({static}/images/embedded.jpg)

Embedded device.

Interested in embedded systems, real-time systems, or how the
software on satellites or on the Mars rover works, from someone
with many years of experience in this field? Joel has a talk just
for you.

[Joel](http://rtemsramblings.blogspot.com/) from
[RTEMS](http://www.rtems.org/) came to the VU University in Amsterdam
to give a talk. The audience was a big group of [computer systems
researchers](http://en.wikipedia.org/wiki/System_software) that
aren't necessarily experts in the field of embedded or realtime.

It turns out the audience was perfect for it because the talk is a
great introduction to embedded and realtime; and also goes in-depth
when it comes to the unique challenges in SMP scheduling in that
area.

## We recorded it

My friends at the office Lionel and Kees did audio and video recordings of
it. Joel gave me his slides. I transcribed the whole talk (i.e. subtitles)
to compensate for the audio being crummy in places. My friend Goran boosted
bits of the audio. And I edited it all together.

## Contents briefly

 * What is embedded?
 * What is real-time?
 * What is an operating system?
 * What is an embedded, real-time, operating system?
 * What is RTEMS? Where is it used?
 * RTEMS architecture
 * How are threads managed and scheduled in RTEMS?
 * What changes when we start doing all this in SMP
 * Audience questions

## My favourite part

Is Joel strutting his stuff in response to a question:

> Nobody said these were easy. 
> It's multithreaded, that's why we get the big bucks, right? 

Watch it to see it!

## Video

Here is the video. Enjoy!

<iframe class="youtube-player"
type="text/html"
width="640" height="385"
src="https://www.youtube.com/embed/7Jh9PUSBPAY" allowfullscreen frameborder="0" cc_load_policy="1">
</iframe>

## PS About The Subtitles

I transcribed all of the subtitles and used the YouTube interface
to automatically do the timing for me. This was hit/miss. The first
version matched the first 70% of the video perfectly, but always
seemed to lose sync completely near the end - same for when the
first 50% or all of the video transcription was complete. The next
version had different audio and the sync was one big mess.

So I used the first version, adjusted the timing for the new video
(the SRT file with timing info was available for download from
YouTube), and then was stuck with how to correct the timing for the
remaining 30 minutes or so. I call it 'stuck' because I found the
youtube interface for correcting these timings far too clumsy to
use in this manner. All I needed was displaying the subtitle, and
me correcting the timing by hitting a key every time I wanted a
transition to the next! Is that so hard? I would be done in the 30
minutes remaining of the video. It can't be done faster.
No of course it's not so hard, but
that doesn't mean existing tools have an obligation to anticipate
your use case, however easy it may be. I looked around but found no
subtitle tool, site or software that had implemented my scenario.

Unfortunately the shortest path from my problem to the solution I
imagined was using Perl. I wrote a script to read the SRT file up
until the timing was wrong, copying over the entries to the output
file directly. From then I made it display each subtitle,
and wait for a keystroke for each transition; and rewrite
the SRT to use the new timings. Somewhat to my surprise, in actual
operation, this went perfectly the first time, start to finish.
Except for falling asleep once or twice while watching the video
again, it was pretty late. I'm not especially proud of the script
but I am a bit proud of solving the problem in a completely optimal way in terms of
execution time, with
fairly low effort in terms of programming time.

