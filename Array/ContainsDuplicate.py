#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Questions
    #? To clarify, we are writing a function that takes an array of integers and returns a boolean value based on if the array contains duplicate values or not?
    #? Do we have to worry about array size or take memory into consideration?
    #? For edge cases, can we assume the input will always be an array of integers, and that the array is 1 dimensional?
    #? Can I code this in Python?

#Considerations
    #Brute Force Method: Nested loop that compares each value to every other value #! O(n^2)
    #Best Time Complexity: Use a hashmap to track previous array values, and check for duplicates in time #! O(n)

#! Time Complexity of O(n)
def containsDuplicate(nums):
    trackDuplicates = {}

    for num in nums:
        if num in trackDuplicates:
            return True
        else:
            trackDuplicates[num] = True
    return False


nums = [2,3,1,1]
print(containsDuplicate(nums)) #True

nums1 = [1,2,3,4]
print(containsDuplicate(nums1)) #False

nums2 = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums2)) #True

nums4 = []
print(containsDuplicate(nums4)) #False