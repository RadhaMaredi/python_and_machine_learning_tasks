#find the factorial of the factorial

#fact fun does the factorial of each value in factorial and return it
def fact(num):
    return 1 if num == 0 else num * fact(num-1)

#subfact fun. does the multiplication of each factorial value and return it
def subfact(num):
    n = 1
    while num != 0:
        n = fact(num) * n
        num = num -1
    return n

num = int(input("Enter the number to know factorial: "))
print("The factorial of", num, "is: ", subfact(num))
