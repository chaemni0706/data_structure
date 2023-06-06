def is_sorted(arr): #배열을 인자로 받아서 배열이 오름차순으로 정렬되어 있는지를 검사
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                return False

    return True

array1 = [1, 2, 3, 4, 5]
array2 = [1, 3, 2, 4, 5]

print(is_sorted(array1))
print(is_sorted(array2))