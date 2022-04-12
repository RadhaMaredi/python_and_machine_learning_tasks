#importing the arithmatic file 
from arithmatic import *

#taking a variable is true. to run while loop and stop the while loop
x = True 
while x:
      #taking the two numbers from the user
      num1 = int(input("Enter First Number: "))
      num2 = int(input("Enter Second Number: "))
      print("Enter which operation would you like to perform?")
      operators = ['+' , '-' , '*' , '/']  #store all operations in a variable
      #takes which kind of operation user would like to perform
      operation = input("Enter any of these character for specific operation +,-,*,/: ")

      #if user enter invalid operation(which are i declared in "operators" variable) 
      # then this while loop print the error.
      while operation not in operators:            
            operation=input("Enter a valid operator:  ")
      
      ##if user enter valid operation(which are i declared in "operators" variable) 
      # then this if block executed.
      if operation in operators :

            #if the operation is addition this block perform 
            # the operation and print the output
            if operation == "+":
                  result = add(num1, num2)
                  print(str(num1) + str(operation) + str(num2) + " = " + str(result))
            
            #if the operation is subtraction this block perform 
            # the operation and print the output
            elif operation == "-":
                  result = sub(num1, num2)
                  print(str(num1) + str(operation) + str(num2) + " = " + str(result))
            
            #if the operation is multiplication this block perform 
            # the operation and print the output
            elif operation == "*":
                  result = mul(num1, num2)
                  print(str(num1) + str(operation) + str(num2) + " = " + str(result))
            
            #if the operation is division this block perform 
            # the operation and print the output
            elif operation == "/":
                  result = div(num1, num2)
                  print(str(num1) + str(operation) + str(num2) + " = " + str(result))

      #here taking user further move if he wants to do another operation go forward
      #by pressing the "Enter" else enter the "stop" to stop the operations
      a = input()

      #if user enter "stop" terminate from the while loop
      if a == "stop":
            x = False
