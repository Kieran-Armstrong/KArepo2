from multiprocessing.sharedctypes import Value


def calculator(a, b, op):
    global output 

    output = 0 
    
    if op == "+":
        output = (a + b)
    elif op == "-":
        output = (a - b)
    elif op == "*":
        output = (a * b)
    elif op == "/":
        output = (a / b) 

while True:
    try:
        a = int(input("Please enter number (1) "))

        b = int(input("Please enter number (2) "))
    except ValueError:
        print("Please enter a whole number - start again")
    else:
        break


op = input("Please enter operation you would like to carry out ")

calculator(a, b, op)

print(output)


