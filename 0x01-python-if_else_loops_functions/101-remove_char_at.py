#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str

    result = ''
    for current_index in range(len(str)):
            if current_index != n:
                result += str[current_index]

    return result
