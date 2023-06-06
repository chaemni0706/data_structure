def merge_sort(arr):
    n = len(arr)
    width = 1  #초기 너비는 1로 설정

    while width < n:  #너비가 배열 크기보다 작을 때까지 반복
        for i in range(0, n, 2 * width):  #현재 너비에 따라서 부분 배열을 병합
            left = i  #왼쪽 부분 배열의 시작 인덱스
            mid = min(i + width - 1, n - 1)  #중간 인덱스
            right = min(i + 2 * width - 1, n - 1)  #오른쪽 부분 배열의 끝 인덱스
            merge(arr, left, mid, right)  #부분 배열을 병합

        width *= 2  #너비를 2배로 증가

def merge(arr, left, mid, right):
    temp = []  #임시 배열을 생성합니다.
    i = left  #왼쪽 부분 배열의 현재 인덱스
    j = mid + 1  #오른쪽 부분 배열의 현재 인덱스

    while i <= mid and j <= right: #왼쪽 부분 배열과 오른쪽 부분 배열을 비교하면서 작은 값을 임시 배열에 저장
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid: #남은 요소들을 임시 배열에 추가
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(left, right + 1): #임시 배열의 값을 원래 배열에 복사
        arr[k] = temp[k - left]

arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
merge_sort(arr)
print("병합정렬:", arr)
