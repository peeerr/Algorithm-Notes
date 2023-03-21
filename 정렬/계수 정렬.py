def counting_sort(lst):
    # lst의 가장 큰 값을 크기로 하는 배열 생성
    temp = [ 0 for _ in range(max(lst) + 1) ]

    for i in lst:
        temp[i] += 1  # 해당 원소 카운팅

    # 출력
    for i, v in enumerate(temp):
        for _ in range(v):
            print(i, end=' ')
