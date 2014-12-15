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


def alternate_solution(a):
    sol = {}  # key is index value is solution ending with element of that index
    optimal_sol = []
    for i, e in enumerate(a):
        s = None
        for j in range(i):
            if e >= sol[j][-1]:
                new_s = 1 + len(sol[j]), j
                if s is None or new_s[0] > s[0]:
                    s = new_s
        if s is None:
            sol[i] = [e]
        else:
            sol[i] = list(sol[s[1]])
            sol[i].append(e)

        if len(optimal_sol) < len(sol[i]):
            optimal_sol = sol[i]

    return optimal_sol


def main():
    a1 = (5, 3, 4, 8, 6, 7)
    s1 = first_solution(a1)
    s2 = alternate_solution(a1)
    assert s1 == s2
    print s1
    print s2

    a2 = (0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15)
    s1 = first_solution(a2)
    s2 = alternate_solution(a2)
    assert s1 == s2
    print s1
    print s2


if __name__ == '__main__':
    main()
