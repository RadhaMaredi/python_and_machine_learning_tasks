#Given a string s, find the length of the longest substring
#  without repeating characters?

class Solution:

    def lengthOfLongestSubstring(self, str):
        """it takes the string as an input, finds the longest substring and
        return the number of longest sub strings"""
        
        #creating an empty dictionary to store 
        #the each character how many time  repeation.
        sub = {} 
        current_substing_start = 0
        current_len = 0
        longest = 0
        
        for i, letter in enumerate(str):
            #this loop iterate over the string and 
            # also it gives the count because we used enumerate.

            if (letter in sub) and (sub[letter] >= current_substing_start):
                #this block gives us no. of times a char. repeated in string and stored in dictionary 
                #as key:value format, here key means character and value is count of the character 
                current_substing_start = sub[letter] + 1
                current_len = i - sub[letter]
                sub[letter] = i
                
            else:
                sub[letter] = i
                current_len += 1
                #this if block give the longest substring
                if current_len > longest:
                    longest = current_len
        return longest

obj = Solution()    #creating the object
my_string = input() #taking input

#calling the method by passing my_string as argument
result = obj.lengthOfLongestSubstring(my_string)
print(result)  #print the result
                