__author__ = 'rahul'


# Maximum subarray problem
# The maximum subarray problem is the task of finding the contiguous subarray within a one-dimensional array of numbers
# (containing atleast one positive number) which has the largest sum.
# e.g. sequence: -2, 1, -3, 4, -1, 2, 1, -5, 4
# output: 4, -1, 2, 1


def first_solution(sequence):
    if all(e < 0 for e in sequence):
        e = min(sequence)
        return e, [e]
    solution = []
    current_opt = 0, []
    for i, e in enumerate(sequence):
        if current_opt[0] + e <= 0:
            solution.append(current_opt)
            current_opt = 0, []
        else:
            current_opt = current_opt[0] + e, list(current_opt[1])
            current_opt[1].append(e)
            solution.append(current_opt)

    return max(solution, key=lambda x: (x[0], len(x[1])))


def main():
    s1 = (-2, 1, -3, 4, -1, 2, 1, -5, 4)
    result = first_solution(s1)[1]
    print result
    assert sum(result) == 6

    s2 = (-2, -1, -3, 4, -1, -2, -1, -5, -4)
    result = first_solution(s2)[1]
    print result
    assert sum(result) == 4


if __name__ == '__main__':
    main()

