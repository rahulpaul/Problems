""" https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

import heapq
import functools
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
@functools.total_ordering
class NodeValue(NamedTuple):
    val: int
    node: ListNode
    
    def __lt__(self, other):
        return self.val < other.val
    
    
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        arr = []
        
        for node in lists:
            if node:
                heapq.heappush(arr, NodeValue(node.val, node))
        
        if len(arr) == 0:
            return None
        
        val, node = heapq.heappop(arr)
        node = node.next
        if node:
            heapq.heappush(arr, NodeValue(node.val, node))
        
        start = current = ListNode(val)
        while len(arr) > 0:
            val, node = heapq.heappop(arr)
            current.next = ListNode(val)
            current = current.next
            
            node = node.next
            if node:
                heapq.heappush(arr, NodeValue(node.val, node))
        
        return start
