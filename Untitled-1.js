function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let currentElement = arr[i];
        let j = i - 1;

        while (j >= 0 && arr[j] > currentElement) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = currentElement;
    }

    return arr; 
}


let arr = [5, 2, 9, 1, 5, 6];
console.log("Sorted array:", insertionSort(arr)); 
