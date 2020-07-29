"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

The solution set must not contain duplicate quadruplets.

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

from typing import List


class TwoSumSolver:
    
    def __init__(self):
        pass
    
    def solve(self, nums: List[int], target: int) -> List[List[int]]:
        results = set()
        i, j = 0, len(nums) - 1
        while i < j:
            value = nums[i] + nums[j]
            if value == target:
                results.add((nums[i], nums[j]))
                i += 1
                j -= 1
            elif value < target:
                i += 1
            else:
                j -= 1
        
        return results


class FourSumSolver:
    
    def __init__(self):
        pass
    
    def solve(self, nums: List[int], target: int) -> List[List[int]]:
        results = set()
        i, j = 0, len(nums) - 1
        for i in range(len(nums)-3):
            for j in range(i+3, len(nums)):
                solver = TwoSumSolver()
                two_sum_target = target - (nums[i] + nums[j])
                two_solver_results = solver.solve(nums[i + 1: j], two_sum_target)
                for result in two_solver_results:
                    results.add((nums[i], *result, nums[j]))
        
        return results
    


class Solution:
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        solver = FourSumSolver()
        return solver.solve(sorted_nums, target)
                
        