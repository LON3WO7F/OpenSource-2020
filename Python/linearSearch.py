def linear_search(values, search_for):
    search_at = 0
    search_res = False

# Match the value with each data element	
    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            print("Element is present at index", str(search_at))
            search_res = True
        else:
            search_at = search_at + 1

    return search_res

arr = []
n = int(input("Enter number of elements: "))
print("Enter elements in sorted order\n")
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
    arr.append(ele) # adding the element 
x = int(input("Enter key to search: "))

if(not(linear_search(arr, x))):
    print("Element is not present in array")