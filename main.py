from pyfiglet import Figlet
from code import ascii


ascii("ASCII IMAGE TEXT")
print("What word do you want to convert to ASCII IMAGE TEXT")
while True:
  word = input(f"\n:")

  print("")
  ascii(word)