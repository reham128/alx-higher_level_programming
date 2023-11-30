#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ac = sys.argv
    nums = len(ac) - 1
    if nums == 0:
        print("0 arguments.")
    elif nums == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(nums))
    for a in range(1, nums + 1):
        print("{:d}: {:s}".format(a, ac[a]))
