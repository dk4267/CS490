str1 = input('Please enter a string') #get user input
str2 = str1[:len(str1) - 2] #delete the last 2 characters from the string
print(str2[::-1]) #print resulting string, reversed

num1 = int(input('Please enter a number')) #input 2 numbers
num2 = int(input('Please enter another number'))

#print sum, difference, product, and quotient of the 2 numbers
print('The sum of ', num1, ' and ', num2, ' is ', num1 + num2)
print('The difference of ', num1, ' and ', num2, ' is ', num1 - num2)
print('The product of ', num1, ' and ', num2, ' is ', num1 * num2)
print('The quotient of ', num1, ' and ', num2, ' is ', num1 / num2)