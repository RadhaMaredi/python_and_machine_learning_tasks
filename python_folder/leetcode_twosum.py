class Solution:
    def twoSum(self, nums, target):
        """twoSum method takes list and target as input and perform 
        the below operation and returns a list which contain indexes """

        index_list = []
        for i in range(len(nums)-1):     
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    index_list.append(i,j)  
        return index_list

#class object
obj = Solution()

#declaring the inputs
list_1 = list(map(int, input().split(",")))
target = int(input())

#calling the twoSum method
output = obj.twoSum(list_1, target)
print(output)

                
        