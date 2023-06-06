def counting_sort(arr): #입력 리스트의 문자 개수를 세기 위한 카운트 배열을 초기화
    n = len(arr)

    count = [0] * 26 #알파벳 소문자를 기준으로 가정

    for char in arr: #입력 리스트에서 각 문자의 개수를 세어 카운트 배열에 저장
        count[ord(char) - ord('a')] += 1
   
    for i in range(1, 26): #카운트 배열을 누적 합으로 갱신
        count[i] += count[i - 1]

    sorted_arr = [''] * n #정렬된 결과를 저장할 배열을 생성
   
    for char in arr: #입력 리스트를 순회하면서 정렬된 결과를 sorted_arr에 저장
        index = count[ord(char) - ord('a')] - 1
        sorted_arr[index] = char
        count[ord(char) - ord('a')] -= 1

    return sorted_arr

arr = ['d', 'b', 'a', 'c', 'e']
sorted_arr = counting_sort(arr)
print("카운팅 정렬:", sorted_arr)