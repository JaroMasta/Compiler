from sys import stdin

from compiler_modules.Scanner import *
from compiler_modules.Colouring import *

skaner = Scanner()
kolorowanie = Colouring()

"""for line in stdin:
  line = clean_spaces(line)
  p = 0
  while p < len(line):
    kwp = scanner(line, p) # k - klucz, w- wartość, p - indeks początku skanowania linii
    print("   ", kwp[0], kwp[1])
    p = kwp[2]"""


with open("example_input.txt", "r") as filehandler:
  example_input = filehandler.read()
  #print(repr(example_input))


# nie z stdin tylko z zdefiniowanego stringa
line = skaner.clean_spaces(example_input)
p = 0
while p < len(line):
  kwp = skaner.scanner(line, p) #k - klucz w- wartość
  print("   ", kwp[0], kwp[1])
  p : int = kwp[2]


# do pliku html
arr = []
line : str = skaner.clean_spaces(example_input)
p = 0
while p < len(line):
  kwp : list = skaner.scanner(line, p) #k - klucz w- wartość
  if kwp[0][:5] != "ERROR":
    arr.append([kwp[0], kwp[1]])
  else:
    arr.append(["ERROR", kwp[1]])
  kolorowanie.generate_html(arr)
  p : int = kwp[2]