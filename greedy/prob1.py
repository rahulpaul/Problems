__author__ = 'rahul'


# In Olympic boxing, there are five judges who press a button when they think that a particular boxer
# has just landed a punch. The times of the button presses are recorded, and the boxer receives credit
# for a punch if at least three of the judges press their buttons within 1 second of each other.
# This "algorithm" needs a lot of refinement. Here is the version that you should implement. Find the
# maximum number of disjoint time intervals that can be chosen such that each interval is of duration
# 1 second or less and contains button presses from at least 3 different judges. Two intervals are disjoint
# if every time within one interval is strictly less than every time in the other. We give the boxer credit
# for one punch during each interval.
# The duration of an interval is the amount of time between the instant when it starts and when it ends,
# and a punch may be included in an interval if its recorded time is at the start, end, or in between.
# So, for example, the interval from 1 to 4 has duration 3, and a punch recorded at time 1, 2, 3, or 4 is in
# that interval. The intervals 1 to 4 and 5 to 22 are disjoint, but the intervals 1 to 4 and 4 to 22 are not
# disjoint.
#
# Create a class Boxing that contains a method maxCredit that is given five int[]s, a, b, c, d, and e,
# representing the times of the button presses of the five judges in milliseconds. The method returns the
# maximum credits that can be given to the boxer.

#Definition
#
#Class:	Boxing
#Method:	maxCredit
#Parameters:	int[], int[], int[], int[], int[]
#Returns:	int
#Method signature:	int maxCredit(int[] a, int[] b, int[] c, int[] d, int[] e)
#(be sure your method is public)
#
#
#Constraints
#-	Each of the five arguments will contain between 0 and 50 elements inclusive.
#-	Each element of each of the arguments will be between 0 and 180,000 inclusive.
#-	The elements within each of the arguments will be in strictly increasing order.
#
#Examples
#0)
#
#{1,2,3,4,5,6}
#{1,2,3,4,5,6,7}
#{1,2,3,4,5,6}
#{0,1,2}
#{1,2,3,4,5,6,7,8}
#Returns: 6
# This match had a fast start, with 6 punches credited in the first 6 milliseconds of the match! One way to
# choose 6 disjoint intervals is to choose [1,1], [2,2], [3,3], [4,4], [5,5], [6,6] each of which contains
# button presses from judges a, b, and c. There are three button presses in the time interval from 7 through 8,
# but only from two different judges so no additional credit can be given.
#1)
#
#{100,200,300,1200,6000}
#{}
#{900,902,1200,4000,5000,6001}
#{0,2000,6002}
#{1,2,3,4,5,6,7,8}
#Returns: 3
#One way to form three intervals is [0,1000], [1001,2000], [6000,6002]
#2)
#
#{5000,6500}
#{6000}
#{6500}
#{6000}
#{0,5800,6000}
#Returns: 1
# Any interval that doesn't include 6000 will not have enough button presses, so we can form only one disjoint
# interval with credit for a punch.


class InvalidIntervalError(Exception):
    pass


class CreditCounter(object):

    class Credit(object):

        def __init__(self, int_min_start=None, buzz_entries=None):
            self.int_min_start = int_min_start if int_min_start else -1
            self.buzz_entries = []
            self.int_judges = set()
            if buzz_entries:
                for entry in buzz_entries:
                    self.add_buzz(entry)

        @property
        def int_start(self):
            try:
                return self.buzz_entries[0][0]
            except IndexError:
                return -1

        @property
        def int_end(self):
            try:
                return self.buzz_entries[-1][0]
            except IndexError:
                return -1

        def buzz_count(self):
            return len(self.int_judges)

        def is_complete(self):
            return self.buzz_count() == 3

        def add_buzz(self, buzz_entry):
            judge = buzz_entry[1]
            ts = buzz_entry[0]
            if self.buzz_count() == 0:
                if ts > self.int_min_start:
                    self.buzz_entries.append(buzz_entry)
                    self.int_judges.add(judge)
            elif ts - self.int_start <= 1000:
                if judge not in self.int_judges:
                    self.buzz_entries.append(buzz_entry)
                    self.int_judges.add(judge)
                else:
                    if self.buzz_entries[0][1] == judge:
                        del self.buzz_entries[0]
                        self.buzz_entries.append(buzz_entry)
            else:
                raise InvalidIntervalError()

        def __str__(self):
            return '[%s, %s]' % (self.int_start, self.int_end)

    def __init__(self):
        self.count = 0
        self.current_credit = self.Credit()

    def add_buzz(self, buzz_entry):
        try:
            self.current_credit.add_buzz(buzz_entry)
            if self.current_credit.is_complete():
                print self.current_credit,
                self.count += 1
                self.current_credit = self.Credit(int_min_start=self.current_credit.int_end)
        except InvalidIntervalError:
            int_start = self.current_credit.int_start
            int_entries = list(self.current_credit.buzz_entries)
            while True:
                try:
                    entry = int_entries[0]
                    if entry[0] == int_start:
                        del int_entries[0]
                    else:
                        break
                except IndexError:
                    break

            self.current_credit = self.Credit(buzz_entries=int_entries)
            self.current_credit.add_buzz(buzz_entry)


def solution(a, b, c, d, e):
    aa = [(ei, 'a') for ei in a]
    bb = [(ei, 'b') for ei in b]
    cc = [(ei, 'c') for ei in c]
    dd = [(ei, 'd') for ei in d]
    ee = [(ei, 'e') for ei in e]
    xx = sorted(aa + bb + cc + dd + ee)

    del aa, bb, cc, dd, ee

    cr_cntr = CreditCounter()
    for t in xx:
        cr_cntr.add_buzz(t)
    print ''
    return cr_cntr.count


def main():
    a = [1, 2, 3, 4, 5, 6]
    b = [1, 2, 3, 4, 5, 6, 7]
    c = [1, 2, 3, 4, 5, 6]
    d = [0, 1, 2]
    e = [1, 2, 3, 4, 5, 6, 7, 8]
    print solution(a, b, c, d, e)

    a = [100, 200, 300, 1200, 6000]
    b = []
    c = [900, 902, 1200, 4000, 5000, 6001]
    d = [0, 2000, 6002]
    e = [1, 2, 3, 4, 5, 6, 7, 8]

    print solution(a, b, c, d, e)

    a = [5000, 6500]
    b = [6000]
    c = [6500]
    d = [6000]
    e = [0, 5800, 6000]

    print solution(a, b, c, d, e)


if __name__ == '__main__':
    main()
