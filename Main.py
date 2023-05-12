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
    d = int(input("input second number: "))
    add(a, b)