import xml.etree.ElementTree as ET # Hey! ET!
from optparse import OptionParser
import urllib
import urllib2
import re
import colorama
import spellingCorrector as corrector

with open("APIKEY", "r") as apikeyfile:
	key = apikeyfile.read().replace('\n', '')

def parseWord(word):
	req = urllib2.Request("http://www.dictionaryapi.com/api/v1/references/sd4/xml/%s?key=%s" % (word, key))
	merriamXML = urllib2.urlopen(req)	

	tree = ET.parse(merriamXML)	
	root = tree.getroot()
	defs = tree.findall(".//dt")
	
	# Merriam throws these disgusting extra tags in there. :(
	# So we got to clean it up.	
	
	definitions = [re.sub(r'<[^>]*?>', '', ET.tostring(definition)) for definition in defs]	
	# Shortened version of for def in defs: definitions.append(re.blahblahblah, stuff)

	return definitions

if __name__ == "__main__":	

	colorama.init(autoreset=True)

	optionParser = OptionParser()
	optionParser.add_option("-f", "--file", action="store", help="Take words from a specified file.", metavar="FILE")
	optionParser.add_option("-a", "--alternating", dest="alternating", action="store_true", default = True, help="Alternate the background colors for the definitions to make them more distinguishable.")
	optionParser.add_option("-s", "--sane", dest="alternating", action="store_false", help="Keep the output sane, no alternating background colors.")
	(options, args) = optionParser.parse_args()
	words = {}

	if options.file is not None:
		wordFile = open(options.file)
		words = [line.rstrip() for line in wordFile.readlines()]	
		wordFile.close()
	else:
		words = args

	words = [corrector.correct(word) for word in words]

	for word in words:
		cleanedDefinitions = parseWord(word)
		print colorama.Fore.RED + colorama.Style.BRIGHT + word.upper()
		for num,definition in enumerate(cleanedDefinitions):
			definition = colorama.Back.GREEN + definition if num % 2 == 0 and options.alternating else definition
			print "%d -> %s " % (num+1, definition)
			
