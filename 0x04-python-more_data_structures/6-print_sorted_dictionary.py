#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k, y in sorted(a_dictionary.items()):
        print(f"{k}: {y}".format(k, y))
