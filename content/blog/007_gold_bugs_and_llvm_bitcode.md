Title: LLVM Bitcode, Minix Liveupdate, and Gold Bugs
Date: 2014-05-04 22:45
Category: Blog
Tags: llvm,minix
Summary: A story about the powerful possibilities of building code using LLVM bitcode; and a binutils gold bug I came across and fixed.

![Lightning]({static}/images/lightning.jpg)

The power of LLVM. Image: Rainer Knäpper

Interested in adding a whole new dimension to existing everyday C code?
Or what it's like to be among the first of projects to be trying such
things with new tools and technologies, and having to fix a linker bug
to do it? Read on.

## Introduction to LLVM 

![LLVM Dragon]({static}/images/llvm-dragon-small.png)

[LLVM](http://www.llvm.org/) is a full compiler infrastructure made to not
only compile various languages to various kinds of machine code, but also work with
code in other ways using re-usable components. Examples: an editor
that understands your code as you type (an IDE); a library that
lets you perform source-level transformations easily that are very
messy to do reliably at the text level; [Clang](http://clang.llvm.org/)
is a C/C++ compiler built on LLVM that can generate machine code
for many architectures, including i386 and ARM;
[Klee](http://klee.github.io/klee/), which simulates many executions
of programs with unspecified inputs; and so on.

[More complete intro in PDF format here](http://www.llvm.org/pubs/2008-10-04-ACAT-LLVM-Intro.pdf).

## Introduction to LLVM Bitcode

At the core of how LLVM works is its Intermediate Representation,
or IR, or bitcode. It represents the logic of the program after
translation from the input language. So it describes the intended
action of the program independent of a particular target architecture.
Such bitcode files can be linked together to form the bitcode
representation of the final executable program.

## Powerful applications of LLVM Bitcode

This allows some powerful reasoning over complete programs at a higher
abstraction level than machine code. Example:

  * [Klee](http://klee.github.io/klee/) makes use of this. It is
    able to *symbolically execute* a program. It simulates
    running a program without knowing what inputs it will receive
    (I/O results, program arguments, etc.). Such unknowns are treated
    symbolically and Klee tries to find execution paths and input
    values that cause unwanted states (e.g. bad pointer dereference
    or an assertion failing). A nice demonstration of KLEE's reasoning powers
    is making it
    [solve a maze](http://feliam.wordpress.com/2010/10/07/the-symbolic-maze/).
  * For a demonstration combining another powerful form of abstraction with
    LLVM bitcode: based on his work with
    [RUMP kernels](http://wiki.netbsd.org/rumpkernel/),
    Antti Kantee was able to use
    [emscripten](https://github.com/kripken/emscripten/wiki) to translate his kernels to Javascript.
    The result is [the NetBSD kernel booting in javascript](https://blog.netbsd.org/tnf/entry/kernel_drivers_compiled_to_javascript).

Not only has analyzing programs become possible; also transforming them
before the machine code is generated. This has powerful applications.
Examples:

  * All kinds of code instrumentation.
  * Link-time optimisation. Optimisation is generally done at compile
    time, so on a per-file basis; but the compiler is actually quite limited
    in what it can do and what information it has available at this scope.
    Examples: leaving out dead code; inlining functions that are defined
    in a different file; having a better estimate of how many times 
    functions are called. These are all things that are impossible at the
    file level but possible at link time. Needless to say, the possibilities to improve
    on time- and space-optimisation this way are near-endless.
  * Introspection. This makes available information about functions and
    variables of the current (or another!) C program in the form of regular
    C datastructures, allowing operations at runtime that are otherwise
    impossible.

## Minix and Liveupdate

[Minix](http://www.minix3.org/) is close to supporting being built
with bitcode completely. The code is ready on a working branch,
just not merged with mainline yet. This allows for many powerful
features such as LTO, introspection, running KLEE etc. to be applied
to its codebase - userland and OS components alike.

The driving force behind building Minix with bitcode is the Liveupdate
project spearheaded by [Cristiano Giuffrida](http://www.cs.vu.nl/~giuffrida/).
His Ph.D thesis topic is the implementation of the updating of OS components
to newer versions while they are in use. It uses information obtained from
LLVM bitcode to make this possible. More details are in his Liveupdate papers here on
his [homepage](http://www.cs.vu.nl/~giuffrida/).

## Minix is unique

Minix is unique in more ways than one. However, having this available
as a maintained feature in the codebase means Minix is in a position
to offer a powerful extra level of code analysis and instrumentation;
for applications known (such as LTO) and to be invented.  It is the
first and so far only operating system that supports full bitcode
builds in the base system!

The future holds more promise - LLVM-based instrumentation supports
more projects in Minix that Cristiano is working on - memory
checkpointing for crash recovery, address space layout randomization,
and fault injection.

## Gold bugs

![Gold bug]({static}/images/goldbug.jpg)

To link bitcode files and perform transformations on them at link
time, the [Binutils Gold linker](http://en.wikipedia.org/wiki/Gold_%28linker%29)
is required. Unfortunately we at Minix ran into a few problems and bugs when linking
everything with Gold.

The most recent one [I recently fixed and submitted a fix upstream
for](https://sourceware.org/bugzilla/show_bug.cgi?id=16900). It was
quite a trip down the rabbit hole to find that one from just the
symptoms of a crashing runtime linker! I really like being able to
contribute such a fix to a project upstream that we make heavy use of -
it's a way to give back and raise the profile of Minix a little.

Also the fact that we ran into these problems suggests that Minix is
unusual, perhaps unique, in supporting bitcode builds in its own codebase.
And therefore is a uniquely enticing platform to do OS-level LLVM transform
experimentation on.

## Now what?

[More LLVM-bsed projects here](http://llvm.org/ProjectsWithLLVM/).

## Acknowledgements

My thanks to [Cristiano Giuffrida](http://www.cs.vu.nl/~giuffrida/) who
kindly reviewed a draft of this post and substantially improved upon it.
Any errors are still mine of course.
