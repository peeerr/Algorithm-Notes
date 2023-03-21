# 퀵 정렬
def quick_sort(lst, start, end):
    if start >= end:  # 원소가 1개면
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 원소 찾을 떄까지
        while left <= end and lst[left] <= lst[pivot]:
            left += 1

        # 피벗보다 작은 원소 찾을 때까지
        while right > start and lst[right] >= lst[pivot]:  # start는 피벗이기 때문에 포함 X
            right -= 1

        if left > right:  # 엇갈렸다면 피벗과 작은 원소 교환
            lst[pivot], lst[right] = lst[right], lst[pivot]
        else:  # 아니면 작은 원소와 큰 원소 교환
            lst[left], lst[right] = lst[right], lst[left]

    quick_sort(lst, start, right - 1)
    quick_sort(lst, right + 1, end)
