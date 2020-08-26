""" https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""


from typing import List

def shortest_subarray(arr, k):
    n = len(arr)
    output = {}
    for i in range(n):
        sum_ = 0
        for j in range(i, -1, -1):
            sum_ += arr[j]
            if sum_ >= k:
                output[i] = 1 + (i - j)
                break
    print(output)
    return min(output.values()) if output else -1


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        return shortest_subarray(A, K)


def main():
    arr = [2,1,3,5,-1,1,6,5,2]
    assert shortest_subarray(arr, 8) == 2
    assert shortest_subarray(arr, 11) == 2
    assert shortest_subarray(arr, 12) == 3

if __name__ == "__main__":
    main()
