"""
Overview:
    - Utility using for handling incorrect input.
Author:
    - Le Anh Tu
Contributor:
    - None
Information:
    - letuss004@gmail.com
    - 0336407556
Note:
    - If there is any issue, contact me as above
"""

import PythonStore.Console.StringStore as Ss
import PythonStore.Console.ListStore as Ls
import datetime


def input_controller(message, min_value, max_value):
    """

    :param message:
    :param min_value:
    :param max_value:
    :return:
    """
    # Constraint input_value must be correct, if not => re-input by input_float_not_exception method
    value = input_float_not_exception(message)

    # Constraint value variable must in range (min < val < max)
    while value < min_value or value > max_value:
        value = input_float_not_exception(
            "Input value must in range(%f, %f) ! Enter again: " % (min_value, max_value))
    return value


def float_controller(message, min_value, max_value):
    """

    :param message:
    :param min_value:
    :param max_value:
    :return:
    """
    # Constraint input_value must be correct, if not => re-input by input_float_not_exception method
    value = input_float_not_exception(message)

    # Constraint value variable must in range (min < val < max)
    while value < min_value or value > max_value:
        value = input_float_not_exception(
            "Input value must in range(%f, %f) ! Enter again: " % (min_value, max_value))


def integer_controller(message, min_value, max_value):
    """

    :param message:
    :param min_value:
    :param max_value:
    :return:
    """

    # Constraint input_value must be correct, if not => re-input by input_integer_not_exception method
    value = input_integer_not_exception(message)

    # Constraint value variable must in range (min < val < max)
    while value < min_value or value > max_value:
        value = input_integer_not_exception(
            "Input value must in range(%d, %d) ! Enter again: " % (min_value, max_value))
    return value


def input_a_n_s_controller(message, attribute_name):
    """

    :param message:
    :param attribute_name:
    :return:
    """
    inputs = str(input(message))
    list_all_re = Ss.split_string(inputs)
    list_unaccepted = []

    # this block is used to filter out duplicate special char
    for i in list_all_re:
        i = str(i)
        if is_a_n_s_char(i):
            print(is_a_n_s_char(i))
            list_unaccepted.append(i)
    list_unaccepted = Ls.list_no_repetition(list_unaccepted)

    # check attribute_name is only space character => if yes => True
    check = True
    for i in list_all_re:
        i = str(i)
        if not i.isspace():
            check = False
            break

    # delete all unaccepted char before and add " ".
    # this if block is created by space char is valid but all of it is not
    if check:
        list_unaccepted.clear()
        list_unaccepted.append(" ")

    # force user re-input the corresponding input until end.
    while len(list_unaccepted) != 0:
        if check:
            print(attribute_name + " can not only space.")
            inputs = input_a_s_controller(" - Enter another " + attribute_name + ": ", attribute_name)
        else:
            print(attribute_name + " can not contains: ", end="")
            print(list_unaccepted)
            inputs = input_a_s_controller("Enter another " + attribute_name + ": ", attribute_name)
    return inputs


def input_a_s_controller(message, attribute_name):
    """

    :param message:
    :param attribute_name:
    :return:
    """
    inputs = str(input(message))
    list_all_re = Ss.split_string(inputs)
    list_unaccepted = []

    # this block is used to filter out duplicate special char
    for i in list_all_re:
        i = str(i)
        if is_a_s_char(i):
            list_unaccepted.append(i)
    list_unaccepted = Ls.list_no_repetition(list_unaccepted)

    # check attribute_name is only space character => if yes => True
    check = True
    for i in list_all_re:
        i = str(i)
        if not i.isspace():
            check = False
            break

    # delete all unaccepted char before and add " ".
    # this if block is created by space char is valid but all of it is not
    if check:
        list_unaccepted.clear()
        list_unaccepted.append(" ")

    # force user re-input the corresponding input until end.
    while len(list_unaccepted) != 0:
        if check:
            print(attribute_name + " can not only space.")
            inputs = input_a_s_controller(" - Enter another " + attribute_name + ": ", attribute_name)
            list_unaccepted.clear()
        else:
            print(attribute_name + " can not contains: ", end="")
            print(list_unaccepted)
            inputs = input_a_s_controller("Enter another " + attribute_name + ": ", attribute_name)
            list_unaccepted.clear()
    return inputs


def input_identifier(message):
    inputs = input(message)

    while not inputs.isidentifier():
        inputs = input("Your input is not identifier. Enter again: ")

    return inputs


def is_a_n_s_char(str_input):
    """

    :param str_input:
    :return:
    """
    inputs = str(str_input)
    list_all_re = Ss.split_string(inputs)
    check = False

    # this block is used to find out special char, if True => end
    # note -- there is any non-special char => False => end
    for i in list_all_re:
        i = str(i)
        if not i.isalpha() and not i.isspace() and not i.isdigit():
            check = True
        else:
            check = False
            break
    return check


def is_a_s_char(str_input):
    """

    :param str_input:
    :return:
    """
    inputs = str(str_input)
    list_all_re = Ss.split_string(inputs)
    check = False

    # this block is used to find out special char, if True => end
    # note -- there is any non-special char => False => end
    for i in list_all_re:
        i = str(i)
        if not i.isalpha() and not i.isspace():
            check = True
        else:
            check = False
            break
    return check


def is_custom_special_char():
    pass


def input_integer_not_exception(message):
    """

    :param message:
    :return:
    """
    try:
        inputs = int(input(message))
        return inputs
    except ValueError:
        return input_integer_not_exception(
            "Your input is not int type that make ValueError exception. Re-input: ")


def input_float_not_exception(message):
    """

    :param message:
    :return:
    """
    try:
        inputs = float(input(message))
        return inputs
    except ValueError:
        return input_integer_not_exception(
            "Your input is not float type that make ValueError exception. Re-input: ")


def input_dob(message):
    dob = str(input(message))
    try:
        date_of_birth = datetime.datetime.strptime(dob, "%d/%m/%Y")
        str(date_of_birth)
        return dob
    except ValueError:
        return input_dob("Time input " + dob
                         + " does not match format '%d/%m/%Y'. Re-input: ")
