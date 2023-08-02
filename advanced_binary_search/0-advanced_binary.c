#include "search_algos.h"

/**
 * @array: Pointer to the first element of the array to search in
 * @size: Number of elements in array
 * @value: Value to search for
 * Return: Index of the leftmost occurrence of value if found, or -1 if not found
 */

int advanced_binary(int *array, size_t size, int value) {
    int low = -1;
    int high = size - 1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (array[mid] == value) {
            return mid;
        } else if (value > array[mid]) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
