import urllib2
from bs4 import BeautifulSoup
from lxml import html

webExemple1 = 'http://www.voidspace.org.uk'
webExemple2 = 'http://www.lavanguardia.com'
webExemple3 = 'http://www.google.com/search?q=Artur+Mas'

url = webExemple2
#import pdb;pdb.set_trace()
peticio = urllib2.Request(url)
resposta = urllib2.urlopen(peticio)
##html = resposta.read()
##text = html2text.html2text(html)
##print text

soup = BeautifulSoup(resposta)
[s.extract() for s in soup('script')]
[s.extract() for s in soup('style')]
#htmlBonic = soup.prettify()
text = soup.body.text

print(text)
