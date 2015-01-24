from convertirEnText import convertirEnText;
from countWords import countWords;
from applyBlacklist import applyBlacklist

blacklist_file = "stop-words/stop-words-en.txt" ;
webExemple1 = 'http://www.voidspace.org.uk'
webExemple2 = 'http://www.lavanguardia.com'
webExemple3 = 'http://www.google.com/search?q=Artur+Mas'

url = webExemple1



text = convertirEnText(url);
text = text.encode('latin1');

count = countWords(text);

wordCount = [ (v,k) for k,v in count.iteritems() ]
wordCount.sort(reverse=True) # natively sort tuples by first element
print "\n===========   Total   ============\n\n"
print wordCount;

countNew = applyBlacklist(count,blacklist_file);


wordCountNew = [ (v,k) for k,v in countNew.iteritems() ]
wordCountNew.sort(reverse=True) # natively sort tuples by first element
print "\n===========   Prunned   ============\n\n"
print wordCountNew

