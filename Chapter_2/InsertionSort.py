# Python list with n elements to be sorted
array_A = [5, 2, 4, 6, 1, 3]
print(array_A)
number = len(array_A)
print(f"Number of items into array A: {number}")
# Insertion Sort algorithm
for item in range(len(array_A)):
    key = array_A[item]
#   insert array_A[item] into the sorted subarray A[0: item - 1]
    j = item - 1

    while j >= 0 and array_A[j] > key:
        array_A[j + 1] = array_A[j]
        j = j - 1
    array_A[j + 1] = key


print(f"This is the list sorted: {array_A}")
