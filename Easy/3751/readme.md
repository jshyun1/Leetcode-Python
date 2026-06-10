<!--
# [Hard] 3400. Total Waviness of Numbers in Range I

> **문제 링크:** [LeetCode - Total Waviness of Numbers in Range I](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/)

## 📝 문제 설명
두 정수 `num1`과 `num2`가 주어집니다. 범위 `[num1, num2]`에 속하는 모든 정수의 **총 웨이비니스(Total Waviness)**를 구해야 합니다. 

특정 숫자의 웨이비니스는 숫자를 구성하는 각 자릿수 중, 양옆의 자릿수보다 크거나(**Peak/local maximum**) 양옆의 자릿수보다 작은(**Valley/local minimum**) 자릿수의 개수를 의미합니다. 단, 숫자의 가장 첫 자릿수와 마지막 자릿수는 양옆의 숫자가 모두 존재하지 않으므로 웨이비니스를 측정할 때 제외됩니다.

---

## 💡 접근 방식 (Approach)

### 1. 직관적인 접근 (Brute Force) - *소규모 입력용 방법*
* **생각한 로직:** `num1`부터 `num2`까지 반복문을 돌며 모든 숫자를 문자열로 변환합니다. 그 후 각 문자열의 index 1부터 `length - 2`까지 순회하며 양옆의 문자와 대소 관계를 비교하여 조건(Peak 또는 Valley)을 만족할 때마다 카운트를 증가시킵니다.
* **한계점:** 숫자의 범위($num2 - num1$)가 매우 크거나 자릿수가 길어질 경우, 모든 숫자를 문자열로 바꾸고 순회하는 방식은 **시간 초과(Time Limit Exceeded, TLE)**를 유발합니다. 시간 복잡도가 $O(N \times L)$ (단, $N$은 수의 개수, $L$은 자릿수)이 되기 때문입니다.

### 2. 최적화된 접근 (Optimized) - *최종 해결 방향성*
* **생각한 로직:** 대규모 범위 문제를 해결하기 위해 **자릿수 DP (Digit DP)** 기법을 적용해야 합니다.
* **해결 과정:** 숫자를 일일이 세는 대신, `0`부터 `X`까지의 총 웨이비니스를 구하는 함수 `solve(X)`를 정의합니다. 가장 큰 자릿수부터 숫자를 하나씩 결정해 나가며, `(현재 인덱스, 이전 자릿수 값, 이전 대소 관계 상태, 상한선 제한 여부, 앞자리 0 여부)`를 메모이제이션(Memoization) 테이블에 저장하여 중복 계산을 방지합니다. 최종 결과는 `solve(num2) - solve(num1 - 1)`로 도출합니다.

---

## ⏱️ 복잡도 (Complexity)

### 작성한 브루트 포스 코드 기준:
* **시간 복잡도 (Time Complexity):** $O(N \times L)$
  * 범위 내 정수의 개수 $N = (num2 - num1 + 1)$만큼 반복하고, 각 숫자마다 자릿수 길이 $L$만큼 순회합니다.
* **공간 복잡도 (Space Complexity):** $O(L)$
  * 숫자를 문자열로 변환할 때 자릿수 길이 $L$만큼의 문자열 공간이 필요합니다.

### 자릿수 DP(Digit DP) 최적화 기준:
* **시간 복잡도 (Time Complexity):** $O(\log_{10}(num2) \times 10 \times \text{상태수})$
  * 숫자의 자릿수(대략 $\log_{10}(num2)$)에 비례하므로 매우 효율적이며 큰 수 범위도 빠르게 통과할 수 있습니다.
* **공간 복잡도 (Space Complexity):** $O(\log_{10}(num2) \times \text{상태수})$
  * DP 테이블(Memoization)을 유지하기 위한 공간이 필요합니다.

---

## 💻 코드 핵심 요약 (Key Code)
> 작성한 코드 중 인덱스 범위를 제어하고 Peak와 Valley를 판별하는 핵심 로직입니다.

```python
# 양 끝 자릿수를 제외하고 (1번 인덱스부터 length-2번 인덱스까지) 탐색
for i in range(1, length - 1):
    # Case 1: Peak (양옆보다 큰 경우)
    # Case 2: Valley (양옆보다 작은 경우)
    if (num_str[i] > num_str[i-1] and num_str[i] > num_str[i+1]) or \
       (num_str[i] < num_str[i-1] and num_str[i] < num_str[i+1]):
        waves += 1

-->


# [Hard] 3400. Total Waviness of Numbers in Range I

> **문제 링크:** [LeetCode - Total Waviness of Numbers in Range I](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/)

## 📝 問題説明
2つの整数「num1」と「num2」が与えられます。 範囲〔num1, num2〕に属するすべての整数の**総ウェイビネス（Total Waviness）**を求める必要があります。 

特定の数字のウェイビニスは、数字を構成する各桁のうち、両側の桁より大きい（**Peak/local maximum**）か、両側の桁より小さい（**Valley/local minimum**）桁の個数を意味します。 ただし、数字の最初の桁と最後の桁は両側の数字が存在しないため、ウェイビネスを測定する際には除外されます。

---

## 💡 アプローチ（Approach）

### 1. 直感的なアプローチ（Brute Force） - *小規模入力用の方法*
* **考えたロジック:** `num1`から`num2`までのループを回し、すべての数字を文字列に変換します。 その後、各文字列のindex 1から`length - 2`までを巡回し、両側の文字と大小の関係を比較して条件（PeakまたはValley）を満たすたびにカウントを増やします。
* **制限点:** 数値の範囲（$num2 - num1$）が非常に大きいか桁数が長くなる場合、すべての数字を文字列に変換して巡回する方法は**時間超過（Time Limit Exceeded, TLE）**を引き起こします。 時間計算量が$O(N \times L)$（ただし、$N$は数の個数、$L$は桁数）になるためです。

### 2. 最適化されたアプローチ（Optimized） - *最終解決方向*
* **考えたロジック:** 大規模範囲問題を解決するために、**桁数DP（Digit DP）**手法を適用する必要があります。
* **解決過程:** 数字を一つ一つ数える代わりに、`0`から`X`までの総ウェイビネスを求める関数`solve(X)`を定義します。 最も大きい桁から数字を一つずつ決定し、`（現在のインデックス、前の桁の値、前の大小関係の状態、上限の制限の有無、先頭の0の有無）`をメモ化（Memoization）テーブルに保存して重複計算を防止します。 最終結果は `solve(num2) - solve(num1 - 1)` で導出します。

---

## ⏱️ 複雑性（Complexity）

### 作成したブルートフォースコードの基準：:
* **時間計算量（Time Complexity）：** $O(N \times L)$
  * 範囲内の整数の個数 $N = (num2 - num1 + 1)$だけ繰り返し、各数字ごとに桁数Lだけ巡回します。
* **空間計算量（Space Complexity）：** $O(L)$
  * 数字を文字列に変換する際には、桁数L分の文字列スペースが必要です。

### 桁数DP（Digit DP）最適化基準：:
* **時間計算量（Time Complexity）：** $O(\log_{10}(num2) \times 10 \times \text{状態数})$
  * 数字の桁数（おおよそ $\log_{10}(num2)$)に比例するため非常に効率的であり、大きな数の範囲も速く通過できます。
* **空間計算量（Space Complexity）：** $O(\log_{10}(num2) \times \text{状態数})$
  * DPテーブル（Memoization）を維持するためのスペースが必要です。

---

## 💻 コードの核心要約（Key Code）
> 作成したコードの中でインデックス範囲を制御し、PeakとValleyを判別する核心ロジックです。

```python
# 両端の桁数を除いて（1番目のインデックスからlength-2番目のインデックスまで）探索
for i in range(1, length - 1):
    # Case 1: Peak（両側より大きい場合）
    # Case 2: Valley（両側より小さい場合）
    if (num_str[i] > num_str[i-1] and num_str[i] > num_str[i+1]) or \
       (num_str[i] < num_str[i-1] and num_str[i] < num_str[i+1]):
        waves += 1