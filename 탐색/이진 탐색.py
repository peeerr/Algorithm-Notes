# 이진 탐색
def binary_search(lst, key, start, end):  # start, end는 인덱스임에 주의
    if start > end:  # key가 없으면
        return False

    mid = (start + end) // 2

    if lst[mid] == key:
        return mid
    elif lst[mid] > key:
        return binary_search(lst, key, start, mid - 1)
    else:
        return binary_search(lst, key, mid + 1, end)
