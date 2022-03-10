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
    else:
        print("Invalid Input")
    
a = int(input("Please enter number "))

b = int(input("Please enter number "))

op = input("Please enter operation you would like to carry out ")

calculator(a, b, op)

print(output)


