
#I accidentally made this much more difficult than it had to be
inputString = input('Please enter a string') #get input
outputString = '' #string to add chars for output
index = 0 #keeps track of where we are in the string
isPython = False #keeps track of whether we're in the middle of the word 'python'

for char in inputString: #loop through input string by character

    if inputString[index:index + 6] == 'python': #only enter if we encounter the word 'python'
        outputString += 'pythons' #output 'pythons' instead of just the character
        isPython = True #indicates that we're in the middle of the word 'python'
    else:
        if isPython: #if in a letter in 'python'
            if char == 'n': #set isPython to false if at the end of the word
                isPython = False
        else: #if not inside the word 'python', just add the character to output, don't add char if in 'python'
            outputString += char
    index += 1 #incrememt index at the end of each iteration
print(outputString)

#here's the easy way...
outputString2 = inputString.replace('python', 'pythons')
print(outputString2)