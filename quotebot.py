import os
import random

import tweeter as Tweeter

# main entry, gets called by cron, chooses a 1/125 possbility for Tweeting
# this is based on cron starting at 6am (PST) - 9pm (PST), 15 hours total
# every 7 minutes is about 1 out of every 125 for an average of 1 tweet/day
def Activate():
	randChance = 1.0/125.
	dirList =  getDirectoryList()
	randChance = randChance * len(dirList)
	
	randomNum = random.random()

	# this outputs to cronlog, so we can tell if script is working, use randomNum to switch up output
	outStr = "Activate (quotebot.py)\n"
	outStr = outStr + "randomNum = " + str(randomNum) + "\n"
	outStr = outStr + "randomChance " + str(randChance) + "\n"

	# if we are in random range, choose a random quotebot and tweet it
	if randChance >= randomNum:
		twitterBot = dirList[random.randint(0, len(dirList)-1)] 
		tweetedMsg = tweetQuote(twitterBot)
		outStr = outStr + "SENDING TWEET via " + twitterBot + "\n"
		outStr = outStr + tweetedMsg
	else:
		outStr = outStr + "NO TWEET SENT"

	print outStr
# dirName = something like "marktwainbot", do not include the trailing '/'
def tweetQuote(dirName):
	dirName = dirName + '/'
	lastQuotesFilename = dirName + "lastquote.txt"
	quotes = loadQuotes(dirName + "quotes.txt")		# e.g. "marktwainbot/quotes.txt"

	arrIndex = findArrayIndex(quotes,getLastQuote(lastQuotesFilename))
	
	# if not found, set to beginning of file
	if arrIndex == -1:
		arrIndex = 0
	elif arrIndex == len(quotes)-1:
		arrIndex = 0
	else:
		arrIndex = arrIndex+1

	tweetQuote = quotes[arrIndex]
	Tweeter.tweetMessage(Tweeter.getKeys(dirName+"keys.txt"), tweetQuote)
	saveLastQuote(lastQuotesFilename, tweetQuote)
	return tweetQuote

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

# return a list of directories, not including hidden ones like git
def getDirectoryList():
	dirList = []

	for d in os.listdir(os.path.curdir):
		if os.path.isdir(d) and d[0] != '.':
			dirList.append(d)
	return dirList

if __name__ == "__main__":
	Activate()
		
