# 삽입 정렬
def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):  # i부터 1까지
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:   # 더 작은 값 만나면
                break
