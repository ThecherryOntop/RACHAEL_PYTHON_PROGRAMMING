#!/usr/bin/python3
#Use strip() to remove the particular character
# Take a string data as input
string1 = input("Enter a string\n")
# Take a character data as input
char1 = input("Enter a character to remove from the string\n")

# Remove the character from both side of the string data
newString = string1.strip(char1)

# print the original string
print("The original string is :\n%s" %string1)
# Print the string after stripping
print("The output after removing '%c' from the string is:\n%s" %(char1, newString))