#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = set()
    total = 0

    for unique_num in my_list:
        if unique_num not in new_list:
            new_list.add(unique_num)
            total += unique_num

    return total
