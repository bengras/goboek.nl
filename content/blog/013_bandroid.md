Title: BAndroid: How Google killed two-factor authentication
Date: 2015-09-23 1:00
Category: Blog
Tags: android,security
Summary: A Android vulnerability called BAnderoid is found and described. This work was done by members of the VU University security research group.

Explain Like I'm 5
===================
Do you know those banks that use text messages on your phone to double-check who you are when you want to do an transaction on their website with your account? It's extra safe, because people can't steal your phone. Wrong, it's not safe. If you're using an Android phone. It's bad. This post explains how and why.

We do this so we can pressure Google into removing the feature from Android that makes this possible.

Is that all you wanted to know? Ok. How about a FAQ?
[Here is the FAQ](http://www.few.vu.nl/~vvdveen/bandroid.html)

How about a video of a talk describing the problem in ful detail?

<iframe class="youtube-player"
type="text/html"
width="640" height="385"
src="http://www.youtube.com/embed/7WiE0cpsxv4" allowfullscreen frameborder="0" cc_load_policy="1">
</iframe>

What?
====
This post explains an interesting digital security development: the weakening of two-factor authentication using SMS in Android phones. I want to give more exposure to this bug in order to pressure Google to remove the feature that makes this vulnerability possible.

Attackers can bypass SMS-based two-factor authentication on Android once the browser is hacked. They can do this by intercepting the SMS as it comes in, and then forwarding it to the attacker. The user never notices. There are big financial institutions that depend on this being secure. 

The Research Group
==================

At the VU University where I work, I am part of a computer systems security research group led by [Herbert Bos](http://www.cs.vu.nl/~herbertb). In 2014, one of the researchers, Victor van der Veen, discovered an interesting Android vulnerability that allows an attacker, with only a little manipulating of the user, to bypass two-factor authentication using SMS.

Background: Two-Factor Authentication
=========================
In the digital security world, there is a lot to do about authentication - proving who you are. That's good, because otherwise someone else could use systems as if they were you (such as: transfer your money away). We often talk about 3 factors that can be supplied to a system to prove your identity:

  1. something you know (such as: a password, or your mother's maiden name)
  1. something you have (such as: a metal key, or your phone)
  1. something you are (such as: your fingerprint, or the pattern on your iris)

Many systems are content with just asking your login name and password. But passwords aren't really that great - if someone guesses it or steals it, it can be used to impersonate you. There's no warning that this has happened. And because everything is networked, the opportunities for people to steal your passwords are all over the place.

If only a password is required, we call this one-factor authentication. If we require something else as well, we call this two-factor authentication. Such as: a password and a digital card. Or, a password and your phone. You can prove you have your own phone by typing in a SMS code that is sent to you. Someone who steals your password can't do this, because he hasn't stolen your phone and that's not easy to do over the internet.

Because this raises the bar to forge someone's identity enormously, the more sensitive systems such as banks or the Dutch national Digital ID system [DigiD](https://www.digid.nl/) require two factor authentication. Fortunately!

The Attack
==========
Victor has devised a way that eliminates this factor. The scenario is as follows: somebody hacks into your browser. This is possible with many of the past, present and future security bugs in browsers. This is precisely the scenario that two-factor authentication is designed to thwart. What happens next?

  * The malicious code is able to forcibly install an app with any permissions on your Android phone remotely using your Google account. It can use your Google account because the browser can. You won't even notice the app is there.
  * The app then has to be activated. This can be done by some very light manipulation, also without the user noticing. E.g., let the user click on a attacker-crafted url, in any context whatsoever, in the phone.
  * From that point on, the app can silently intercept SMS messages. So the malicious code in the browser can trigger a bank login, the bank will send an SMS code to the phone, the app will transmit it to the attacking code.

Presto. You can log in without stealing someone's phone.

For full details, see the FAQ and video above.

The Result
==========
Someone who breaks into your browser doesn't need to steal your phone over the internet any more
in order to log in as you.

The Google
==========
Officially, Google has largely brushed off this concern. (See more details in the FAQ.) They claim it
works as designed. We want this changed.

The Press
=========
The [Dutch national press](http://www.volkskrant.nl/tech/lek-op-android-telefoons-door-beveiliging-google~a4089416/) [was interested](http://www.nu.nl/mobiel/4076742/onderzoekers-vu-ontdekken-lek-in-android-telefoons.html), but we want more attention for this vulnerability in order to increase the pressure on Google.

The FAQ
=======

For further information, please see more description and answers to common question [in the FAQ](http://www.few.vu.nl/~vvdveen/bandroid.html) maintained by Victor.
