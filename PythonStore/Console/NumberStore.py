"""
Overview:
    - Utility using for processing number value into product with higher usage attributes.
Author:
    - Le Anh Tu
Information:
    - letuss004@gmail.com
    - 0336407556
Note:
    - If there is any issue, contact me as above
"""

import StringStore


def ordinal(number):
    """

    :param number:
    :return:
    """
    if number >= 1:
        if number % 10 == 1:
            print(number + "st ")
        elif number % 10 == 2:
            print(number + "st ")
        elif number % 10 == 3:
            print(number + "rd ")
        else:
            print(number + "th ")
    else:
        print(number + " ")


def sum_arithmetic_progression(start, end, amount):
    """
    :overview: sum n first number.
    :param start:
    :param end:
    :param amount: the
    :example:
    :return:
    """
    summation = (amount * (start + end)) / 2
    return summation


def divisor_list(number):
    """
    :overview: create a list of divisor
    :param number: is 8
    :example: res = [1, 2, 4, 8]
    :return:
    """
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors


def split_number(number):
    """
    :overview:
    :param number:
    :example:
    :return:
    """
    a = str(number)
    b = StringStore.split_string(a)  # a list
    number_list = []
    for i in b:
        number_list.append(int(i))
    return number_list


def is_prime(number):
    """
    :overview:
    :param number: is 5
    :example: res = True
    :return:
    """
    check = True
    if number == 2:
        check = True
    else:
        for i in range(2, number):
            if number % i == 0:
                check = False
    return check


def count_digit_in1number(number):
    """
    :overview:
    :param number:
    :return:
    """
    num_list = split_number(number)
    return len(num_list)
