
from hashlib import new


def charReplace(string): 
    string = string.lower()     
    newString = string.replace("i", "1")
    newString = newString.replace("e", "3")
    newString = newString.replace("a", "4")
    newString = newString.replace("s", "5")
    newString = newString.replace("b", "6")
    newString = newString.replace("t", "7")
    newString = newString.replace("o", "0")
    
    
    print(newString)

string = input("Enter text ")

charReplace(string)

