def bubble_sort(arr, counter):
    length = len(arr) - 1

    while counter > 0:
        for i in range(length):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                counter -= 1

v = [19, 1, 9, 7, 3, 10, 13, 15, 9, 12]
bubble_sort(v, 3)
print(v)
