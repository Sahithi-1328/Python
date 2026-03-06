# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
        # 1
        # for i in range(len(nums)-1):
        #     if nums[i]+nums[i+1]==target:
        #         return i,i+1
        #         break
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # 2
        dict={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in dict:
                return [dict[x],i]
                break
            dict[nums[i]]=i
        # 3
        # for i,num in enumerate(nums):
        #     if target-num in dict:
        #         return [dict[target-num],i]
        #     dict[num]=i
print(twoSum([2,7,11,15],9))
