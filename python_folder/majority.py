#Create a function that returns the majority vote in a list.
#A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
#Example
#majority_vote(["A", "A", "B"]) ➞ "A" majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A" majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None


#this fun. finds the majority of an element occurs n//2 times and print the output 
def majority(input_a):
    unique_ele = list(set(input_a))
    result = [i for i in unique_ele if input_a.count(i) > (len(input_a) // 2)]

    #printing the results
    print("NONE") if len(result) == 0 else print("Majority vote is:",result)

input_a = input().split()
#Calling the function
majority(input_a)