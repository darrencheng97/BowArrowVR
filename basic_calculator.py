num1 = input("Please enter number 1: ")
num2 = input("Please enter number 2: ")

method = input("Please enter a method to calculate: 1. Add 2. Subtract 3. Multiply 4. Divide. Enter the method in number.")

if (method == "1") :
    print(float(num1) + float(num2))
elif (method == "2") :
    print(float(num1) - float(num2))
elif (method == "3") :
    print(float(num1) * float(num2))
elif (method == "4") :
    print(float(num1) / float(num2))

