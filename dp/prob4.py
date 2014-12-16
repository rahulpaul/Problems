__author__ = 'rahul'


# Problem Statement
#
# A sequence of numbers is called a zig-zag sequence if the differences between successive numbers strictly alternate
# between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence
# with fewer than two elements is trivially a zig-zag sequence.
#
# For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences (6,-3,5,-7,3) are alternately positive and
# negative. In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences, the first because its first two differences
# are positive and the second because its last difference is zero.
#
# Given a sequence of integers, sequence, return the length of the longest subsequence of sequence that is a zig-zag
# sequence. A subsequence is obtained by deleting some number of elements (possibly zero) from the original sequence,
# leaving the remaining elements in their original order.
#
#
# Definition
#
# Class:	ZigZag
# Method:	longestZigZag
# Parameters:	int[]
# Returns:	int
# Method signature:	int longestZigZag(int[] sequence)
# (be sure your method is public)
#
#
#Constraints
#-	sequence contains between 1 and 50 elements, inclusive.
#-	Each element of sequence is between 1 and 1000, inclusive.
#
#Examples
#0)
#
#{ 1, 7, 4, 9, 2, 5 }
#Returns: 6
#The entire sequence is a zig-zag sequence.
#1)
#
#{ 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 }
#Returns: 7
#There are several subsequences that achieve this length. One is 1,17,10,13,10,16,8.
#2)
#
#{ 44 }
#Returns: 1
#3)
#
#{ 1, 2, 3, 4, 5, 6, 7, 8, 9 }
#Returns: 2
#4)
#
#{ 70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32 }
#Returns: 8
#5)
#
#{ 374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
#600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
#67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
#477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
#249, 22, 176, 279, 23, 22, 617, 462, 459, 244 }
#Returns: 36


class ZigZag(object):

    @staticmethod
    def longest_zig_zag(sequence):
        solution = {}
        for i, e in enumerate(sequence):

            if i == 0:
                solution[i] = [sequence[0]]
                continue

            for j in xrange(i - 1, -1, -1):

                # determine if we can move from state j to state i
                can_move_from_j_to_i = False

                if len(solution[j]) == 1 and e != solution[j][0]:
                    can_move_from_j_to_i = True
                elif (solution[j][-1] - solution[j][-2]) * (e - solution[j][-1]) < 0:
                    can_move_from_j_to_i = True

                if can_move_from_j_to_i:
                    new_solution = list(solution[j])
                    new_solution.append(e)
                    solution[i] = new_solution
                    break
            else:
                # we were not able to move to state i from any of the previous states
                # so state[i] = state[i - 1]
                solution[i] = list(solution[i - 1])

        return max(solution.itervalues(), key=lambda x: len(x))


def alternate_solution(a):
    sol = {}
    for i, e in enumerate(a):
        sol[i] = [e]
        for j in xrange(i):
            if is_admissible(sol[j], e) and ((1 + len(sol[j])) > len(sol[i])):
                sol[i] = list(sol[j])
                sol[i].append(e)
    return max(sol.itervalues(), key=len)


def is_admissible(s, e):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return s[0] != e
    d1 = s[-1] - s[-2]
    d2 = e - s[-1]
    return d1 * d2 < 0


def main():
    s1 = (1, 7, 4, 9, 2, 5)
    r11 = ZigZag.longest_zig_zag(s1)
    r12 = alternate_solution(s1)
    assert len(r11) == len(r12)
    print len(r11), r11


    s2 = (1, 17, 5, 10, 13, 15, 10, 5, 16, 8)
    r21 = ZigZag.longest_zig_zag(s2)
    r22 = alternate_solution(s2)
    assert len(r21) == len(r22)
    print len(r21), r21

    s3 = (44, )
    r31 = ZigZag.longest_zig_zag(s3)
    r32 = alternate_solution(s3)
    assert len(r31) == len(r32)
    print len(r31), r31

    s4 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    r41 = ZigZag.longest_zig_zag(s4)
    r42 = alternate_solution(s4)
    assert len(r41) == len(r42)
    print len(r41), r41

    s5 = (70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32)
    r51 = ZigZag.longest_zig_zag(s5)
    r52 = alternate_solution(s5)
    assert len(r51) == len(r52)
    print len(r51), r51

    s6 = (374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669,
          810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23,
          22, 617, 462, 459, 244)
    r61 = ZigZag.longest_zig_zag(s6)
    r62 = alternate_solution(s6)
    assert len(r61) == len(r62)
    print len(r61), r61

    s7 = (1, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2)
    r71 = ZigZag.longest_zig_zag(s7)
    r72 = alternate_solution(s7)
    assert len(r71) == len(r72)
    print len(r71), r71

    s8 = (1, 3, 2, 7, 3, 201, 200, 8, 13, 8, 13, 8)
    r81 = ZigZag.longest_zig_zag(s8)
    r82 = alternate_solution(s8)
    assert len(r81) == len(r82)
    print len(r81), r81


if __name__ == '__main__':
    main()