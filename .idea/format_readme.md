# [난이도] 문제 번호. 문제 이름

> **문제 링크:** [LeetCode 문제 링크 입력](https://leetcode.com/problems/...)

## 📝 문제 설명
(여기에 문제 내용을 간단히 요약하거나 복사해 넣으세요.)
* 예시: 정수 배열 `nums`와 목표 값 `target`이 주어졌을 때, 더해서 `target`이 되는 두 수의 인덱스를 반환하라.

---

## 💡 접근 방식 (Approach)

### 1. 직관적인 접근 (Brute Force) - *실패했거나 비효율적인 방법*
* **생각한 로직:** 2중 반복문을 돌면서 모든 쌍을 하나씩 비교한다.
* **한계점:** 배열의 크기가 클 경우 시간 초과($O(N^2)$)가 발생할 수 있음.

### 2. 최적화된 접근 (Optimized) - *최종 통과한 방법*
* **생각한 로직:** 해시 테이블(Hash Map)을 사용하여 이미 지나간 숫자의 인덱스를 저장한다.
* **해결 과정:** `target - 현재 숫자`가 해시 테이블에 존재하는지 확인하면 $O(1)$만에 매칭되는 숫자를 찾을 수 있음.

---

## ⏱️ 복잡도 (Complexity)

* **시간 복잡도 (Time Complexity):** $O(N)$
  * 배열을 단 한 번만 순회하므로 배열의 길이 $N$에 비례하는 시간이 걸립니다.
* **공간 복잡도 (Space Complexity):** $O(N)$
  * 최악의 경우 배열의 모든 요소를 해시 테이블에 저장해야 하므로 $O(N)$만큼의 공간이 필요합니다.

---

## 💻 코드 핵심 요약 (Key Code)
> 전체 코드는 같은 폴더 내 소스코드 파일(`.py`, `.java` 등)에서 확인하고, 여기에는 핵심 아이디어나 기억해야 할 부분만 가볍게 적어둡니다.

```python
# 예시: 핵심 로직 기록
for i, num in enumerate(nums):
    remaining = target - num
    if remaining in hash_map:
        return [hash_map[remaining], i]
    hash_map[num] = i