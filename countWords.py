"""
usage: [dictionary] = countWords(dictInit,file)

This script counts the words in the input file and returns a dictionary 
with the word count for each word found in the file.

"""
import string;
def countWords(dictInit,text):

	wordDict = dict();
	
	wordDict = dictInit;
	
	words = text.split();
	for word in words:
		word = word.lower();
		exclude = set(string.punctuation)
		word = ''.join(ch for ch in word if ch not in exclude)
		wordDict[word] = wordDict.get(word,0)+1;

	return wordDict; 
