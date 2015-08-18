#!/usr/bin/python

import xml.sax
import re
import urllib


class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.key = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
     

   # Call when an elements ends
   def endElement(self, tag):
      pass


       
      

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "Key":
         if (re.match('.*(pdf)$',content)):
            self.key = content
            print "http://files2.syncfusion.com/"+self.key

   
def download(file):
      with open(file) as fp:
         for line in fp:
            name = line.split("/")[5]
            print len(name), name
            name = name.rstrip('\n')
            print len(line), line
            testfile = urllib.URLopener()
            testfile.retrieve(line,name)

      
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   #parser.parse("Ebooks.xml")
   download("ebook.txt")


#ab = "aaa"
#b = re.match('aaa',ab)
#if(b):
#   print "true"

