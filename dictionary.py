import xml.etree.ElementTree as ET # Hey! ET!
from optparse import OptionParser
import urllib
import urllib2
import re
import colorama
import spellingCorrector as corrector
import sys
try:
	with open("APIKEY", 'r') as apikeyfile:
		key = apikeyfile.read().replace('\n', '')
except IOError as e:
	print "Your APIKEY file does not exist! Please input your apikey for the merriam webster student dictionary below:"
	key = input()
	with open("APIKEY", 'w') as apikeyfile:
		apikeyfile.write(key)

def parseWord(word):
	try:
		req = urllib2.Request("http://www.dictionaryapi.com/api/v1/references/sd4/xml/%s?key=%s" % (word, key))
		merriamXML = urllib2.urlopen(req)
	except URLError as urlerror:
		print "There was an error in the URL. (%s)" % urlerror.reason	
		return {"Could not retrieve definition due to an error."}

	try:
		tree = ET.parse(merriamXML)	
		root = tree.getroot()
		defs = tree.findall(".//dt")
	except ParseError as pe: # NOTE: Due to bad documentation I could not find much about ParseError and if it's even thrown, it's in the source code of etree so I can check for it, but at this time it is unknown whether or not this is needed.
		print "There was an error when parsing the files from merriam webster."
	
	# Merriam throws these disgusting extra tags in there. :(
	# So we got to clean it up.	
	
	definitions = [re.sub(r'<[^>]*?>', '', ET.tostring(definition)) for definition in defs] # Error handling here?	
	# Shortened version of for def in defs: definitions.append(re.blahblahblah, stuff)

	return definitions

if __name__ == "__main__":	

	stdout = sys.stdout 

	colorama.init(autoreset=True)

	optionParser = OptionParser()
	optionParser.add_option("-f", "--file", action="store", help="Take words from a specified file.", metavar="FILE")
	optionParser.add_option("-a", "--noalternating", dest="alternating", action="store_false", help="Keep the output sane, no alternating background colors.")
	optionParser.add_option("-b", "--noformat", dest="color", action="store_false", default = True, help="Remove all formatting from the text, useful for piping.")
	optionParser.add_option("-o", "--output", dest="output", action="store", help="Output all the definitions to a chosen file, the boring option is also set to true.", metavar="FILE")
	(options, args) = optionParser.parse_args()
	options.alternating = True
	words = {}

	if options.output is not None:
		sys.stdout = open(options.output, 'w') # Ugly hack to redirect output of the program! Eww!
		options.color = False
		options.alternating = False

	if options.file is not None:
		try:
			with open(options.file, 'r') as wordFile:
				words = [line.rstrip() for line in wordFile.readlines()]
		except IOError as e:
			print "Unable to read from the given wordfile! Check that it exists and/or that there is permissions enough to access it."
	else:
		words = args

	words = [corrector.correct(word) for word in words]

	for word in words:
		cleanedDefinitions = parseWord(word)
		if options.color == True:
			print colorama.Fore.RED + colorama.Style.BRIGHT + word.upper()
		else:
			print word.upper()
		for num,definition in enumerate(cleanedDefinitions):
			if num % 2 == 0 and options.alternating == True and options.color == True:
				definition = colorama.Back.GREEN + definition
			print ("%d -> %s " % (num+1, definition))
	
	sys.stdout = stdout
