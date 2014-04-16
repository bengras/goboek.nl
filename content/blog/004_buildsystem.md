Title: MINIX builds on 22 Linux distro's thanks to NetBSD's buildsystem
Date: 2014-04-15 14:19
Category: Blog
Tags: minix,justworks
Summary: I tried the Minix build procedure in many environments with relatively minimal effort using OpenSuse's build farm. Minix builds from scratch on many different OSes and Linux distributions. This is a testament to the power of its buildsystem, taken from NetBSD.

Software that always works is pretty hard to achieve. It depends
on its own state and the state of its environment. Its own state
is hard enough to manage as it is. That of the environment, however,
is outside of its control alltogether. Whenever I use something that is
highly dependent on its environment, and it works without fiddling,
I'm always surprised and impressed and pleased. It's such a nice
experience.  Example: [my SONOS players](http://www.sonos.com/).
Phones nowadays (I use Androids) do a really good job of it too.
Apple also seems to invest a lot into the 'just works' experience
and it's impressive how often it does, in fact, just work.

I've come to appreciate both the value of things that just work,
and the cost of getting things to just work, a lot, because I'm on
both sides of the fence. I co-provide a product that should work;
and I'm a consumer of many products that should work.  It's easy
to underestimate how much more complex something has to be if it
has to work for everyone, in any environment, compared to just for you. 
You got it working in your environment, after all.
I'd like it if MINIX never had any build problems.  (Let's not talk
about run problems for now - that's much harder to measure.) But
we're a pretty small team so can't go down the [long
tail](http://en.wikipedia.org/wiki/Long_tail) of reasons why builds
might break in many different environments.

MINIX can be cross-built for x86 or ARM and so relies on its host
environment to a degree. This can't be controlled, so to have a
robust build system that not only works but also doesn't break
easily is pretty hard. 

Fortunately we consciously decided to re-invent the wheel as little
as possible and so went with [NetBSD](http://www.netbsd.org/)'s
build system. Their approach shows they recognize the same problem
and they solved it very neatly. All dependencies - from small
utilities like stat to a crossbuilding compiler and linker - can
be packaged along with the NetBSD source and built as `tools' before
NetBSD itself is. The build process then uses the tools and no host
commands. So the dependencies on the host environment are minimized.
This is crucial; just a simple utility like stat not taking exactly
the expected option and produce exactly the expected output could easily
break the whole build - often a hard-to-diagnose problem given the
on-the-surface symptoms.

I should add that, powerful as the system is, it is not magical.
When used properly, the system provides reproducibility of builds
independent of the host environment.  This doesn't mean there are
no problems. It means the state is manageable and only minimally
dependent on the host environment.  In the best case, all problems
are solved just once. Once it is solved by the first person, someone
else shouldn't bump into it again. Even if the hosting environments
are different. Given how diverse such environments can be, that
does make it *quite magical* as far as I'm concerned.

The buildsystem has worked really well for Minix as well. Just to
see how well it does on many different Linux distro's, I tried
crosscompiling x86 Minix on the [OpenSUSE's Build
Service](https://build.opensuse.org/).  It did take some tweaking,
mostly of package parameters like dependencies to get the tools
bootstrap going, but then 22 distro's built Minix without changing
the build system itself; [here are the
results](https://build.opensuse.org/package/show/home:beng-nl/Minix3). Well
done NetBSD, and the MINIX guys that work hard to cleanly integrate
it.
