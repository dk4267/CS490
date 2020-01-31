inFile = open('userFile.txt', 'r')
fileLine = inFile.readline()
wordDict = {}

while fileLine != "":
    words = fileLine.split()
    for word in words:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    fileLine = inFile.readline()

for item in wordDict.keys():
    print(item, ': ', wordDict[item])
