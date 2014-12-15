__author__ = 'rahul'


# Given a sequence of N numbers - A[1] , A[2] , ..., A[N] . Find the length of the longest non-decreasing sequence.
# e.g. sequence: 5, 3, 4, 8, 6, 7
# result = 4 -> 3, 4, 6, 7

# http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=dynProg


def first_solution(sequence):
    solution = {}  # key is the index and value is a sequence that corresponds to the best solution till that index

    # At first we initialize it with a solution of 1, which consists only of the i-th number itself.
    for idx, n in enumerate(sequence):
        solution[idx] = [n]

    for i, n in enumerate(sequence):
        for j in xrange(0, i):
            # determine if we can pass from state j to state i
            if solution[j][-1] <= n:

                if 1 + len(solution[j]) > len(solution[i]):
                    solution[i] = list(solution[j])
                    solution[i].append(n)

    return max(solution.itervalues(), key=lambda x: len(x))


def main():
    s1 = (5, 3, 4, 8, 6, 7)
    print s1, first_solution(s1)
    s2 = (0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15)
    print s2, first_solution(s2)


if __name__ == '__main__':
    main()
