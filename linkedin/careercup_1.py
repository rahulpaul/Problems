import collections

__author__ = 'rahul'


#Find the maximum sum subset in an array with negative integers

def find_max_subarray(arr):
    """
    To find maximum sum of continuous subsequence: keep summing up numbers and record maximum sum.
    If the sum is negative, reset it to be 0.
    """
    opt_sum, opt_start_idx, opt_stop_idx = 0, -1, -1
    curr_sum, curr_start_idx, curr_stop_idx = 0, -1, -1

    for index, num in enumerate(arr):
        if curr_sum == 0:
            curr_start_idx = index
        if curr_sum + num <= 0:
            curr_sum = 0
            continue
        curr_sum += num
        if curr_sum > opt_sum:
            opt_sum = curr_sum
            opt_start_idx = curr_start_idx
            opt_stop_idx = index

    return opt_sum, opt_start_idx, opt_stop_idx

#Given a sorted array with duplicates and a number, find the range in the
#form of (startIndex, endIndex) of that number. For example,
#
#find_range({0 2 3 3 3 10 10}, 3) should return (2,4).
#find_range({0 2 3 3 3 10 10}, 6) should return (-1,-1).
#The array and the number of duplicates can be large.


def find_range(num_list, search_num):

    def find_range_internal(l_index, r_index):
        if l_index > r_index:
            return -1, -1
        if l_index == r_index:
            return (l_index, r_index) if num_list[l_index] == search_num else (-1, -1)
        mid_index = (l_index + r_index) / 2
        mid_result = mid_index if num_list[mid_index] == search_num else -1
        l_result = (-1, -1) if num_list[mid_index] < search_num else find_range_internal(l_index, mid_index - 1)
        r_result = (-1, -1) if num_list[mid_index] > search_num else find_range_internal(mid_index + 1, r_index)

        result = []
        result.extend(l_result)
        result.append(mid_result)
        result.extend(r_result)

        result = [i for i in result if i != -1]
        if result:
            return result[0], result[-1]
        return -1, -1

    return find_range_internal(0, len(num_list) - 1)


#Returns a^b, as the standard mathematical exponentiation function
#Interviewer looking for log(n) solution, right on first attempt.

def custom_pow(a, b):
    if b < 0:
        return 1.0 / custom_pow(a, -b)
    exponent_to_value_map = collections.OrderedDict()
    current_exponent = 1
    current_value = a
    exponent_to_value_map[current_exponent] = current_value
    while 2 * current_exponent < b:
        current_exponent *= 2
        current_value = current_value * current_value
        exponent_to_value_map[current_exponent] = current_value
    residual_exponent = b - current_exponent
    while residual_exponent != 0:
        tmp_exp, tmp_val = 0, 1
        for exponent, value in exponent_to_value_map.iteritems():
            if exponent <= residual_exponent:
                tmp_exp = exponent
                tmp_val = value
            else:
                break
        residual_exponent -= tmp_exp
        current_value *= tmp_val
    return current_value

# Generate all permutations of given sequence of elements.
# Return a list of all distinct permutations.


def permutations(s):
    pass

#You have two arrays of integers, where the integers do not repeat and the two arrays have no common integers.
#Let x be any integer in the first array, y any integer in the second. Find min(Abs(x-y)).
# That is, find the smallest difference between any of the integers in the two arrays.
#Assumptions: Assume both arrays are sorted in ascending order.


def find_smallest_diff(list_1, list_2):
    def get_next_indices(l1, l2, idx1, idx2):
        # assumption, idx1 < len(l1) and idx2 < len(l2)
        if idx1 == (len(l1) - 1) and idx2 == (len(l2) - 1):
            return None
        current_diff = abs(list_1[idx1] - list_2[idx2])
        if idx1 == len(l1) - 1:
            return (idx1, idx2 + 1) if current_diff > abs(list_1[idx1] - list_2[idx2 + 1]) else None
        if idx2 == len(l2) - 1:
            return (idx1 + 1, idx2) if current_diff > abs(list_1[idx1 + 1] - list_2[idx2]) else None
        # here we perform a greedy operation
        # we increment idx1 or idx depending on whichever results in a smaller diff
        l1_jump_diff = abs(l1[idx1 + 1] - l2[idx2])
        l2_jump_diff = abs(l2[idx2 + 1] - l1[idx1])
        return (idx1 + 1, idx2) if l1_jump_diff < l2_jump_diff else (idx1, idx2 + 1)
    i, j = 0, 0
    min_diff = abs(list_1[i] - list_2[j])
    min_idx_list_1, min_idx_list_2 = i, j
    while True:
        if min_diff > abs(list_1[i] - list_2[j]):
            min_diff = abs(list_1[i] - list_2[j])
            min_idx_list_1, min_idx_list_2 = i, j
        next_indices = get_next_indices(list_1, list_2, i, j)
        if not next_indices:
            break
        else:
            i, j = next_indices
            print i, j

    return min_diff, min_idx_list_1, min_idx_list_2


if __name__ == '__main__':
    #print find_range([0, 2, 2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 5, 10, 10], 3)
    #print custom_pow(-2, -1)
    print find_smallest_diff([1,3,7,20,31], [5,16,19,25,37])
