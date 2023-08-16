#!/usr/bin/python3


def common_elements(set_1, set_2):
    common_element_set = set()

    for common_element in set_1:
        if common_element in set_2:
            common_element_set.add(common_element)

    return common_element_set
