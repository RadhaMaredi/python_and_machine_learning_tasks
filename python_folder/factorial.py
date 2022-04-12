#Q.find the factorial of the factorial 


def factorial_num(num):

    """this factorial_num takes input as the factorial of each 
    value in factorial and return the value"""
    
    #here i used ternary operator. if num equal to zero it returns 1 
    #else it perform the recursive by callin it self.
    return 1 if num == 0 else num * factorial_num(num-1)

def sub_factorial(num):

    """subfact fun. takes the number as input and does 
    the multiplication of each factorial value and return it"""
    
    #declare a variable with value 1. because our value should not 
    # have zero to perform factoial.
    n = 1 
    while num != 0:
        #here we are calling the factorial_nm function to perform factorial
        n = factorial_num(num) * n
        num = num -1
    return n

#takes input from the user
num = int(input("Enter the number to know factorial: "))

#print the output and calling the sub_factorial function
print("The factorial of", num, "is: ", sub_factorial(num))
