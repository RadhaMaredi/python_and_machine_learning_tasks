# Q.Create a function that returns the majority vote in a list.
#A majority vote is an element that occurs > N/2 times in a list
#  (where N is the length of the list).
#Example:
#majority_vote(["A", "A", "B"]) ➞ "A" majority_vote(["A", "A", "A", "B", "C", "A"]) 
# ➞ "A" majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

def finding_majority(input_a):
   
    """this fun. finds the majority of an element occurs n//2 times and 
    print the output """
    
    #find the unique elements using the set and it 
    # converted into list and stored in a variable
    unique_ele = list(set(input_a)) 

    #here the loop iterate over the unique elements and if block finds the majority.
    result = [i for i in unique_ele if input_a.count(i) > (len(input_a) // 2)]

    #print the results
    if len(result) == 0:
        print("NONE")  
    else:
        print("Majority vote is:",result)

#take the input from the user
input_a = input().split()
#calling the function by passing input as argument
finding_majority(input_a) 