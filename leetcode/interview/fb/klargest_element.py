"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

from typing import List

"""Maintain a min heap internally, of a specified max size
"""
class KLargestHolder:
    
    def __init__(self, max_size: int):
        self.size = 0
        self.max_size = max_size
        self.data = [None for _ in range(max_size)]
    
    def peak(self):
        return self.data[0]
    
    def add(self, x: int):
        if self.size < self.max_size:
            self.data[self.size] = x
            self.size += 1
            self._heapify_up(self.size - 1)
        elif self.data[0] < x:
            self.data[0] = x
            self._heapify_down(0)
    
    def _heapify_up(self, index):
        if not self._has_parent(index):
            return 
        parent = self._parent_idx(index)
        if self.data[parent] > self.data[index]:
            self._swap(parent, index)
            self._heapify_up(parent)
    
    def _heapify_down(self, index):
        child_idx = None
        if self._has_right_child(index):
            child_idx = self._right_child_idx(index)
        if self._has_left_child(index):
            left_child_idx = self._left_child_idx(index)
            if (child_idx is None) or (self.data[left_child_idx] < self.data[child_idx]):
                child_idx = left_child_idx
        
        if child_idx is None:
            return
        
        if self.data[index] > self.data[child_idx]:
            self._swap(index, child_idx)
            self._heapify_down(child_idx)
                
    
    def _swap(self, i1, i2):
        self.data[i1], self.data[i2] = self.data[i2], self.data[i1]
    
    def _has_parent(self, x: int):
        return self._parent_idx(x) >= 0
    
    def _has_left_child(self, x: int):
        idx = self._left_child_idx(x)
        if idx >= self.max_size:
            return False
        return self.data[idx] is not None
    
    def _has_right_child(self, x: int):
        idx = self._right_child_idx(x)
        if idx >= self.max_size:
            return False
        return self.data[idx] is not None
    
    def _parent_idx(self, x: int):
        if x % 2 == 0:
            # is right child
            return (x - 2) // 2
        else:
            # is left child
            return (x - 1) // 2
    
    def _left_child_idx(self, x: int):
        return x*2 + 1
    
    def _right_child_idx(self, x: int):
        return x*2 + 2


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = KLargestHolder(k)
        for n in nums:
            heap.add(n)
        
        return heap.peak()