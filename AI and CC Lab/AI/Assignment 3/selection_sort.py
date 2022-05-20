def selection_sort(arr):
 for i in range(0, len(arr) - 1):
    smallest = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[smallest]:
            smallest = j
    arr[i], arr[smallest] = arr[smallest], arr[i]
 
arr = input('Enter the Elements of Array : ').split()
arr = [int(x) for x in arr]
selection_sort(arr)
print('Sorted Array : ', end='')
print(arr)