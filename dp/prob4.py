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


def main():
    s1 = (1, 7, 4, 9, 2, 5)
    result = ZigZag.longest_zig_zag(s1)
    print len(result), result
    assert len(result) == 6

    s2 = (1, 17, 5, 10, 13, 15, 10, 5, 16, 8)
    result = ZigZag.longest_zig_zag(s2)
    print len(result), result
    assert len(result) == 7

    s3 = (44, )
    result = ZigZag.longest_zig_zag(s3)
    print len(result), result
    assert len(result) == 1

    s4 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    result = ZigZag.longest_zig_zag(s4)
    print len(result), result
    assert len(result) == 2

    s5 = (70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32)
    result = ZigZag.longest_zig_zag(s5)
    print len(result), result
    assert len(result) == 8

    s6 = (374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669,
          810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23,
          22, 617, 462, 459, 244)
    result = ZigZag.longest_zig_zag(s6)
    print len(result), result
    assert len(result) == 36

    s7 = (1, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2)
    result = ZigZag.longest_zig_zag(s7)
    print len(result), result
    assert len(result) == 7

    s8 = (1, 3, 2, 7, 3, 201, 200, 8, 13, 8, 13, 8)
    result = ZigZag.longest_zig_zag(s8)
    print len(result), result
    assert len(result) == 11


if __name__ == '__main__':
    main()