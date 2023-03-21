# Algorithm-Notes
자주 쓰이는 알고리즘을 정리하는 노트 <br><br>

# 📌 정렬
### [선택 정렬](https://github.com/peeerr/Algorithm-Notes/blob/main/%EC%A0%95%EB%A0%AC/%EC%84%A0%ED%83%9D%20%EC%A0%95%EB%A0%AC.py)
최선의 경우 O(N^2)<br>
최악의 경우 O(N^2)

### [삽입 정렬](https://github.com/peeerr/Algorithm-Notes/blob/main/%EC%A0%95%EB%A0%AC/%EC%82%BD%EC%9E%85%20%EC%A0%95%EB%A0%AC.py)
최선의 경우 O(N) -> **이미 데이터가 정렬되어 있는 경우**<br>
최악의 경우 O(N^2)

### [퀵 정렬](https://github.com/peeerr/Algorithm-Notes/blob/main/%EC%A0%95%EB%A0%AC/%ED%80%B5%20%EC%A0%95%EB%A0%AC.py) (호어 분할 방식)
평균의 경우 O(NlogN)<br>
최악의 경우 O(N^2) -> **이미 데이터가 정렬되어 있는 경우**

### [계수 정렬](https://github.com/peeerr/Algorithm-Notes/blob/main/%EC%A0%95%EB%A0%AC/%EA%B3%84%EC%88%98%20%EC%A0%95%EB%A0%AC.py)
원소의 개수가 N, 원소 중 최댓값을 K라 할 때, 시간 복잡도 O(N + K)<br>
-> 적절한 인덱스에 +1 하는 과정에서 N, 출력하는 과정에서 최댓값까지 반복하므로 K<br>
**단, 리스트의 크기를 이용하는 만큼 항상 사용할 순 없다.<br>
(최댓값이 작고 총 원소의 개수(예를 들어 10만 개 이상)나 중복되는 원소가 많을수록 유리)**

### 파이썬 내장함수 (병함 정렬 기반)
**sort() 및 sorted()**<br>
일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 O(NlogN)를 보장한다.<br>

## 정리
* 별도의 요구 없이 단순 정렬을 요구할 때 -> 파이썬 내장함수 사용
* 원소의 크기가 한정, 빠르게 동작해야 할 때 -> 계수 정렬 사용
* 특정 정렬 알고리즘의 원리를 물을 때 -> 특정 정렬 알고리즘 사용
