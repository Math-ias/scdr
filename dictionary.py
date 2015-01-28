from lxml import etree as lxml
import argparse
import re
import colorama
import spellingCorrector as corrector
import sys

try:
	input = raw_input
except NameError:
	pass # Just a very rough attempt at python2 & 3 compatability

try:
	with open("APIKEY", 'r') as apikeyfile:
		key = apikeyfile.read().replace('\n', '')
except IOError as e:
	key = input("Your APIKEY file does not exist! Please input your apikey for the merriam webster student dictionary:")
	with open("APIKEY", 'w') as apikeyfile:
		apikeyfile.write(key)

def parseWord(word):
	try:
		tree = lxml.parse("http://www.dictionaryapi.com/api/v1/references/sd4/xml/{0}?key={1}".format(word, key))
		defs = tree.findall(".//dt")
	except lxml.ParseError as pe:
		print("There was an error when parsing the files from merriam webster.")
		return {"Could not recieve definitions due to an error involving parsing."}
	
	# Strip text of unparsed tags.

	definitions = [defin.text for defin in defs]	

	return definitions

if __name__ == "__main__":	

	stdout = sys.stdout 

	colorama.init(autoreset=True)

	argParser = argparse.ArgumentParser(description="A python program to fetch English definitions from the command line.")
	argParser.add_argument("-f", "--file", action="store", help="Take words from a specified file.", metavar="FILE")
	argParser.add_argument("--noalternating", dest="alternating", action="store_false", default=True, help="Keep the output sane, no alternating background colors.")
	argParser.add_argument("-n","--noformat", dest="color", action="store_false", default = True, help="Remove all formatting from the text, useful for piping.")
	argParser.add_argument("-o","--output", dest="output", action="store", help="Output all the definitions to a chosen file, the boring option is also set to true.", metavar="FILE")
	argParser.add_argument("words", nargs="+")
	
	args = argParser.parse_args()
	
	words = {}

	if args.output is not None:
		sys.stdout = open(args.output, 'w') # Ugly hack to redirect output of the program! Eww!
		args.color = False
		args.alternating = False

	if args.file is not None:
		try:
			with open(args.file, 'r') as wordFile:
				words = [line.rstrip() for line in wordFile.readlines()]
		except IOError as e:
			print("Unable to read from the given wordfile! Check that it exists and/or that there is permissions enough to access it.")
	else:
		words = args.words

	words = [corrector.correct(word) for word in words]

	for word in words:
		cleanedDefinitions = parseWord(word)
		if args.color == True:
			print(colorama.Fore.RED + colorama.Style.BRIGHT + word.upper())
		else:
			print(word.upper())
		for num,definition in enumerate(cleanedDefinitions):
			if num % 2 == 0 and args.alternating == True and args.color == True:
				definition = colorama.Back.GREEN + definition
			print ("{0} -> {1}".format(num+1, definition))
	
	sys.stdout = stdout
