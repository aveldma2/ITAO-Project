import re
txt = "Whatever the question is ?"
x = re.search("[?]$", txt)

if x:
  print("YES! we end in a ?")
else:
  print("Nope no ?")

#if we ever wanted to use regex for the question mark