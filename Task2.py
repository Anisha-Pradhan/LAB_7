# Bubble Sort with Trace

arr = [64, 34, 25, 12, 22, 11, 90]

n = len(arr)

print("Original List:", arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Pass", i + 1, ":", arr)