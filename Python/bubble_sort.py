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

from copy import deepcopy


def bubble_sort(given_list):
    """
        Takes a list as a parameter, returns the given list but sorted.

        :param given_list: A numerical list
        :return sorted_list: The given list, sorted using bubble sort
    """
    sorted_list = deepcopy(given_list) # Copies the list in a temporary list that will be sorted

    is_sorted = False # Considers the list not sorted by default
    while not is_sorted: # Executes the code while the list is not sorted
        is_sorted = True # At the beginning of the loop, considers the list as sorted
        for i in range(1, len(sorted_list)): # Iterates trough all items of the list
            if sorted_list[i-1] > sorted_list[i]: # If it finds 2 items in the wrong order...
                is_sorted = False # ...considers the list not sorted...

                aux = sorted_list[i-1] # ... and swaps the elements in order to put them in the right order
                sorted_list[i-1] = sorted_list[i]
                sorted_list[i] = aux
    
    return sorted_list # Finally, the sorted list is returned


def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert bubble_sort([1, 2, 3, 3, 3, 3, 3]) == [1, 2, 3, 3, 3, 3, 3]
    assert bubble_sort([1.23, 1.32, 3.89, 2.333]) == [1.23, 1.32, 2.333, 3.89]
    assert bubble_sort([1, 9, 2, 8, 3, 7, 4, 6, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
