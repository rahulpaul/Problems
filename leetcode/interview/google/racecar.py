""" https://leetcode.com/problems/race-car/

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.

"""
import collections


class Solution:
    def racecar(self, target: int) -> str:
        # bfs
        q = collections.deque([('', 0, 1)]) # move, pos, vel
        while q:
            move, pos, vel = q.popleft()
            if pos == target:
                return move
            # A
            q.append((f"{move}A", pos+vel, vel*2))
            # R, considered in 4 cases, get rid of excessive search
            if (pos > target and vel > 0) or (pos < target and vel < 0) or (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):  #reverse
                q.append((f"{move}R", pos, -1 if vel > 0 else 1))


def main():
    print(Solution().racecar(5))


if __name__ == "__main__":
    main()
