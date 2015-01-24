"""
usage: [dictionary] = countWords(file)

This script counts the words in the input file and returns a dictionary 
with the word count for each word found in the file.

"""
def countWords(text):

	wordDict = dict();
	#for line in text:
	#	words = line.split();
	words = text.split();
	for word in words:
		wordDict[word] = wordDict.get(word,0)+1;

	wordCount = [ (v,k) for k,v in wordDict.iteritems() ]
	wordCount.sort(reverse=True) # natively sort tuples by first element
	return wordCount
