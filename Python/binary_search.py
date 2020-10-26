print('''INSTRUCTIONS FOR ADAPTED CODE: 
    can run a binary search in the following ways:

    1) in python shell:
        run code as is
        
    2) in your terminal:
        open a command line / terminal 
        cd to the path of binary_search.py
        type your list (e.g. 1 2 4 10 12) and key (e.g. 4) in the following way: 
            python binary_search.py -e 1 2 4 10 12 -k 4 
            
    3) directly by writing on the script
        activate lines 22 - 26 and change the sorted_list and key parameters 
        deactivate lines 28 - 32
        run code \n
''')

import argparse
ap = argparse.ArgumentParser()

# ap.add_argument("-e", "--sorted_list", \
#                 default = [1,2,5,12,122,232,1334,1445,3240], nargs = '+',
#                 help="add integer list of data in sorted order in default (line 4)")
# ap.add_argument("-k", "--key", default = 12, type=int,
#                 help="enter key to search")

ap.add_argument("-e", "--sorted_list", \
                default = '', nargs = '+', 
                help="add integer list of data in sorted order in default (line 4)")
ap.add_argument("-k", "--key", default = '',
                help="enter key to search")

args = vars(ap.parse_args())


def binary_search(arr, n, key):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid+1
        elif arr[mid] < key:
            low = mid+1
        else:
            high = mid-1
    return -1


if __name__ == "__main__":
    # n = int(input('Enter number of Elements: '))
    arr = list( map( int, input('Enter data in sorted order: ').split() ) ) \
        if args["sorted_list"] == '' else args["sorted_list"]
    key = int(input('Enter key to search: ')) if args["key"] == '' else args["key"]
    n = len(arr)
    x = binary_search(arr, n, key)
    if x == -1:
        print('Element not found')
    else:
        print("Element found at position ", x)