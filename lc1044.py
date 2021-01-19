from functools import lru_cache
class Solution:
    def longestDupSubstring(self, s: str) -> str:
      @lru_cache
      def find_dupe(length):
        # find duplicated string with length
        seen = set()
        for start in range(len(s) - length + 1):
          substring = s[start:start+length]
          if substring in seen:
            return substring
          seen.add(substring)
        return ''


      l, r = 0, len(s) - 1
      dupe = None
      while l != r:
        mid = (l + r + 1) // 2
        dupe = find_dupe(mid)
        if dupe:
          l = mid
        else:
          r = mid - 1
      return find_dupe(l)

def test():
  s = Solution()
  data = 'banana'
  want = 'ana'
  print('want: {}, got {}'.format(want, s.longestDupSubstring(data)))

test()