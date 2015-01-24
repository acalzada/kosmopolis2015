import urllib2
from bs4 import BeautifulSoup
from lxml import html

def convertirEnText(url) :
	peticio = urllib2.Request(url)
	resposta = urllib2.urlopen(peticio)

	soup = BeautifulSoup(resposta)
	[s.extract() for s in soup('script')]
	[s.extract() for s in soup('style')]
	text = soup.body.text

	return text;
