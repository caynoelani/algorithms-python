# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one. A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array, but that are in the same order as they appear in the array. For instance, [1, 3, 4] is a subsequence of [1, 2, 3, 4]

def ValidSubsequence(array1, sequence1):
    return

array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, 10]

array2 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence2 = [5, 1, 22, 25, 6, -1, 8, 10]

array3 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence3 = [5, 1, 22, 6, -1, 8, 10]

array4 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence4 = [4, 22, 25, 6]

print(ValidSubsequence(array1, sequence1)) #true
print(ValidSubsequence(array2, sequence2)) #true
print(ValidSubsequence(array3, sequence3)) #true
print(ValidSubsequence(array4, sequence4)) #false