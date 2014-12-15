__author__ = 'rahul'


"""
LONGEST INCREASING SUBSEQUENCE
The input is a sequence of numbers a(1), a(2), a(3), a(4) .... , a(n)
A subsequence is any subset of these numbers taken in order, of the form a(i1), a(i2), ... a(ik),
where 1 <= i1 < i2 < .... < ik <= n, and an increasing sunsequence is one in which the numbers are getting
strictly larger. The task is to find the increasing subsequence of greatest length. For e.g. the longest
increasing subsequence of 5,2,8,6,3,6,9,7 is 2,3,6,9
"""


def longest_increasing_subsequence(l):
    # the keys range from [0, n) and the value is the longest increasing subsequence ending at the key index
    m = {}
    for i, e in enumerate(l):
        pass
