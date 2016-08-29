__author__ = 'rahul'


# Problem Statement
#
# The old song declares "Go ahead and hate your neighbor", and the residents of Onetinville have taken those words to
# heart. Every resident hates his next-door neighbors on both sides. Nobody is willing to live farther away from the
# town's well than his neighbors, so the town has been arranged in a big circle around the well. Unfortunately, the
# town's well is in disrepair and needs to be restored. You have been hired to collect donations for the Save Our Well
# fund.
#
# Each of the town's residents is willing to donate a certain amount, as specified in the int[] donations, which is
# listed in clockwise order around the well. However, nobody is willing to contribute to a fund to which his neighbor
# has also contributed. Next-door neighbors are always listed consecutively in donations, except that the first and last
# entries in donations are also for next-door neighbors. You must calculate and return the maximum amount of donations
# that can be collected.
#
#
# Definition
#
# Class:	BadNeighbors
# Method:	maxDonations
# Parameters:	int[]
# Returns:	int
# Method signature:	int maxDonations(int[] donations)
# (be sure your method is public)
#
#
# Constraints
# -	donations contains between 2 and 40 elements, inclusive.
# -	Each element in donations is between 1 and 1000, inclusive.
#
#Examples
#0)
#
# { 10, 3, 2, 5, 7, 8 }
#Returns: 19
# The maximum donation is 19, achieved by 10+2+7. It would be better to take 10+5+8 except that the 10 and 8 donations
# are from neighbors.
#1)
#
#{ 11, 15 }
#Returns: 15
#2)
#
#{ 7, 7, 7, 7, 7, 7, 7 }
#Returns: 21
#3)
#
#{ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 }
#Returns: 16
#4)
#
#{ 94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
#  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
#  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 }
#Returns: 2926




from collections import namedtuple


Solution = namedtuple('Solution', ['total_donation', 'donators'])


def _compute_max_donation_ij(donations, j_solution, i, i_donation, is_i_last):
    """
    Returns the max possible donation including i
    """
    if (0 in j_solution.donators) and is_i_last:
        return j_solution.total_donation - donations[0] + i_donation
    return j_solution.total_donation + i_donation


def _compute_max_solution_ij(donations, j_solution, i, i_donation, is_i_last):
    """
    Returns the optimal solution including i
    """
    if (0 in j_solution.donators) and is_i_last:
        return Solution(j_solution.total_donation - donations[0] + i_donation, j_solution.donators[1:] + [i])
    return Solution(j_solution.total_donation + i_donation, j_solution.donators + [i])


def max_donations(donations):
    solutions_dict = {}
    for i, donation in enumerate(donations):
        if i - 2 < 0:
            solutions_dict[i] = Solution(donation, [i])
        else:
            i_solution = Solution(donation, [i])
            is_i_last = (i == len(donations) - 1)
            for j in range(i-1):
                ij_donation = _compute_max_donation_ij(donations, solutions_dict[j], i, donation, is_i_last)                
                if ij_donation > i_solution.total_donation:                    
                    i_solution = _compute_max_solution_ij(donations, solutions_dict[j], i, donation, is_i_last)
            solutions_dict[i] = i_solution
    return max(solutions_dict.values(), key=lambda soln : soln.total_donation)


def main():
    sep = '======================================================='
    d1 = [10, 3, 2, 5, 7, 8]
    print('expected optimal donation = {}\ndonations = {}'.format(19, d1))
    print(max_donations(d1))
    print(sep)

    d2 = [11, 15]
    print('expected optimal donation = {}\ndonations = {}'.format(15, d2))
    print(max_donations(d2))
    print(sep)

    d3 = [7, 7, 7, 7, 7, 7, 7]
    print('expected optimal donation = {}\ndonations = {}'.format(21, d3))
    print(max_donations(d3))
    print(sep)

    d4 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print('expected optimal donation = {}\ndonations = {}'.format(16, d4))
    print(max_donations(d4))
    print(sep)

    d5 = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 
          265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
    print('expected optimal donation = {}\ndonations = {}'.format(2926, d5))
    print(max_donations(d5))
    print(sep)



if __name__ == '__main__':
    main()
