scdr
====

Simple Commandline Definition Receiver is a small python program that fetches definitions of words from the command line.

Use
---

To use simply run `python dictionary.py WORD` in a terminal, use `python dictionary --help` to find out about all the options.

Installation
------------

To install pull this project `git clone https://github.com/Math-ias/scdr.git` or however you like to do this, and edit the APIKEY file. Change it to being your [dictionaryapi.com](http://www.dictionaryapi.com/) API key. This key should be for the Merriam Webster's School Dictionary with Audio, you can see it [here](http://www.dictionaryapi.com/products/api-school-dictionary.htm). This program however might work with the other products on [dictionaryapi.com](http://www.dictionaryapi.com/).

TODO
----

 - [ ] Better parsing (currently tags are stripped ungracefully)
 - [x] Supporting most words
 - [ ] Windows support? (Uses /usr/share/dict/words which Windows does not have)
