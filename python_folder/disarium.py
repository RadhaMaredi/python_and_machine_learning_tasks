#Create a function that determines whether a number is a Disarium or not?



def find_disarium(input_a, convert_list, length_of_list):

    """this fun. finds the disarium number or not 
    and return the results."""
    
    count = 0
    for i in range(length_of_list):
        count += int(convert_list[i]) ** (i+1)
    count = str(count)

    print ("Disarium Number") if count == input_a else  print ("Not a Disarium Number")

input_a = input("Enter a number: ")
convert_list = list(input_a)
length_of_list = len(convert_list)

#calling function
find_disarium(input_a, convert_list, length_of_list)