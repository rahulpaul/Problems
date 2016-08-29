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


Solution = namedtuple('Solution', ['sequence', 'one_end', 'two_start'])


def all_index_of_char_in_str(c, seq):
    for i, c_dash in enumerate(seq):
        if c == c_dash:
            yield  i
        

def find_all(seq):
    solution_dict = {}
    for i, c in enumerate(seq):
        i_solns = []        
        for j in range(i):
            if c == seq[j]:
                i_solns.append(Solution(c, j, i))
            j_solns = solution_dict[j]
            for j_soln in j_solns:
                for idx in all_index_of_char_in_str(c, seq[j_soln.one_end + 1 : j_soln.two_start]):
                    idx = idx + j_soln.one_end + 1  # Converting to the absolute index
                    i_solns.append(Solution(j_soln.sequence + c, idx, j_soln.two_start))                
        
        solution_dict[i] = i_solns
    
    solutions = []
    for soln_list in solution_dict.values():
        for soln in soln_list:            
            solutions.append(soln.sequence * 2)
    return solutions


def main():
    inputs = ['dlcgdewhtaciohordt', 'vwcsgspqoqmsboaguwn', 'qxnzlgdgwpb', 'wblnsadeuguumoqcdrub', 'okyxhoac', 'dvmxxrd', 'xlmnd', 'ukwagmle', 
              'ukwcibxubum', 'meyatdrmydiajx', 'ghiqfmzhlvihjouvs', 'oyp', 'ulyeimuot', 'zrii', 'skpggkbb', 'zzrz', 'xamludf', 'g', 'o', 'giooobpp']
    outputs = [17, 12, 1, 12, 1, 2, 0, 0, 6, 11, 11, 0, 1, 1, 3, 3, 0, 0, 0, 4]
    sep = '############################################################'
    for input, output in zip(inputs, outputs):
        actual_output = len(find_all(input))
        assert(output == actual_output)
        print('seq:{}\nexpectedValue:{}\nactualValue:{}\n{}'.format(input, output, actual_output, sep))
                  


if __name__ == '__main__':
    main()