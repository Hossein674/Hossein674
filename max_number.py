def max_n(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = input("Enter num 1: ")
num2 = input("Enter num 2: ")
num3 = input("Enter num 3: ")

print("max number is = " + str(max_n(num1, num2, num3)))

