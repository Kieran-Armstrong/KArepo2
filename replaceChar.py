
from hashlib import new


def charReplace(string):      
    newString = string.replace("i", "1") 
    newString = newString.replace("I", "1")
    newString = newString.replace("e", "3")
    newString = newString.replace("E", "3")
    newString = newString.replace("a", "4")
    newString = newString.replace("A", "4")
    
    
    print(newString)

string = input("Enter text")

charReplace(string)

