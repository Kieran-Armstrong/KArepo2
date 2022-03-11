print("Please see codeBreaker.txt before starting for more info")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(plainText, secretKey):
    cipherText = ""
    for character in plainText:
        if character.isalpha():
            character.lower()
            charIndex = alphabet.index(character)
            newIndex = (charIndex + secretKey) % 26
            cipherChar = alphabet[newIndex].upper()
        else:
            cipherChar = character
        
        cipherText += cipherChar

    print("Your cipher text is " + cipherText)

plainText = input("Enter a message to be encrypted: ")

while True:
    try:
        secretKey = int(input("Now enter how many characters in the alphabet you would like to shift: "))
    except ValueError:
        print("Please enter a whole number")
    else:
        break

encrypt(plainText, secretKey)