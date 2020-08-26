""" https://leetcode.com/problems/all-oone-data-structure/

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
"""

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_dict = {}
        self.value_to_keys = {}
        self.min_value = None
        self.max_value = None
    
    def on_value_added(self, value):
        if self.max_value is None or value > self.max_value:
            self.max_value = value
        
        if self.min_value is None or value < self.min_value:
            self.min_value = value
    
    def on_value_removed(self, value):
        if self.max_value == value:
            self.max_value = max(self.value_to_keys.keys()) if self.value_to_keys else None
        elif self.min_value == value:
            self.min_value = min(self.value_to_keys.keys()) if self.value_to_keys else None
    
    def add_to_value_tracker(self, key, value):
        if value not in self.value_to_keys:
            self.value_to_keys[value] = { key }
            self.on_value_added(value)
        else:
            self.value_to_keys[value].add(key)
    
    def remove_from_value_tracker(self, key, value):
        key_set = self.value_to_keys[value]
        key_set.remove(key)
        if not key_set:
            del self.value_to_keys[value]
            self.on_value_removed(value)

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.data_dict:
            self.data_dict[key] = 1
            self.add_to_value_tracker(key, 1)
        else:
            value = self.data_dict[key]
            self.data_dict[key] = value + 1
            
            self.remove_from_value_tracker(key, value)
            self.add_to_value_tracker(key, value + 1)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.data_dict:
            value = self.data_dict[key]
            if value == 1:
                del self.data_dict[key]
            else:
                self.data_dict[key] = value - 1
                self.add_to_value_tracker(key, value - 1)
            
            self.remove_from_value_tracker(key, value)

                
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.max_value is None:
            return ""
        return next(iter(self.value_to_keys[self.max_value]))
        
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.min_value is None:
            return ""
        return next(iter(self.value_to_keys[self.min_value]))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()