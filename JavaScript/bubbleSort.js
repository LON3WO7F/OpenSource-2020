let bubbleSort = (inputArr) => {
    // Returns the input array sorted
    let len = inputArr.length; // Gets the length of the array
    let is_sorted = false; // Checks if the array is or is not sorted
    while(!is_sorted){ // While the array is not sorted
        is_sorted = true; // Considers the array as sorted
        for (let i = 0; i < len; i++) { //Iterates through the array 
            if (inputArr[i] > inputArr[i + 1]) { //To find 2 items that are not sorted
                let tmp = inputArr[i]; //Swaps the items
                inputArr[i] = inputArr[i + 1];
                inputArr[i + 1] = tmp;
                is_sorted = false; //And considers the array as not sorted
            }
        }
    }
    return inputArr; //Returns the sorted array
};