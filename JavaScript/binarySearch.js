function binarySearch(arr, target) {
    // initialize first and last position of given array
    let first = 0;
    let last = arr.length - 1;
    // `position` will be our answer variable that we will use in after we have found index of the target in provided array
    let position = -1;
    // found` will be our boolean to check if the target was found in provided array
    let found = false;
    // `middle` will be middle index of provided array
    let middle;

    // start loop and check while the `found` is false and `first` variable is lower or equal of `last` variable
    while (found === false && first <= last) {
        // calculate the average value in the array and assign it to `middle` variable
        middle = Math.floor((first + last) / 2);
        // if this calculated variable is the target that we were searching then end the loop and return the position of this target in provided array
        if (arr[middle] == target) {
            found = true;
            position = middle;
        }else if (arr[middle] > target){ //if the target is greater than our middle number in array then assign to `last` new value, other way to `first` variable
            last = middle - 1;
        }else{
            first = middle + 1;
        }
    }
    return position;
}

// run created function
binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 13);
