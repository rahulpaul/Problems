def count_anagrams(s: str):
    anagram_count = 0
    g = gen_substrings()
    all_substrings = []
    for letter in s:
        next(g)
        substrings = g.send(letter)
        substrings = [''.join(sorted(word)) for word in substrings]
        for _set in all_substrings:
            for _string in substrings:
                if _string in _set:
                    anagram_count += 1
        
        all_substrings.append(substrings)
    
    return anagram_count


def gen_substrings():
    last_row = []
    while True:
        letter = yield
        new_last_row = [letter]
        for word in last_row:
            new_last_row.append(word+letter)
        
        last_row = new_last_row
        yield last_row


def main():
    q = int(input())
    for _ in range(q):
        s = input()
        c = count_anagrams(s)
        print(c)

if __name__ == '__main__':
    main()
