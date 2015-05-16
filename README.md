SCDR
====

Simple Commandline Definition Receiver is a small python program that fetches definitions of words from the command line.

Use
---

To use simply run `define WORD` in a terminal where `WORD` is the word you wish to have the definition of, use `define --help` to find out how to use it from your command line.

Currently the options are:

`-h, --help` To see a help page.

`-f FILE, --file=FILE` To use a file with words (every new line) to find definitions of.

`-a, --noalternating` To keep the output sane, no alternating background colors.

`-b, --noformat` To have the output boring with no color or bolding, this is mainly useful for piping output. This removes all formatting.

`-o FILE, --output=FILE` To choose a location for a text file to output to. This will not have any colors or bolding since that is very messy (ANSI codes and everything)

Installation
------------

SCDR utilizes [Merriam Webster Incorporated's School Dictionary with Audio API](http://www.dictionaryapi.com/products/api-school-dictionary.htm), you can obtain an apikey for this at [dictionaryapi.com](http://www.dictionaryapi.com), this apikey is needed for the functioning of SCDR.

To install SCDR pull this project `git clone https://github.com/Math-ias/scdr.git` or however you wish to do so, and run `python setup.py install` within the directory. This will install all the needed packages and install the python package.

Merriam-Webster-Inc
-------------------

Licensing requires me to put Merriam-Webster's Inc.'s logo here, so woopdeedoo!
![Merriam-Webster Inc.](merriam-webster-logo.png)

TODO
----

 - [x] Better parsing (currently tags are stripped ungracefully)
 - [x] Supporting most words
 - [x] Windows support? (Uses /usr/share/dict/words which Windows does not have)
