scdr
====

Simple Commandline Definition Receiver is a small python program that fetches definitions of words from the command line.

Use
---

To use simply run `python dictionary.py WORD` in a terminal where word is the word you wish to have the definition of,, use `python dictionary --help` to find out how to use it from your command line.

Currently the options are:

`-h, --help` To see a help page.

`-f FILE, --file=FILE` To use a file with words (every new line) to find definitions of.

`-a, --noalternating` To keep the output sane, no alternating background colors.

`-b, --noformat` To have the output boring with no color or bolding, this is mainly useful for piping output. This removes all formatting.

`-o FILE, --output=FILE` To choose a location for a text file to output to. This will not have any colors or bolding since that is very messy (ANSI codes and everything)

Installation
------------

To install pull this project `git clone https://github.com/Math-ias/scdr.git` or however you like to do this, and edit the APIKEY file (create the APIKEY file in the directory if it doesn't exist). Change it to being your [dictionaryapi.com](http://www.dictionaryapi.com/) API key. This key should be for the Merriam Webster's School Dictionary with Audio, you can see it [here](http://www.dictionaryapi.com/products/api-school-dictionary.htm). This program however might work with the other products on [dictionaryapi.com](http://www.dictionaryapi.com/).

TODO
----

 - [ ] Better parsing (currently tags are stripped ungracefully)
 - [x] Supporting most words
 - [ ] Windows support? (Uses /usr/share/dict/words which Windows does not have)
