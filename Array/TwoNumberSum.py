# Write a function that takes in a non-empty list of distinct integers and an integer representing a target sum.  If any two numbers in the input list sum up to the target sum, the function should return them in an list, in any order. If no two numbers sum up to the target sum, the function should return an empty list. 

def twoNumberSum(list, target):
    map = {}

    for num in list:
        dif = target - num  

        if dif in map:
            return [dif, num]
        else:
            map[num] = True

    return []

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