from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

      '''
      merge sort
      '''
      def merge_sort(arr):
        if len(arr) < 2:
          return arr
        length = len(arr)
        left = merge_sort(arr[:length // 2])
        right = merge_sort(arr[length//2:])
        res = [None] * length
        p, q, r = len(left) - 1, len(right) - 1, length - 1
        while r >= 0:
          if q == -1:
            res[r] = left[p]
            p -= 1
          elif p == -1:
            res[r] = right[q]
            q -= 1
          else:
            if left[p][0] > right[q][0]:
              res[r] = left[p]
              p -= 1
              res[r][2] += q + 1

            else:
              res[r] = right[q]
              q -= 1
          r -= 1
        return res



      arr = [[n, idx, 0] for idx, n in enumerate(nums)]  # the third is number smaller

      arr = merge_sort(arr)

      res = [0] * len(nums)

      for _, idx, smaller in arr:
        res[idx] = smaller
      return res

def test():
  s = Solution()
  data = [
    [[-1, -1], [0, 0]],
    [[5,2,6,1], [2, 1, 1, 0]]
  ]
  for inp, exp in data:
    print('got: {}, exp: {}'.format(s.countSmaller(inp), exp))

test()