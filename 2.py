def string_alternative(sentence):
    newSentence = sentence[::2]
    return newSentence


userSentence = input("Please enter a sentence")
print(string_alternative(userSentence))
