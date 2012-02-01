#Here is my code.
# importing file.
from decruft import Document
import urllib2
# Get Users URL
URL=raw_input("ENTER THE URL: ") 
# putting it in to object.
fURL = urllib2.urlopen(URL)
#Making Html file 
htmlName="decrufted.html"
htmlThing = open(htmlName,'w')
#htmlThing.write(Document(fURL.read()).summary())
#first i printed on this shall
# and than i thought that i could store that in to veriable. and i stored in to string veriable.
#print Document(fURL.read()).summary()
#making srting object.
strHtmlStuff = Document(fURL.read()).summary()
#Writing stuff from string object.
htmlThing.write(strHtmlStuff)
htmlThing.close
print "The file name is: " + htmlName
# there u go with html file.
