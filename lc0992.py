'''
create a sliding window with two endings, the first ending will be just K different integers, the second ending will be also K differnet integers.
K = 2
e.g. [1, 2, 1, 1, 3]
the first ending will be at index 1 and the second ending will be at 3. Then I know for this window (starting at index 0) the number of subarrays will be 3 - 1 + 1 = 3.
Keep sliding the window.
'''
from collections import defaultdict
def count_subarrays(arr, K):
  left, right1, right2 = 0, 0, 0
  n_long, n_short = 0, 0
  counter_long = defaultdict(int)
  counter_short = defaultdict(int)
  res = 0
  for left in range(len(arr)):
    while right1 < len(arr) and n_short < K:
      counter_short[arr[right1]] += 1
      if counter_short[arr[right1]] == 1:
        n_short += 1
      right1 += 1

    while right2 < len(arr) and n_long < K + 1:
      counter_long[arr[right2]] += 1
      if counter_long[arr[right2]] == 1:
        n_long += 1
      right2 += 1
    res += right2 - right1
    counter_short[arr[left]] -= 1
    if counter_short[arr[left]] == 0:
      n_short -= 1
    counter_long[arr[left]] -= 1
    if counter_long[arr[left]] == 0:
      n_long -= 1
  return res

arr = [1, 2, 1, 1, 3]

print(count_subarrays(arr, 2))
