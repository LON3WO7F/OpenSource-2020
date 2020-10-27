from random import randint


def insertion_sort(array, left=0, right=None):
    """
    Insertion sort on a subset of an array. Left and right are parameters to mark the subset
    Args:
        array (list): array to sort
        left (int): Leftmost index to set of the sort
        right (int): Rightmost index to set the sort
    Returns:
        partially sorted list
    """
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        # This is the element we want to position in its correct place
        key_item = array[i]
        # j will be used to find the correct position of the element referenced by `key_item`
        j = i - 1
        while j >= left and array[j] > key_item:
            # Shift the value one position to the left
            array[j + 1] = array[j]
            j -= 1
        # place key_item in the correct position
        array[j + 1] = key_item
    return array


def merge(left, right):
    """
    Receives two different sorted arrays that need to be merged together.
    Returns singly merged array
    """
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def timsort(array):
    """
    The following is an implementation of timsort which is a hybrid insertion sort and merge sort.
    The timsort function can take any array and sort in O(nlog2n) average time.
    """
    min_run = 32
    n = len(array)
    # Slice and sort small portions of the array
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # merge sorted slices
    size = min_run
    while size < n:
        # Determine the arrays that will be merged together
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            # Merge the two subarrays.
            merged_array = merge(left=array[start : (midpoint + 1)], right=array[(midpoint + 1) : (end + 1)])

            # Put the merged array back into your array
            array[start : start + len(merged_array)] = merged_array

        # start with min_run size and double after each merge
        size *= 2

    return array


if __name__ == "__main__":
    # DEMO
    array = [randint(0, 1000) for i in range(50)]
    print(f"Un-sorted Array:\n{array}")
    sorted_array = timsort(array)
    print(f"Sorted Array:\n{sorted_array}")
