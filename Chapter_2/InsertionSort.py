# Python list with n elements to be sorted
array_A = [31, 41, 59, 26, 41, 58]
print(array_A)
number = len(array_A)
print(f"Number of items into array A: {number}")


# Insertion Sort algorithm (monotonically increasing)
def insertion_sort_incr(arr):
    ''' Insertion sort algorithm.

    Parameters
    ----------
        arr: input array
    '''
    for i in range(1, len(arr)):
        key = arr[i]  # value in the i-th position
        #  insert arr[item] into the sorted subarray arr[0: item - 1]
        j = i - 1  # position - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    return arr


# Insertion Sort algorithm (monotonically decreasing)
def insertion_sort_decr(arr):
    ''' Insertion sort algorithm.

    Parameters
    ----------
        arr: input array
    '''
    for item in range(1, len(arr)):
        key = arr[item]  # value in the i-th position #41
        #  insert arr[item] into the sorted subarray arr[0: item - 1]
        y = item - 1  # position - 1

        while y >= 0 and arr[y] < key:
            arr[y + 1] = arr[y]
            y = y - 1
        arr[y + 1] = key

    return arr


array_sorted_incr = insertion_sort_incr(array_A)
print(f"This is the list sorted in ascending order: {array_sorted_incr}")

array_sorted_decr = insertion_sort_decr(array_A)
print(f"This is the list sorted in descending order: {array_sorted_decr}")
