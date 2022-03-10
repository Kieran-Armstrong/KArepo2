
from hashlib import new


def charReplace(string): 
    string = string.lower()     
    newString = string.replace("i", "1")
    newString = newString.replace("e", "3")
    newString = newString.replace("a", "4")
    
    
    print(newString)

string = input("Enter text")

charReplace(string)

