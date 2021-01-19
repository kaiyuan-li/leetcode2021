from typing import List
from collections import defaultdict

class TrieNode:
  def __init__(self, parent=None):
    self.parent = parent
    self.children = defaultdict(lambda:TrieNode(parent=self))

    # top 3 dictionary words
    self.top3 = {}

    # freq is non-zero if only is end
    self.freq = 0
    self.is_end = False

class AutocompleteSystem:
  def _insert(self, word, freq):
    node = self.trie
    for ch in word:
      node = node.children[ch]
    node.is_end = True
    node.freq += freq

    new_freq = node.freq
    while node:
      if word in node.top3 or len(node.top3) < 3:
        node.top3[word] = new_freq
      else:
        mi_freq, mi_word = min([(freq, word) for word,freq in node.top3.items()])
        if mi_freq > new_freq:
          break  # there are three more frequent words than this one
        node.top3.pop(mi_word)
        node.top3[word] = new_freq
      node = node.parent


  def __init__(self, sentences: List[str], freq: List[int]):
    self.curr_word = ''
    self.trie = TrieNode()
    self.curr_node = self.trie
    self.in_trie = True  # whether current input char is still in the trie
    for word, freq in zip(sentences, freq):
      self._insert(word, freq)


  def input(self, c: str) -> List[str]:
    if c == '#':
      self._insert(self.curr_word, 1)
      self.curr_word = ''
      self.in_trie = True
      self.curr_node = self.trie
      return
    self.curr_word += c
    if self.in_trie and c in self.curr_node.children:
      self.curr_node = self.curr_node.children[c]
    else:
      self.in_trie = False
    if self.in_trie:
      return self.curr_node.top3.keys()

def test():
  words, freqs = [["i love you","island","iroman","i love leetcode"],[5,3,2,2]]
  acs = AutocompleteSystem(words, freqs)
  inputs = 'i a#i a#i a#'
  for ch in inputs:
    print(acs.input(ch))

test()

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)