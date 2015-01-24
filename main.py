from convertirEnText import convertirEnText;
from countWords import countWords;
from applyBlacklist import applyBlacklist
from search import getgooglelinks


blacklist_file = "stop-words/stop-words-es.txt" ;
numberOfSitesForDictionary = 3;
numberOfKeywords = 30;


query = raw_input('Enter your search keywords: ');

query.replace(" ","+");

#links = getgooglelinks('python','http://www.stackoverflow.com/')
links = getgooglelinks(query)

topLinks = list();

for link in links:
	if link not in topLinks:
		topLinks.append(link);

count = dict();
for url in topLinks[0:numberOfSitesForDictionary]:
	
	text = convertirEnText(url);
	#text.encode('utf-8',errors='replace')
	#text.encode('ascii',errors='ignore')
	count = countWords(count,text);



wordCount = [ (v,k) for k,v in count.iteritems() ]
wordCount.sort(reverse=True) # natively sort tuples by first element
#print "\n===========   Total   ============\n\n"
#print wordCount;

countNew = applyBlacklist(count,blacklist_file);


wordCountNew = [ (v,k) for k,v in countNew.iteritems() ]
wordCountNew.sort(reverse=True) # natively sort tuples by first element
#print "\n===========   Prunned   ============\n\n"
#print wordCountNew


for k,v in wordCountNew[0:numberOfKeywords]:
	print k," -> ",v
