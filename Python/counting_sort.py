"""
    Counting sort is a linear time sorting algorthm!

    What it does is instead of comparing elements,
    it keeps track of the elements when sweeping through the array,
    and places them into a new array accordingly.

    For an array of n positive integers with maximum k,
    the running time is O(n+k).

    The reason why it can achieve linear time
    without breaking the Ω(n log n) lower bound is because
    it is NOT a comparison sort, which was the only assumption
    when proving the lower bound.
"""

def counting_sort(arr: [int], bound:int = 100, key = lambda x: x):
    # The key is a surprise tool that will help us later
    # (see radix-sort)
    if bound == None:
        bound = max(arr)
        keys = [key(x) for x in arr]
    else:
        assert bound>0, "Bound must be a positive integer"
        keys = [key(x) for x in arr]
        for k in keys:
            assert 0<=k<=bound, "{} should be in [0,{}]".format(k,bound)
    tally = [0]*(bound+1)
    for k in keys:
        tally[k] += 1
    cum_tally = [x for x in tally]
    for i in range(bound):
        cum_tally[i+1] += cum_tally[i]
    res = [None]*len(arr)
    for x,k in zip(arr[::-1],keys[::-1]): # going through the array in reverse keeps the sort stable
        cum_tally[k] -= 1
        res[cum_tally[k]] = x
    return res

def test_counting_sort():
    arrays = [
        [2,4,1,5,3,2,2,5,3],
        [4,5,7,3,9,10,2],
        [1,1,0,1,1,True,1,10,1,False,0],
        [],
        [1,10000,0],
        [4,5,7,3,9,10,2],
        list(range(200)),
    ]
    bounds = [5,10,10,5,None,10000,200]
    for arr, b in zip(arrays, bounds):
        assert counting_sort(arr, b) == list(sorted(arr))

test_counting_sort()