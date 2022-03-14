
print("Please see codeBreaker.txt before starting for more info")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(plainText, encrpytKey):
    encryptText = ""
    for character in plainText:
        if character.isalpha():
            character = character.lower()
            charIndex = alphabet.index(character)
            newIndex = (charIndex + encrpytKey) % 26
            cipherChar = alphabet[newIndex].upper()
        else:
            cipherChar = character
        
        encryptText += cipherChar

    print("Your cipher text is " + encryptText)

plainText = input("Enter a message to be encrypted: ")

while True:
    try:
        encryptKey = int(input("Now enter how many characters in the alphabet you would like to shift: "))
    except ValueError:
        print("Please enter a whole number")
    else:
        break

encrypt(plainText, encryptKey)

def decrypt(decryptText, decryptKey):
    alphaText = ""
    for character in decryptText:
        if character.isalpha():
            character = character.lower()
            charIndex = alphabet.index(character)
            newIndex = (charIndex - decryptKey) % 26
            alphaChar = alphabet[newIndex]
        else:
            alphaChar = character

        alphaText += alphaChar

    print("Your plaintext is: " + alphaText)

decryptText = input("Please input a message to be decrypted: ")

while True:
    try:
        decryptKey = int(input("Now enter how many characters in the alphabet you would like to shift back: "))
    except ValueError:
        print("Please enter a whole number")
    else:
        break

decrypt(decryptText, decryptKey)

print("Now here's a challenge, try to decrypt the message below: ")

import string 
import random

chalMsg = ("".join(random.choices(string.ascii_lowercase, k = 5)))

chalShift = (random.randint(1, 5))

encrypt(chalMsg, chalShift)

print("The shift key is " + str(chalShift))

while True:
    userAns = input("Answer: ")
    if userAns.lower() != chalMsg:
        print("Unlucky! Try Again")
    else:
        print("Well done! You got it!")
        break








