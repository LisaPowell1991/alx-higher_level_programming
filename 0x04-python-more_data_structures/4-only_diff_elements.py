#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    diff_element_set = set()

    for diff_element in set_1:
        if diff_element not in set_2:
            diff_element_set.add(diff_element)

    for diff_element in set_2:
        if diff_element not in set_1:
            diff_element_set.add(diff_element)

    return diff_element_set
