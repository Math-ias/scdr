SCDR
====
Simple Commandline Definition Receiver is a small python program that
fetches definitions of words from the command line.

Use
---
To use simply run `define WORD` in a terminal where `WORD` is the word
you wish to have the definition of, use `define --help` to find out how to use
it from your command line.

Currently the options are:

 * `-h, --help` To see a help page.

 * `-f FILE, --file=FILE` To use a file with words (every new line) to find
definitions of.

 * `-a, --noalternating` To keep the output sane, no alternating background
 colors.

 * `-b, --noformat` To have the output boring with no color or bolding, this is
   mainly useful for piping output. This removes all formatting.

 * `-o FILE, --output=FILE` To choose a location for a text file to output to.
   This will not have any colors or bolding since that is very messy (ANSI codes and
   everything)

 * `-p NUMBER, --processes=NUMBER` To choose a number of worker processes used
   to download and parse definitions. The default is set to 4 processes. The
   program becomes faster with large lists of words when more processes are
   used because definition fetching is mostly net-bound.

 * `-s --spellingcorrect` To enable spell correction provided by the
   [autocorrect python package by phatpiglet](https://github.com/phatpiglet/autocorrect).

Installation
------------
SCDR utilizes [Merriam Webster Incorporated's School
Dictionary with Audio
API](http://www.dictionaryapi.com/products/api-school-dictionary.htm), you can
obtain a key for this at [dictionaryapi.com](http://www.dictionaryapi.com), this
key is needed for the functioning of SCDR.

To install SCDR you can use either the:

 * [Bitbucket repository](https://bitbucket.org/mathias_kools/scdr), by running
   `pip install git+https://bitbucket.org/mathias_kools/scdr`
 * [GitHub repository](https://github.com/Math-ias/scdr.git), by running `pip
   install git+https://github.com/Math-ias/scdr`

Both of the commands listed will install SCDR for you! Hooray :smile:. Both of
the repositories are up to date so it doesn't matter which one you are using.

Contributing
------------
Hold on, give me a few minutes and I will be back with
you about how to contribute ...

Merriam-Webster-Inc
-------------------
Licensing requires me to put
Merriam-Webster's Inc.'s logo here, so woopdeedoo!

![Merriam-Webster Inc.](merriam-webster-logo.png)
