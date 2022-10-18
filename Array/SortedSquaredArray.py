#Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

def SortedSquaredArray(array):
    outputArray = [0 for _ in array]
    start = 0
    end = len(array) - 1

    for idx in reversed(range(len(array))):

        if abs(array[start]) > abs(array[end]):
            outputArray[idx] = array[start]**2
            start += 1
        else:
            outputArray[idx] = array[end]**2
            end -=1

    return outputArray


array1 = [1, 2, 3, 4, 5, 6, 8, 9]
array2 = [1]
array3 = [-5, -4, -3, -2, -1]
array4 = [-10, -5, 0, 5, 10]

print(SortedSquaredArray(array1)) #[1, 4, 9, 16, 25, 36, 64, 81]
print(SortedSquaredArray(array2)) #[1]
print(SortedSquaredArray(array3)) #[1, 4, 9, 16, 25]
print(SortedSquaredArray(array4)) #[0, 25, 25, 100, 100]