import timeit
import random

arr1 = [5, 2, 9, 1, 5, 6]
arr2 = random.sample(range(1, 100000), 10000)
'sorts'

'insertionSort'
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key 
    return arr


'mergeSort'
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

'timSort'
def timsort(arr):
    return sorted(arr)


def time_(func, name, arr, number):
    t1 = timeit.default_timer()
    for i in range(1000):
        func(arr)
    t2 = timeit.default_timer()
    print(f'\n{name} for arr{number}')
    print(t2-t1)

def time_all(data, number):
    for i in ((insertion_sort, 'insertionSort', data, number), (merge_sort, 'mergeSort', data, number), (timsort, 'timSort', data, number)):
        time_(*i)

'checks for arr1'
time_all(arr1, '1')
time_all(arr2, '2')
