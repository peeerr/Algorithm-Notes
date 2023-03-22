# 이진 탐색
def binary_search(lst, key, start, end):
    if start > end:   # key가 없으면
        return False

    mid = (start + end) // 2

    if lst[mid] == key:
        return mid
    elif lst[mid] > key:
        return binary_search(lst, start, mid - 1, key)
    else:
        return binary_search(lst, mid + 1, end, key)
