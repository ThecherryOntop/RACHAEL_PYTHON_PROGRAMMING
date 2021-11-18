#!/usr/bin/env python3

# Define two string values with starting and ending space
username = " admin"
password = " hello123 "

# Compare the strings without removing space
print("Output without strip method:")

if(username == "admin" and password == "hello123"):
  print("Authenticated user\n")
else:
  print("Not Authenticated user\n")

# Compare the strings by removing space
print("Output with strip method:")

if(username.strip() == "admin" and password.strip() == "hello123"):
  print("Authenticated user")
else:
  print("Not Authenticated user")

