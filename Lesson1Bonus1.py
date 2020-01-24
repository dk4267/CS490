
#armstrong number test

origNum = int(input('Please enter an integer'))
calcNum = origNum #for extracting the individual digits from the number
resultNum = 0
digPlace = 1 #ones place, tens place, etc.

while calcNum != 0:
    digit = (calcNum % (digPlace * 10)) / digPlace #get the digit
    calcNum -= (digit * digPlace)
    digitCubed = digit ** 3
    resultNum += digitCubed
    digPlace *= 10

if origNum == resultNum:
    print(origNum, ' is an Armstrong number!')
else:
    print(origNum, ' is not an Armstrong number!')
