def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mult(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

print("A. Addition")
print("B. Substraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

choice = input("input your choice: ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    add(a, b)

if choice == "b" or choice == "B":
    print("Substraction")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    sub(a, b)

if choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    mult(a, b)