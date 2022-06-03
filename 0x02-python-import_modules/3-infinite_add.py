#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    total = 0
    if argc == 0:
        print(total)
    else:
        for i in range(0, argc):
            total += int(sys.argv[i + 1])
        print(total)
