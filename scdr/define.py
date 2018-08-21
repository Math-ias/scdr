import lxml.etree as etree
import re


class CollectorParser(object):
    def __init__(self):
        self.definition = ""
        self.definitions = []

    def start(self, tag, attrib):
        if tag == "sx":
            self.definition += "\nSynonym: "
        elif tag == "dt":
            self.definition = ""
        elif tag == "un":
            self.definition += "\nUsage: "
        elif tag == "vi":
            self.definition += "\nExample: "

    def end(self, tag):
            if tag == "dt":
                # Makes the first letter uppercase.
                reformattedDefinition = self.definition[:1].upper() + self.definition[1:]
                # Strip newlines without text (for when a definition is just a synonym)
                reformattedDefinition = reformattedDefinition.lstrip()
                self.definitions.append(reformattedDefinition)

    def data(self, data):
        self.definition += re.sub(':', '', data)

    def close(self):
        return self.definitions


def define(word, key):
    if type(key) is not str:
        raise ValueError("key '{0}' must be a string", key)

    if type(word) is not str:
        raise ValueError("word '{0}' must be a string", word)

    try:
        parser = etree.XMLParser(target=CollectorParser())
        definitions = etree.parse("http://www.dictionaryapi.com/" +
                                  "api/v1/references/sd4/xml/{0}?key={1}".format(word, key), parser)
    except etree.ParseError as pe:
        raise Exception("Parsing error, probably due to invalid API key")

    return definitions
