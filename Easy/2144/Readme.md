# [난이도] 2144. Minimum Cost of Buying Candies With Discount

<!--
> **문제 링크:** [LeetCode 문제 링크](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/?envType=daily-question&envId=2026-06-01)

## 📝 문제 설명

사탕의 가격들이 담긴 배열 `cost`가 주어집니다. 사탕을 살 때 다음과 같은 할인 규칙이 적용됩니다.
* 사탕 2개를 사면, **산 사탕 두 개의 가격보다 작거나 같은 가격**의 사탕 1개를 무료로 얻을 수 있습니다.
* 모든 사탕을 구매하기 위해 필요한 **최소 비용**을 구해야 합니다.
---

## 💡 접근 방식 (Approach)

### 1. 최적화된 접근 (Optimized)
* **생각한 로직:** sort(오름차순)을 사용하여 정렬된 결과를 모두 더함 (3의 배수인 인덱스는 제외)

---

## ⏱️ 복잡도 (Complexity)

* **시간 복잡도 (Time Complexity):** $O(N \log N)$
  * 배열의 길이가 $N$일 때, 파이썬의 `sort()` 함수(Timsort)를 사용하므로 정렬에 $O(N \log N)$이 소요됩니다.
  * 정렬 후 배열을 한 번 순회하는 데는 $O(N)$이 걸리므로, 전체 시간 복잡도는 정렬에 의해 **$O(N \log N)$**이 됩니다.
* **공간 복잡도 (Space Complexity):** $O(N)$ 또는 $O(1)$
  * 파이썬의 `sort()`는 기본적으로 Timsort 알고리즘을 사용하므로, 정렬 과정에서 O(N)의 추가 공간이 필요할 수 있습니다. (기존 배열을 제자리에서 수정하는 관점에서는 추가 변수 공간이 거의 들지 않아 $O(1)$로 보기도 합니다.)

---

## 💻 코드 핵심 요약 (Key Code)

```python
def minimumCost(cost):
    # 1. 내림차순 정렬하여 비싼 사탕부터 배치
    cost.sort(reverse=True)
    total_cost = 0

    # 2. 3번째 사탕(인덱스 2, 5, 8...)마다 스킵하며 비용 누적
    for i in range(len(cost)):
        if (i + 1) % 3 != 0:
            total_cost += cost[i]

    return total_cost

-->


    ## 📝 問題説明

キャンディの価格が入った配列 `cost` が与えられます。 キャンディを購入する際には、次のような割引ルールが適用されます。
* キャンディ2個を購入すると、**購入したキャンディ2個の価格以下**のキャンディ1個を無料で入手できます。
* すべてのキャンディを購入するために必要な**最低費用**を求める必要があります。
---

## 💡 アプローチ (Approach)

### 1. 最適化されたアプローチ (Optimized)
* **考えたロジック:** sort（昇順）を使用してソートされた結果をすべて合計します（3の倍数のインデックスは除外）

---

## ⏱️ 複雑性 (Complexity)

* **時間計算量 (Time Complexity):** $O(N \log N)$
* 配列の長さが $N$ の場合、Python の `sort()` 関数（Timsort）を使用するため、ソートに $O(N \log N)$ がかかります。
* ソート後に配列を一度巡回するのに$O(N)$かかるため、全体の時間計算量はソートによって**$O(N \log N)$**になります。
* **空間計算量 (Space Complexity):** $O(N)$ または $O(1)$
* Pythonの`sort()`は基本的にTimsortアルゴリズムを使用しているため、ソート過程でO(N)の追加スペースが必要になる場合があります。 (既存の配列をその場で修正する観点では、追加の変数スペースがほとんどかからないため、$O(1)$と見ることもあります。)

---

## 💻 コードの要点まとめ（Key Code）

```python
def minimumCost(cost):
# 1. 降順に並べて高価なキャンディから配置
cost.sort(reverse=True)
total_cost = 0

# 2. 3回目のキャンディ（インデックス2、5、8…）ごとにスキップしてコストを累積
for i in range(len(cost)):
if (i + 1) % 3 != 0:
total_cost += cost[i]

return total_cost