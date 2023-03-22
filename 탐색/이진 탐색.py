# 이진 탐색
def binary_search(lst, key, start, end):  # start, end 는 인덱스 임에 주의
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    return False
