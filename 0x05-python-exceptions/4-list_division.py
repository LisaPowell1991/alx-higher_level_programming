#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for index in range(list_length):
        try:
            result = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        except (ValueError, TypeError):
            result = 0
            print("wrong type")
        finally:
            new_list.append(result)

    return new_list
