# Algorithm-Notes
자주 쓰이는 알고리즘을 정리하는 노트 <br><br>

# 📌 시간 복잡도
* 파이썬은 **초당 대략 20,000,000번의 연산**을 수행할 수 있다.

* 문제를 풀 때, N의 범위를 보고 어떤 시간 복잡도까지 허용되는 지 고려해야 한다.
  * 예를 들어 N이 1,000,000이면 **O(NlogN)** 성능이 나오는 알고리즘을 설계해야 한다.<br><br>

# 📌 정렬
### [선택 정렬](https://github.com/peeerr/Algorithm-Notes/blob/main/%EC%A0%95%EB%A0%AC/%EC%84%A0%ED%83%9D%20%EC%A0%95%EB%A0%AC.py)
* 최선의 경우 **O(N^2)**
* 최악의 경우 **O(N^2)**

### [삽입 정렬](https://github.com/peeerr/Algorithm-Notes/blob/main/%EC%A0%95%EB%A0%AC/%EC%82%BD%EC%9E%85%20%EC%A0%95%EB%A0%AC.py)
* 최선의 경우 **O(N)** -> **이미 데이터가 정렬되어 있는 경우**
* 최악의 경우 **O(N^2)**

### [퀵 정렬](https://github.com/peeerr/Algorithm-Notes/blob/main/%EC%A0%95%EB%A0%AC/%ED%80%B5%20%EC%A0%95%EB%A0%AC.py) (호어 분할 방식)
* 평균의 경우 **O(NlogN)**
* 최악의 경우 **O(N^2) -> 이미 데이터가 정렬되어 있는 경우**

### [계수 정렬](https://github.com/peeerr/Algorithm-Notes/blob/main/%EC%A0%95%EB%A0%AC/%EA%B3%84%EC%88%98%20%EC%A0%95%EB%A0%AC.py)
* 원소의 개수가 N, 원소 중 최댓값을 K라 할 때, 시간 복잡도 O(N + K)<br>
-> 적절한 인덱스에 +1 하는 과정에서 N, 출력하는 과정에서 최댓값까지 반복하므로 K
* **리스트의 크기를 이용하는 만큼 항상 사용할 순 없다.**
  * **최댓값이 작고 총 원소의 개수(예를 들어 10만 개 이상)나 중복되는 원소가 많을수록 유리**

### 파이썬 내장함수 (병함 정렬 기반)
#### sort() 및 sorted()
* 일반적으로 퀵 정렬보다 느리지만 **최악의 경우에도 O(NlogN)를 보장**한다.

## 정리
* 별도의 요구 없이 단순 정렬을 요구할 때 -> 파이썬 내장함수 사용
* 원소의 크기가 한정, 빠르게 동작해야 할 때 -> 계수 정렬 사용
* 특정 정렬 알고리즘의 원리를 물을 때 -> 특정 정렬 알고리즘 사용 <br><br>

# 📌 탐색
### [이진 탐색](https://github.com/peeerr/Algorithm-Notes/blob/main/%ED%83%90%EC%83%89/%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89.py)
* 시간 복잡도 **O(logN)**
* **탐색 범위가 매우 큰 상황에서 쓰인다.**<br>
-> 탐색 범위가 3,000만정도를 넘어가면 이진 탐색을 사용하자.
