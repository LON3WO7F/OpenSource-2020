"""
        This is a function that takes a numeric list as a parameter and returns the sorted list.
        It does not modify the given list, as it works with a copy of it.
        It is a demonstrative algorithm, used for informational and learning purposes.
        It is open to changes, but keep the code clear and understandable, as its main purpose is not to
    be efficient, but to be a learning tool.
        Try keeping the code commented, explaining every functionality, and respecting PEP-8.
        Keep variable names clear and not general, so the code is easyli understandable (it is ok to use i
    for iterator, aux or temp, but just don't name every variable x, a, b, c, y)
        Make sure the modified function passes all assertion tests, but feel free to add more if you can
    think of extra cases that are not covered.
"""


def merge_sort(arr):
    """
    Sorts the given array, modifying the given array.

    :param arr: A given array of ints
    :return: Nothing
    """
    if len(arr) >1:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves
 
        merge_sort(L) # Sorting the first half
        merge_sort(R) # Sorting the second half
 
        i = j = k = 0
         
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
         
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
         
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1


def test_merge_sort():
    my_array = []
    merge_sort(my_array)
    assert my_array == []

    my_array = [1]
    merge_sort(my_array)
    assert my_array == [1]

    my_array = [3, 2, 1]
    merge_sort(my_array)
    assert my_array == [1, 2, 3]

    my_array = [1.21, 1.22, 1.203]
    merge_sort(my_array)
    assert my_array == [1.203, 1.21, 1.22]

    my_array = [1, 9, 2, 8, 3, 7, 4, 6, 5]
    merge_sort(my_array)
    assert my_array == [1, 2, 3, 4, 5, 6, 7, 8, 9]


test_merge_sort()
