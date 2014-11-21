import tweeter as Tweeter


# dirName = something like "marktwainbot", do not include the trailing '/'
def tweetQuote(dirName):
	dirName = dirName + '/'
	lastQuotesFilename = dirName + "lastquote.txt"
	quotes = loadQuotes(dirName + "quotes.txt")		# e.g. "marktwainbot/quotes.txt"

	arrIndex = findArrayIndex(getLastQuote(dirName+lastQuotesFilename))
	
	# if not found, set to beginning of file
	if arrIndex == -1:
		arrIndex = 0

	tweetQuote = quotes[arrIndex]
	print "Tweeting: " + tweetQuote
	#Tweeter.tweetMessage(getKeys(dirName+"keys.txt"), tweetQuote)
	saveLastQuote(dirName+lastQuotesFilename), tweetQuote)

# this filename will typically be something like "marktwainbot/quotes.txt"
def loadQuotes(filename):
	f = open( filename, "r" )
	quotes = []
	for line in f:
    	quotes.append( line.rstrip('\n') )
	f.close()
	return quotes

# return the last quote that we tweeted out
def getLastQuote(filename):
	f = open(filename, "r")
	lastquote = f.read()
	f.close
	return lastquote.rstrip('\n')

# we save the last quote to a filename, so we can move sequentially to the next one
def saveLastQuote(filename, tweetStr):
	f = open(filename, "w")
	f.write(tweetStr)
	f.close()

# utility function: return index of item in array, -1 if none found
def findArrayIndex(arr, sStr):
	for i in range(len(arr)):
		if(arr[i] == sStr):
			return i
	return -1

if __name__ == "__main__":
	tweetQuote("marktwainbot")