#palindrome test

string1 = input('Please enter a string')
string2 = string1[::-1] #reverse string
if string1 == string2:
    print(string1, " is a palindrome!")
else:
    print(string1, " is not a palindrome!")
