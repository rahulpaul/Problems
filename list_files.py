import sys
import os
import heapq


def yield_files(root):    
    if os.path.isfile(root):
        yield root
    elif os.path.isdir(root):        
        for child in os.listdir(root):
            yield from yield_files(os.path.join(root, child))


def nlargest_files(n, files):
    return heapq.nlargest(n, files, key = lambda file : os.path.getsize(file))    


if __name__ == '__main__':
    for file in nlargest_files(int(sys.argv[2]), yield_files(sys.argv[1])):
        print(os.path.getsize(file), file)