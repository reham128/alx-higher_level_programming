#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ac = sys.argv
    nums = len(ac) - 1
    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nums))
    for a in range(1, nums + 1):
        print("{}: {}".format(a, ac[a]))
