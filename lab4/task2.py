#!/usr/bin/env python3

import random

def quicksort_desc(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort_desc(arr, low, p - 1)
        quicksort_desc(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] > pivot:  # DESC
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    numbers = [random.randint(1, 100) for _ in range(50)]
    print("Before:", numbers)

    quicksort_desc(numbers, 0, len(numbers) - 1)
    print("\nAfter   :", numbers)

if __name__ == '__main__':
    main()