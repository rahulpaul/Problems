# Problem: https://www.hackerrank.com/challenges/queens-attack-2/problem


def count_moves(n, rq, cq, obstacles):
    moves = 0
    # move right => increase columns
    for ci in range(cq+1, n+1):
        if (rq, ci) in obstacles:
            break
        moves += 1
    
    # move left => decrease columns
    for ci in range(cq-1, 0, -1):
        if (rq, ci) in obstacles:
            break
        moves += 1
    
    # move up => increase rows
    for ri in range(rq+1, n+1):
        if (ri, cq) in obstacles:
            break
        moves += 1
    
    # move down => decrease rows
    for ri in range(rq-1, 0, -1):
        if (ri, cq) in obstacles:
            break
        moves += 1
    
    # move top-right
    for i in range(1, 1 + min(n-rq, n-cq)):
        ri = rq + i
        ci = cq + i
        if (ri, ci) in obstacles:
            break
        moves += 1
    
    # move top-left
    for i in range(1, 1 + min(n-rq, cq-1)):
        ri = rq + i
        ci = cq - i
        if (ri, ci) in obstacles:
            break
        moves += 1
    
    # move bottom-right
    for i in range(1, 1 + min(rq-1, n-cq)):
        ri = rq - i
        ci = cq + i
        if (ri, ci) in obstacles:
            break
        moves += 1
    
    # move bottom-left
    for i in range(1, 1 + min(rq-1, cq-1)):
        ri = rq - i
        ci = cq - i
        if (ri, ci) in obstacles:
            break
        moves += 1

    return moves


def main():
    n, k = (int(x) for x in input().split(' '))
    rq, cq = (int(x) for x in input().split(' '))
    obstacles = set()
    for _ in range(k):
        ri, ci = (int(x) for x in input().split(' '))
        obstacles.add((ri, ci))
    
    print(count_moves(n, rq, cq, obstacles))


if __name__ == "__main__":
    main()
