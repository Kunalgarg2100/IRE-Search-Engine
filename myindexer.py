import xml.sax
import pdb
cnt = 0;
class WikiXMLHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.isPage = False
      self.isTitle = False
      self.isText = False
      self.isPageId = False
      self.title = ""
      self.text = ""
      self.pageId = -1
      self.pageCnt = 0

   # Call when an element starts
   def startElement(self, tag, attributes):
      if tag == "page":
         self.isPage = True
         self.pageCnt += 1
      elif tag == "title":
         self.isTitle = True
      elif tag == "text":
         self.isText = True
      elif tag == "id":
         self.isPageId = True

   # Call when an elements ends
   def endElement(self, tag):
      if tag == "page":
         self.isPage = False
         self.title = ""
         self.text = ""
         self.pageId = -1
      elif tag == "title":
         self.isTitle = False
      elif tag == "text":
         self.isText = False
      elif tag == "id":
         self.isPageId = False

   # Call when a character is read
   def characters(self, content):
      if self.isTitle:
         self.title = content
         print("Title:", self.title)

      elif self.isText:
         self.text = self.text + content + " "
         print("Text:", self.text)

      elif self.isPageId and self.pageId == -1:
         self.pageId = content
         print("PageId:", self.pageId)

  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()

   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = WikiXMLHandler()
   
   parser.setContentHandler( Handler )
   parser.parse("wiki.xml")