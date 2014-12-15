__author__ = 'rahul'


# http://community.topcoder.com/stat?c=problem_statement&pm=1889&rd=4709


class AvoidRoads(object):

    @staticmethod
    def num_ways(width, height, bad_set_string):
        bad_path_set = AvoidRoads.get_blocked_path_set(bad_set_string)
        s = {}
        for i in xrange(height + 1):
            for j in xrange(width + 1):
                if i == 0 and j == 0:
                    s[(i, j)] = 1
                elif i == 0 and j > 0:
                    if ((i, j-1), (i, j)) in bad_path_set:
                        s[(i, j)] = 0
                    else:
                        s[(i, j)] = s[(i, j-1)]
                elif i > 0 and j == 0:
                    if ((i-1, j), (i, j)) in bad_path_set:
                        s[(i, j)] = 0
                    else:
                        s[(i, j)] = s[(i-1, j)]
                else:
                    # i > 0 and j > 0
                    n = 0
                    if ((i, j-1), (i, j)) not in bad_path_set:
                        n += s[(i, j-1)]
                    if ((i-1, j), (i, j)) not in bad_path_set:
                        n += s[((i-1, j))]
                    s[(i, j)] = n
                print s[(i, j)],
            print ""

        return s[((height, width))]

    @staticmethod
    def get_blocked_path_set(bad_list):
        bad_set = set()
        for bad in bad_list:
            t = [int(b) for b in bad.split(" ")]
            t = sorted(((t[0], t[1]), (t[2], t[3])))
            bad_set.add(tuple(t))
        return bad_set


def main():
    w = 9
    h = 9
    bad = {}

    p = AvoidRoads()
    n = p.num_ways(w, h, bad)
    print n


if __name__ == '__main__':
    main()