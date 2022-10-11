# Write a function that takes in a non-empty list of distinct integers and an integer representing a target sum.  If any two numbers in the input list sum up to the target sum, the function should return them in an list, in any order. If no two numbers sum up to the target sum, the function should return an empty list. 

def twoNumberSum(list, target): #takes in array and target integer
    map = {} # map to keep track of numbers in list for maximum time efficiency

    for num in list: # iterate through list
        dif = target - num #variable dif keeps track of number we are checking for

        if dif in map: #if dif is in our hashmap
            return [dif, num] #we've found a pair whose sum is target
        else: #otherwise
            map[num] = True #add current number to the map and start the loop over

    return [] #if no pairs found return an empty list

list1 = [3, 5, -4, 8, 11, 1, -1, 6]
target1 = 10

list2 = [4, 6, 1]
target2 = 5

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target3 = 17

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
target4 = 43

print(twoNumberSum(list1, target1)) #[-1, 11]
print(twoNumberSum(list2, target2)) #[4, 1]
print(twoNumberSum(list3, target3)) #[8, 9]
print(twoNumberSum(list4, target4)) #[]