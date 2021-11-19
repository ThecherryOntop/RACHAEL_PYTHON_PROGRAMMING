#!/usr/bin/env python3

# sUsing a string to remove multiple characters
# Define an infinite loop
while(True):
  # Take an url address as input
  url = input("Enter a URL address\n")
  # Take a string data as input
  charList = input("Enter the characters to remove\n")
  '''Remove the character from both side of the string data
     where matches'''
  newString = url.strip(charList)

  # print the original string
  print("The original string is :\n%s" %url)
  # Print the string after stripping
  print("The output after removing the characters\n%s" %newString)

  # ask user to continue the script or not
  answer= input("Do you want to quit(y/n)?")
  # Terminate the loop if the answer is 'y' or 'Y'
  if (answer == 'y' or answer == 'Y'):
    break