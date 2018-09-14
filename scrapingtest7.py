from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum=0
    for word,value in wordList.items():
        sum+=value
    return sum

def retrieveRandomWord(wordList):
    randIndex=randint(1,wordListSum(wordList))
    for word,value in wordList.items():
        randIndex-=value
        if randIndex<=0:
            return word

def buildWordDict(text):
    text=text.replace("\n"," ")
    text=text.replace("\"","")

    punctuation=[',','.',';',':']
    for symbol in punctuation:
        text=text.replace(symbol," "+symbol+" ")

    words=text.split(" ")
    words=[word for word in words if word != ""]

    wordDict={}
    for i in range(1,len(words)):
        if words[i-1] not in wordDict:
            wordDict[words[i-1]]={}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]]=0
        wordDict[words[i - 1]][words[i]]=wordDict[words[i-1]][words[i]]+1

    return wordDict

text=str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
wordDict=buildWordDict(text)

length=100
chain=""
currentWord="I"
for i in range(0,length):
    chain+=currentWord+" "
    currentWord=retrieveRandomWord(wordDict[currentWord])

print(chain)

