"""
usage: [dictionary] = countWords(file)

This script counts the words in the input file and returns a dictionary 
with the word count for each word found in the file.

"""

name = raw_input("Enter file:")
if len(name) < 1 : name = "textFile.txt"

handle = open(name)

wordDict = dict();
for line in handle:
	words = line.split();
	for word in words:
		wordDict[word] = wordDict.get(word,0)+1;

#sortedDict = sorted(wordDict,key=itemgetter(1));
#for data in sortedDict:
#	print data

word_view = [ (v,k) for k,v in wordDict.iteritems() ]
word_view.sort(reverse=True) # natively sort tuples by first element
#for v,k in word_view:
#	    print "%s: %d" % (k,v)
print word_view
