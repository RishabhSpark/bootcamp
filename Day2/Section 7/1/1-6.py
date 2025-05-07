import timeit

builtin_sort_time = timeit.timeit("sorted(range(1000))", number=1000)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

custom_sort_time = timeit.timeit("bubble_sort(range(1000))", setup="from __main__ import bubble_sort", number=1000)

print(f"Built-in sorted() time: {builtin_sort_time} seconds")
print(f"Custom bubble sort time: {custom_sort_time} seconds")
