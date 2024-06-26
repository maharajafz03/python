
from array import *

name = ["maga", 'raja', "kanagi", "yamuna"]

iT = "kunthani"

for i in range(0,len(name)):
    if name[i] == iT:
        print(i)
        break
else:
    print("invalid name")
