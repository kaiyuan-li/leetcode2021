from typing import List
from typing import List
from collections import Counter
from functools import lru_cache
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], scores: List[int]) -> int:
        '''
        eight queens problem, if can place, place, otherwise, don't place
        '''
        @lru_cache
        def get_score(word):
            return sum([scores[ord(ch) - ord('a')] for ch in word])


        def try_place(word_idx, counts):
            '''
            args:
                word_idx: index of word
                counts: tuple of 26 allowed count
            returns:
                new_count_left, score, can_place
            '''
            word = words[word_idx]
            c = Counter(word)
            new_counts = list(counts)
            for ch, count in c.items():
                idx = ord(ch) - ord('a')
                if new_counts[idx] < count:
                    return None, None, False
                new_counts[idx] -= count
            return tuple(new_counts), get_score(word), True

        # count left is a tuple of 26 ints, -1 means unlimited
        @lru_cache
        def max_score(p, count_left):
            # returns the maximum score that can be achieved from position p and counts left.
            if p == len(words):
                return 0
            res = max_score(p + 1, count_left)
            new_count_left, score, can_place = try_place(p, count_left)
            if can_place:
                res = max(res, score + max_score(p + 1, new_count_left))
            return res
        counts = [0] * 26
        for ch in letters:
            idx = ord(ch) - ord('a')
            counts[idx] += 1
        return max_score(0, tuple(counts))

def test():
  words = ["dog","cat","dad","good"]
  letters = ["a","a","c","d","d","d","g","o","o"]
  scores = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
  s = Solution()
  got = s.maxScoreWords(words, letters, scores)
  want = 23
  print('got: {}, want: {}'.format(got, want))


test()