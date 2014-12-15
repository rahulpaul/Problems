import collections

__author__ = 'rahul'


# Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. Find the minimum number of coins the
# sum of which is S (we can use as many coins of one type as we want), or report that it's not possible to select coins
# in such a way that they sum up to S.

# For a better understanding let's take this example:
# Given coins with values 1, 3, and 5.
# And the sum S is set to be 11.

# http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=dynProg

def first_solution(denominations, target_sum):
    solution = {0: (0, None)}
    denominations = sorted(denominations)

    for s in xrange(1, target_sum + 1):
        for d in denominations:
            if d <= s:
                current_solution = solution.get(s)
                new_solution = 1 + solution.get(s-d)[0] if solution.get(s-d) is not None else None

                if not (current_solution is None or new_solution is None):
                    if new_solution < current_solution:
                        solution[s] = (new_solution, s - d)

                elif new_solution is not None:
                    solution[s] = (new_solution, s-d)
            else:
                break

    num_denoms = solution.get(target_sum)[0] if solution.get(target_sum) else -1
    denom_counter = get_denom_list_from_solution(solution, target_sum) if solution.get(target_sum) else None
    return num_denoms, denom_counter


def get_denom_list_from_solution(solution_dict, target_sum):
    denoms_list = []
    current_state = target_sum
    while current_state > 0:
        prev_state = solution_dict[current_state][1]
        denom = current_state - prev_state
        denoms_list.append(denom)
        current_state = prev_state

    return collections.Counter(denoms_list)


def main():
    denom_list = [3, 7]
    target_sum = 13
    print first_solution(denom_list, target_sum)


if __name__ == '__main__':
    main()

