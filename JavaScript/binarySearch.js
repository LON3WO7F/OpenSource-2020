function binarySearch(arr, target) {
    let first = 0;
    let last = arr.length - 1;
    let position = -1;
    let found = false;
    let middle;

    while (found === false && first <= last) {
        middle = Math.floor((first + last) / 2);
        if (arr[middle] == target) {
            found = true;
            position = middle;
        }else if (arr[middle] > target){
            last = middle - 1;
        }else{
            first = middle + 1;
        }
    }
    return position;
}

binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 13);
