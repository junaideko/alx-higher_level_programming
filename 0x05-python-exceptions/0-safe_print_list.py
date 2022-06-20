#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elemen = 0
    for y in range(x):
        try:
            print(my_list[y], end="")
            elemen += 1
        except IndexError:
            break
    print()
    return elemen
