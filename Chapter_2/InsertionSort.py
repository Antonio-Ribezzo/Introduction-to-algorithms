# Python list with n elements to be sorted
array_A = [5, 2, 4, 6, 1, 3]
print(array_A)
number = len(array_A)
print(f"Number of items into array A: {number}")
# Insertion Sort algorithm
def insertion_sort(arr):
    ''' Insertion sort algorithm.

    Parameters
    ----------
        arr: input array
    '''
    for item in range(len(arr)):
        key = arr[item]
    #   insert arr[item] into the sorted subarray arr[0: item - 1]
        j = item - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    return arr

array_sorted = insertion_sort(array_A)

print(f"This is the list sorted: {array_sorted}")

