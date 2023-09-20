# Print " in the string Hello World
# print("Hello \" World")
# print("This is Darren\'s book")

phrase = "Hello Mr.Darren"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.lower().islower())

# Find the character position in the string
print(phrase[0])
# Return the position index of the character in a string
print("Give me the position index of D: "+phrase.index('D'))

# Replace one of the character in the string
print("REPLACE FUNC: "+phrase.replace('H','h'))