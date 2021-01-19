from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
      '''
      keep a dict of ordered dict. whenever do a popping, pop the lowest frequency one.
      '''
      self.freq_dict = defaultdict(OrderedDict)
      self.capacity = capacity
      self.count = 0
      self.key_to_freq_dict = defaultdict(int)
      self.min_freq = 1



    def get(self, key: int) -> int:
      if key not in self.key_to_freq_dict:
        return -1
      freq = self.key_to_freq_dict[key]
      self.key_to_freq_dict[key] += 1
      value = self.freq_dict[freq].pop(key)
      self.freq_dict[freq + 1][key] = value
      if self.min_freq == freq and not self.freq_dict[freq]:
        self.min_freq += 1
      return value


    def put(self, key: int, value: int) -> None:
      # if key is already in key_to_frequency_dict, boost it to next frequency otherwise see if capacity is full and remove the lowest frequency one.
      if self.capacity == 0:
        return
      if key not in self.key_to_freq_dict:
        if self.count == self.capacity:
          key_to_pop, _ = self.freq_dict[self.min_freq].popitem(last=False)
          self.key_to_freq_dict.pop(key_to_pop)
          self.count -= 1
        self.key_to_freq_dict[key] = 1
        self.freq_dict[1][key] = value
        self.count += 1
        self.min_freq = 1
      else:
        freq = self.key_to_freq_dict[key]
        self.key_to_freq_dict[key] += 1
        self.freq_dict[freq].pop(key)
        self.freq_dict[freq + 1][key] = value
        if self.min_freq == freq and not self.freq_dict[freq]:
          self.min_freq += 1


def test():
  lfu = LFUCache(2)
  lfu.put(1, 1)
  lfu.put(2, 2)
  got = lfu.get(1)
  want = 1
  print('got: {}, want: {}'.format(got, want))
  lfu.put(3, 3)
  got = lfu.get(2)
  want = -1
  print('got: {}, want: {}'.format(got, want))
  got = lfu.get(3)
  want = 3
  print('got: {}, want: {}'.format(got, want))
  lfu.put(4, 4)
  got = lfu.get(1)
  want = -1
  print('got: {}, want: {}'.format(got, want))
  got = lfu.get(3)
  want = 3
  print('got: {}, want: {}'.format(got, want))
  got = lfu.get(4)
  want = 4
  print('got: {}, want: {}'.format(got, want))

test()



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)