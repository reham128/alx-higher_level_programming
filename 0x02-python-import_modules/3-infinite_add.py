#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ac = sys.argv
    nums = len(ac)
    addition = 0
    for a in range(0, nums - 1):
        addition = addition + int(ac[a + 1])
    print("{:d}".format(addition))
