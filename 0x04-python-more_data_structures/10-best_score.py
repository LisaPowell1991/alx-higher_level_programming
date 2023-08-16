#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None

    highest_score = float('-inf')
    best_student = None

    for student, score in a_dictionary.items():
        if score > highest_score:
            highest_score = score
            best_student = student

    return best_student
