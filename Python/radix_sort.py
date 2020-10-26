from counting_sort import counting_sort

"""
    Radix sort is another linear(-ish) time sorting algorthm!

    Let counting sort, it is a non-comparison sort.
    It distributes its elements by the value of each "digit"
    and repeats it for how many digits there are.

    For an array of n positive integers with maximum k,
    the running time is O(n log k).

    Here we consider "radix 10" i.e. base 10,
    though the algorithm works for other bases as well.
"""

def get_digit(n: int, d: int):
    for _ in range(d-1):
        n //= 10
    return n % 10

def radix_sort(arr: [int], max_value: int):
    max_value = max_value if max_value else max(arr)
    num_digits = len(str(max_value))
    for d in range(num_digits):
        arr = counting_sort(arr, 10, lambda a: get_digit(a, d+1)) # we want to use their (d+1)th digit as the key, not the number itself
    return arr

def test_radix_sort():
    arrays = [
        [20,14,51,55,33,22,21,15,13],
        [40,50,70,30,90,100,20],
        [1,1,0,1,1,True,1,10,1,False,0],
        [],
        [1,1000000,0],
        [400,500,700,3,900,100,20],
        list(range(200)),
    ]
    bounds = [100,100,10,5,None,1000000,200]
    for arr, b in zip(arrays, bounds):
        if len(arr)<=20:
            print(arr, radix_sort(arr, b))
        assert radix_sort(arr, b) == list(sorted(arr))

test_radix_sort()