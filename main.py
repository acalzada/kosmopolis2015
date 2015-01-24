from convertirEnText import convertirEnText;
from countWords import countWords;

webExemple1 = 'http://www.voidspace.org.uk'
webExemple2 = 'http://www.lavanguardia.com'
webExemple3 = 'http://www.google.com/search?q=Artur+Mas'

url = webExemple1



text = convertirEnText(url);

count = countWords(text);

for k,v in count:
	print v," -> ",k
