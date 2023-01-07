# an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

#Questions
    #Confirm there is always eactly one solution and the array is always full of integers
    #Do we have to worry about input times in terms of memory

#Considerations
    #Brute Force: Nest loop to compare each number until a valid sum is found //O(n^2)
    #Most Efficient: Use a hashmap to store each passed value, and see if the difference of the target and current index value is in the map

def twoNumberSum(list, target): 
    differenceMap = {}

    for num in range(len(list)):
        current = list[num]
        difference = target - current
    
        if difference in differenceMap:
            return [num, differenceMap[difference]]
        else:
            differenceMap[current] = num

list1 = [3, 5, -4, 8, 11, 1, -1, 6]
target1 = 10

list2 = [4, 6, 1]
target2 = 5

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target3 = 17

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
target4 = 43

print(twoNumberSum(list1, target1)) #[6, 4]
print(twoNumberSum(list2, target2)) #[0, 2]
print(twoNumberSum(list3, target3)) #[8, 7]