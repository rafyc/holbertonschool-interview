#include "sort.h"

void swap(int* a, int* b)
{

    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int *arr, int i, int n) {
    int largest = i;
     // left
    int left = 2 * i + 1;

    // right
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {

        swap(&arr[i], &arr[largest]);

        // Recursively heapify the affected
        // sub-tree
        heapify(arr, n, largest);
    }
}

// Main function to do heap sort
void heap_sort(int *array, size_t size) {

    // Build max heap
    for (int i = size / 2 - 1; i >= 0; i--)

        heapify(array, size, i);

    // Heap sort
    for (int i = size - 1; i >= 0; i--) {

        swap(&array[0], &array[i]);

        // Heapify root element
        // to get highest element at
        // root again
        heapify(array, i, 0);
    }
}
