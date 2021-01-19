from functools import lru_cache


class Solution:
    def racecar(self, target: int) -> int:
      '''
      move means 1, 2, 4, 8, ... so it's adding steps of binary number B1111... steps.
      Try two options: go just beyonde the target and turn back, or go just before the target and try to go back a few steps and move forward to target.
      '''
      @lru_cache
      def get_best_steps(target):
        if target == 0:
          return 0
        # get the highest bit in binary format
        bits = 0
        tmp = target
        while tmp:
          tmp = tmp >> 1
          bits += 1
        # try go beyond/at target and turn back once to cover the rest of distance
        distance = (1 << bits) - 1
        if distance == target:
          return bits
        best = get_best_steps(distance - target) + 1 + bits

        # try to go to the nearest point first and go back n steps
        distance = (1 << (bits - 1)) - 1
        for n in range(0, bits-1):
          back_distance = (1 << n) - 1
          # we have moved (bits - 1) steps forward, turn back, n steps backward, turn back
          curr_best = bits - 1 + 1 + n + 1 + get_best_steps(target - distance + back_distance)
          best = min(best, curr_best)
        return best

      return get_best_steps(target)

def test():
  s = Solution()
  target = 6
  want = 5
  got = s.racecar(target)
  print('got: {}, want: {}'.format(got, want))

test()