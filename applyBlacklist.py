"""
usage: [dictOut] = applyBlacklist(dictIn,blacklist_file)

This function reads the words in clacklist_file and sets the counter to 0 in the dictionary.
"""

def applyBlacklist(dictIn,blacklist_file): 
	fileHandler = open(blacklist_file);

	for word in fileHandler:
		word = word.rstrip('\n');
		word = word.rstrip('\r');
		if word in dictIn:
			dictIn[word]=0;

	return dictIn;
