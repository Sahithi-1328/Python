# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.


def containsDuplicate(nums):
    return len(nums) != len(set(nums))


# Example usage
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(containsDuplicate(nums))

        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        #             break
        # return False

        #approach-2

        # return len(nums)!=len(set(nums))

        #approach-3

        # x=sorted(nums)
        # for i in range(len(x)-1):
        #     if x[i]==x[i+1]:
        #         return True
        # return False

        #approach-4
        
        # x=set()
        # for i in nums:
        #     if i not in x:
        #         x.add(i)
        #     else:
        #         return True
        # return False
