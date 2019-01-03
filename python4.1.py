import sys

phrase = str(sys.argv[1])
def isPalindrom(phrase):
	phrase = phrase.lower()
	"""This function returns `true` if passing string is palindrom, 
	otherwise returns `false`"""
	excep = (' ', ',', '.', '!', '?', ':', ';', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9') # exceptions signs
	 # this cycle excepts some useless signs from phrase
	for symb in excep: 
		phrase = phrase.replace(symb,'')
	# next cycle of code returns `false` if phrase isn`t palindrom

	if int(len(phrase)) == 1:
		return True
	else:
		for item in range(int(len(phrase)/2)):
			if phrase[item] != phrase[len(phrase) - 1 - item]:
				return False
	return True	
if isPalindrom(phrase) : print "YES"
else: print "NO"