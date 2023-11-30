#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    allNames = dir(hidden_4)
    for n in allNames:
        if n[:2] != '__':
            print("{}".format(n))
