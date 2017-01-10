#Here is my code.
# importing file.
from readability.readability import Document
import urllib2
# Get Users URL
URL= "http://arstechnica.com/science/2017/01/texas-slams-fda-with-lawsuit-for-holding-up-imported-execution-drugs/"
#req = urllib2.Request(URL)
# putting it in to object.
print ("url is - " + URL)
#URL = URL.strip('\'"')
#print ("new url is - " + URL)
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
htmlThing.write(strHtmlStuff.encode('utf8') + '\n')
htmlThing.close
print "The file name is: " + htmlName
# there u go with html file.
