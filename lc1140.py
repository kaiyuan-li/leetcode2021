from typing import List
from functools import lru_cache
import math


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache
        def max_diff(pos, m):
            # how many more stones current player can take when starting at pos (included) and current m that can take.
            if pos + m * 2 >= len(piles):
                return sum(piles[pos:])
            res = -math.inf
            found = False
            for x in range(1, 2 * m + 1):
                if pos + x >= len(piles):
                    break
                found = True
                stones_taken = sum(piles[pos:(pos+x)])
                next_m = max(x, m)
                next_pos = pos + x
                next_max_diff = max_diff(next_pos, next_m)
                res = max(res, stones_taken - next_max_diff)
            return res if found else 0
        return (sum(piles) + max_diff(0, 1)) // 2


def test():
    s = Solution()
    test_data = [
        ([1, 1, 100], 2),
        ([2, 7, 9, 4, 4], 10),
        ([1, 2, 3, 4, 5, 100], 104)
    ]
    for piles, want in test_data:
        got = s.stoneGameII(piles)
        print('got: {}, want: {}'.format(got, want))


test()
