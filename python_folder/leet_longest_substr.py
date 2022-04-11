#Given a string s, find the length of the longest substring
#  without repeating characters?

class Solution:

    def lengthOfLongestSubstring(self, str):
        """it takes the string as an input, finds the longest substring and
        return the number of longest sub strings"""

        sub = {}
        current_substing_start = 0
        current_len = 0
        longest = 0
        
        for i, letter in enumerate(str):
            if (letter in sub) and (sub[letter] >= current_substing_start):
                current_substing_start = sub[letter] + 1
                current_len = i - sub[letter]
                sub[letter] = i
                
            else:
                sub[letter] = i
                current_len += 1
                if current_len > longest:
                    longest = current_len
        return longest

obj = Solution()
my_string = input()
result = obj.lengthOfLongestSubstring(my_string)
print(result)
                