from modules.datemodule import greets
from modules.mathmodule import exponent, hypothenuse
from modules.utils import print_sep, play_with_lists, play_with_array, play_with_dictionaries
from modules.ioutils import writeinFile, viewfile
from modules.classmanipulator import play_with_classes

greets()

a = 5
b = 2

print(f"{a} exponent {b} equals {exponent(a, b)}")
print(f"hypothenuse [{a}, {b}] is {hypothenuse(a, b)}")

print_sep()

a = 3
b = 3
exponent(a, b)
print(f"{a} exponent {b} equals {exponent(a, b)}")

print_sep()

play_with_array()

print_sep()

play_with_lists()

print_sep()

play_with_dictionaries()

print_sep()

writeinFile("gap.txt")

viewfile("gap.txt")

play_with_classes()