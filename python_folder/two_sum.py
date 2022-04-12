#Q. Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.
#You can return the answer in any order.
#eg: Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:

    def two_sum(self, nums, target):

        """twoSum method takes list and target as input and perform 
        the below operation and returns a list which contain indexes """

        index_list = [] #create empty list to store the indexes
        for i in range(len(nums)-1):  #iterate over the length of the of nums -1   
            for j in range(i+1, len(nums)): #inner loop iterate over the i to len of nums
                #if sum of elements equal to target then those indexes stored in a list
                if nums[i] + nums[j] == target:
                    index_list.append(i,j)  
        return index_list

#class object
obj = Solution()

#taking the inputs
list_1 = list(map(int, input().split(",")))
target = int(input())

#calling the two_sum method
output = obj.two_sum(list_1, target)

#print the result
print(output)

                
        