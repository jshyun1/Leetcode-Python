# 🟡 Earliest Finish Time (가장 빠른 작업 종료 시간 찾기)
<!--
> **문제 유형:** 브루트 포스 (Brute Force), 시뮬레이션 (Simulation)

## 📝 문제 설명
두 가지 종류의 작업(Land 작업과 Water 작업)에 대해 각각 가능한 시작 시간(`StartTime`)과 소요 시간(`Duration`)의 후보 리스트가 주어집니다. 
하나의 Land 작업과 하나의 Water 작업을 조합하여 수행할 때, 두 작업이 서로 겹치지 않도록 조율하면서 **전체 작업을 가장 빨리 끝낼 수 있는 최적의 조합과 그때의 최소 종료 시간**을 구해야 합니다.

---

## 💡 접근 방식 (Approach)

### 1. 전수 조사 (Brute Force) 를 통한 모든 조합 탐색
* **전체 탐색:** Land 작업 후보 배열과 Water 작업 후보 배열을 2중 `for` 루프로 순회하며 가능한 모든 $(i, j)$ 조합을 검사합니다.

### 2. 작업 중첩 여부에 따른 종료 시간 계산
각 조합마다 두 작업의 시간대가 겹치는지 여부를 판단합니다.
* **경우 1: 두 작업이 겹치지 않는 경우 (`if`)**
  * 조건: `landFinishTime <= waterStartTime[j]` 또는 `waterFinishTime <= landStartTime[i]`
  * 한 작업이 끝나고 다른 작업이 시작되므로, 전체 종료 시간은 두 작업의 종료 시간 중 더 큰 값이 됩니다. (`max(landFinishTime, waterFinishTime)`)
* **경우 2: 두 작업이 겹치는 경우 (`else`)**
  * 두 작업의 시간대가 중겹되므로, 하나의 작업을 다른 작업이 끝난 뒤로 미뤄야 합니다.
  * 따라서 미뤄진 케이스들을 고려하여 계산한 종료 시간 중 최댓값을 구합니다.

### 3. 최솟값 갱신
* 각 조합에서 계산된 `FinishTime` 중 가장 작은 값을 `minFinishTime`에 지속적으로 갱신하여 최종 반환합니다.

---

## ⏱️ 복잡도 (Complexity)

* **시간 복잡도 (Time Complexity):** $O(N \times M)$
  * `landStartTime` 배열의 길이를 $N$, `waterStartTime` 배열의 길이를 $M$이라고 할 때, 2중 반복문을 통해 모든 쌍을 확인하므로 **$O(N \times M)$**의 시간이 소요됩니다.
* **공간 복잡도 (Space Complexity):** $O(1)$
  * 입력 배열 외에 추가적인 배열이나 자료구조를 생성하지 않고, 변수(`landFinishTime`, `waterFinishTime`, `minFinishTime` 등) 몇 개만 사용하므로 공간 복잡도는 상수 시간인 **$O(1)$**입니다.

---

## 💻 코드 핵심 요약 (Key Code)

```python
from typing import List

def earliestFinishTime(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int: 
    minFinishTime = 300000  # 충분히 큰 값으로 초기화
    
    for i in range(len(landStartTime)):
        landFinishTime = landStartTime[i] + landDuration[i]
        
        for j in range(len(waterStartTime)):
            waterFinishTime = waterStartTime[j] + waterDuration[j]
            
            # 두 작업이 서로 겹치지 않는 경우
            if landFinishTime <= waterStartTime[j] or waterFinishTime <= landStartTime[i]:
                FinishTime = max(landFinishTime, waterFinishTime)
            # 두 작업이 겹쳐서 조정이 필요한 경우
            else:
                FinishTime = max(landFinishTime + waterDuration[j], waterFinishTime + landDuration[i]) 
                
            # 최소 종료 시간 갱신
            minFinishTime = min(minFinishTime, FinishTime)   
    
    return minFinishTime
    -->

    > **問題の種類:** ブルートフォース (Brute Force)、シミュレーション (Simulation)

## 📝 問題説明
2種類の作業（Land作業とWater作業）について、それぞれ可能な開始時間（`んどo`）と所要時間（`Duration`）の候補リストが与えられます。 
1つのLand作業と1つのWater作業を組み合わせて実行する際、2つの作業が互いに重ならないように調整しながら、**全体の作業を最も早く終えるための最適な組み合わせとその時の最小終了時間**を求める必要があります。

---

## 💡 アプローチ (Approach)

### 1. 全数調査（Brute Force）によるすべての組み合わせの探索
* **全体探索:** Land作業候補の配列とWater作業候補の配列を2重の`for`ループで巡回し、可能なすべての$(i, j)$の組み合わせを検査します。

### 2. 作業の重複の有無による終了時間の計算
各組み合わせごとに、2つの作業の時間帯が重なるかどうかを判断します。
* **場合 1: 2つの作業が重ならない場合 (`if`)**
  * 조건: `landFinishTime <= waterStartTime[j]` 또는 `waterFinishTime <= landStartTime[i]`
  * 1つの作業が終了し、別の作業が開始されるため、全体の終了時間は2つの作業の終了時間のうち大きい方が表示されます。 (`max(landFinishTime, waterFinishTime)`)
* **場合2: 2つの作業が重なる場合 (`else`)**
  * 2つの作業の時間帯が重なるため、1つの作業を他の作業が終わった後に延期する必要があります。
  * したがって、遅延したケースを考慮して計算した終了時間の中で最大値を求めます。

### 3. 最小値の更新
* 各組み合わせで計算された`FinishTime`の中で最も小さい値を`minFinishTime`に継続的に更新して最終返却します。

---

## ⏱️ 複雑性 (Complexity)

* **時間計算量 (Time Complexity):** $O(N \times M)$
  * `land 먼저`配列の長さを$N$、`waterStartTime`配列の長さを$M$とした場合、二重ループを通じてすべてのペアを確認するため、**$O(N \times M)$**の時間がかかります。
* **空間計算量 (Space Complexity):** $O(1)$
  * 入力配列以外に追加の配列やデータ構造を生成せず、変数（`landFinishTime`、`waterFinishTime`、`minFinishTime`など）をいくつかだけ使用するため、空間計算量は定数時間である**$O(1)$**です。

---

## 💻 コードの要点まとめ（Key Code）

```python
from typing import List

def earliestFinishTime(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int: 
    minFinishTime = 300000 # 十分に大きな値で初期化
    
    for i in range(len(landStartTime)):
        landFinishTime = landStartTime[i] + landDuration[i]
        
        for j in range(len(waterStartTime)):
            waterFinishTime = waterStartTime[j] + waterDuration[j]
            
            # 二つの作業が互いに重ならない場合
            if landFinishTime <= waterStartTime[j] or waterFinishTime <= landStartTime[i]:
                FinishTime = max(landFinishTime, waterFinishTime)
            # 二つの作業が重なり調整が必要な場合
            else:
                FinishTime = max(landFinishTime + waterDuration[j], waterFinishTime + landDuration[i]) 
                
            # 最小終了時間の更新
            minFinishTime = min(minFinishTime, FinishTime)   
    
    return minFinishTime