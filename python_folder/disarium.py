#Create a function that determines whether a number is a Disarium or not?

def find_disarium(input_a, convert_list, length_of_list):

    """this fun. finds the disarium number or not 
    and return the results."""

    count = 0  # Initialize sum of terms
    for i in range(length_of_list):
        #Calculates the sum of digits powered with their respective position 
        count += int(convert_list[i]) ** (i+1)
    count = str(count)

    #Checks whether the sum is equal to the number itself   
    if count == input_a:
        print ("Disarium Number")
    else:
        print ("Not a Disarium Number")

#declaring inputs
input_a = input("Enter a number: ")
convert_list = list(input_a)
length_of_list = len(convert_list)

#calling function
find_disarium(input_a, convert_list, length_of_list)