def radix_sort_16(arr):
    max_value = max(arr)  #입력 리스트에서 최댓값을 찾습니다.
    exp = 1  #현재 자리수의 16의 거듭제곱

    while max_value // exp > 0:
        count = [0] * 16  #16개의 버켓을 초기화합니다.
        output = [0] * len(arr)

        for num in arr:
            digit = (num // exp) % 16
            count[digit] += 1

        for i in range(1, 16):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            digit = (arr[i] // exp) % 16
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1

        arr = output
        exp *= 16

    return arr

arr = [123, 456, 789, 234, 567, 890]
sorted_arr = radix_sort_16(arr)
print("기수정렬 (16 버켓):", sorted_arr)

def radix_sort_10(arr):
    max_value = max(arr)  #입력 리스트에서 최댓값을 찾습니다.
    exp = 1  #현재 자리수의 10의 거듭제곱

    while max_value // exp > 0:
        count = [0] * 10  #10개의 버켓을 초기화합니다.
        output = [0] * len(arr)

        for num in arr:
            digit = (num // exp) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            digit = (arr[i] // exp) % 10
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1

        arr = output
        exp *= 10

    return arr

arr = [123, 456, 789, 234, 567, 890]
sorted_arr = radix_sort_10(arr)
print("기수정렬 (10 버켓):", sorted_arr)

def radix_sort_2(arr):
    max_value = max(arr)  #입력 리스트에서 최댓값을 찾습니다.
    exp = 1  #현재 자리수의 2의 거듭제곱

    while max_value // exp > 0:
        count = [0] * 2  #2개의 버켓을 초기화합니다.
        output = [0] * len(arr)

        for num in arr:
            digit = (num // exp) % 2
            count[digit] += 1

        for i in range(1, 2):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            digit = (arr[i] // exp) % 2
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1

        arr = output
        exp *= 2

    return arr

arr = [123, 456, 789, 234, 567, 890]
sorted_arr = radix_sort_2(arr)
print("기수정렬 (2 버켓):", sorted_arr)
