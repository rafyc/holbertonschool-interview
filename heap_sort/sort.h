#ifndef SORT_H
#define SORT_H

#include <stdlib.h>
#include <stdio.h>

void print_array(const int *array, size_t size);
void heap_sort(int *array, size_t size);
void heapify(int *arr, int i, int n);
void swap(int* a, int* b);

#endif /* SORT_H */
