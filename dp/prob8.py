# Square Subsequences

# A string is called a square string if it can be obtained by concatenating two copies of the same string. 
# For example, "abab", "aa" are square strings, while "aaa", "abba" are not. Given a string, how many (non-empty) 
# subsequences of the string are square strings? A subsequence of a string can be obtained by deleting zero or 
# more characters from it, and maintaining the relative order of the remaining characters.

# Sample Input

# 3 
# aaa 
# abab 
# baaba

# Sample Output

# 3 
# 3 
# 6

# Explanation

# For the first case, there are 3 subsequences of length 2, all of which are square strings. 
# For the second case, the subsequences "abab", "aa", "bb" are square strings. 
# Similarly, for the third case, "bb", "baba" (twice), and "aa" (3 of them) are the square subsequences.

# Sample Input

# 20
# dlcgdewhtaciohordt
# vwcsgspqoqmsboaguwn
# qxnzlgdgwpb
# wblnsadeuguumoqcdrub
# okyxhoac
# dvmxxrd
# xlmnd
# ukwagmle
# ukwcibxubum
# meyatdrmydiajx
# ghiqfmzhlvihjouvs
# oyp
# ulyeimuot
# zrii
# skpggkbb
# zzrz
# xamludf
# g
# o
# giooobpp

# Sample Output

# 17
# 12
# 1
# 12
# 1
# 2
# 0
# 0
# 6
# 11
# 11
# 0
# 1
# 1
# 3
# 3
# 0
# 0
# 0
# 4



from collections import namedtuple
from collections import defaultdict


Solution = namedtuple('Solution', ['one_end', 'two_start'])


class IndexFinder:
    
    def __init__(self, seq):
        self.d = defaultdict(list)
        for i, c in enumerate(seq):
            self.d[c].append(i)
    
    def yield_all_index(self, c, i, j):
        for idx in self.d[c]:
            if idx < i:
                continue
            elif idx >= j:
                break
            else:
                yield idx


def find_all(seq):
    solution_dict = {}
    idx_finder = IndexFinder(seq)
    for i, c in enumerate(seq):
        i_solns = []        
        for j in range(i):
            if c == seq[j]:
                i_solns.append(Solution(j, i))
            j_solns = solution_dict[j]
            for j_soln in j_solns:
                for idx in idx_finder.yield_all_index(c, j_soln.one_end + 1, j_soln.two_start):                    
                    i_solns.append(Solution(idx, j_soln.two_start))                
        
        solution_dict[i] = i_solns
    
    solutions = 0
    for soln_list in solution_dict.values():
        solutions += len(soln_list)            
    return solutions

                  
def main():
    import sys
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        print(find_all(sys.stdin.readline().rstrip()))


if __name__ == '__main__':
    main()