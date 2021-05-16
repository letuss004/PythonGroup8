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
import PythonStore.Console.ControllerStore as Cs
import datetime


def check_input_is_float_type(inputs):
    try:
        float(inputs)
        return True
    except ValueError:
        return False


def check_input_is_int_type(inputs):
    try:
        int(inputs)
        return True
    except ValueError:
        return False


def input_float_controller(value, min_value, max_value, label_annotation, color="red"):
    """

    :param value:
    :param min_value:
    :param max_value:
    :param label_annotation:
    :param color:
    :return:
    """
    # Constraint input_value must be float, if not => label_annotation raise error
    if check_input_is_float_type(value):
        # Constraint value variable must in range (min < val < max)
        if float(value) < min_value or float(value) > max_value:
            label_annotation.config(
                text=f"The values for min and max are {min_value} and {max_value}", foreground=color)
        else:
            return True
    else:
        label_annotation.config(text="The value is not a number", foreground=color)


def input_int_controller(value, min_value, max_value, label_annotation, color="red"):
    """

    :param value:
    :param min_value:
    :param max_value:
    :param label_annotation:
    :param color:
    :return:
    """
    # Constraint input_value must be float, if not => label_annotation raise error
    if check_input_is_int_type(value):
        # Constraint value variable must in range (min < val < max)
        if value < min_value or value > max_value:
            label_annotation.config(
                text=f"The values for min and max are {min_value} and {max_value}", foreground=color)
        else:
            return True
    else:
        label_annotation.config(text="The value is not a number", foreground=color)


def input_a_s_controller(inputs, label_annotation, attr_name, color="red"):
    """

    :param inputs:
    :param label_annotation:
    :param attr_name:
    :param color: default = red
    :return:
    """
    # list of all character is split by inputs
    list_all_re = Ss.split_string(inputs)
    list_unaccepted = []
    attr_name = str(attr_name)

    # this block is used to filter out duplicate special char
    for i in list_all_re:
        i = str(i)
        if Cs.is_a_s_char(i):
            list_unaccepted.append(i)
    list_unaccepted = Ls.list_no_repetition(list_unaccepted)

    # check attribute_name is only space character => if only " " => True
    check = True
    for i in list_all_re:
        i = str(i)
        if not i.isspace():
            check = False
            break

    # delete all unaccepted char before and add " ".
    # this if block is created by space char is valid but all of it is not
    # so clear and append " ". To left only 1 " " in the list
    if check:
        list_unaccepted.clear()
        list_unaccepted.append(" ")

    if len(list_unaccepted) != 0:
        label_annotation.config(text=attr_name + " can not contains: " + str(list_unaccepted), foreground=color)
        return False
    else:
        label_annotation.config(text="", foreground=color)
        return True


def input_identifier(inputs, label_annotation, color="red"):
    """

    :param inputs: the input value
    :param label_annotation:
        - The label which display input incorrect
        -
    :param color:
        - default = red
    :return:
        - if method return true => label_annotation = "" (mean nothing happen)
        - if method return false => label_annotation = label_annotation.config
    """
    if not inputs.isidentifier():
        label_annotation.config(text=str(inputs) + " is not an identifier", foreground=color)
        return False
    else:
        label_annotation.config(text="", foreground=color)
        return True


def input_dob(inputs, label_annotation, color="red"):
    """

    :param inputs:
        - the input value
    :param label_annotation:
        - The label which display input incorrect
    :param color:
        - default = red
    :return:
        - if method return true => label_annotation = "" (mean nothing happen)
        - if method return false => label_annotation = label_annotation.config
    """
    dob = str(inputs)
    try:
        date_of_birth = datetime.datetime.strptime(dob, "%d/%m/%Y")
        str(date_of_birth)
        label_annotation.config(text="", foreground=color)
        return True
    except ValueError:
        label_annotation.config(text="Time input " + dob
                                     + " does not match format '%d/%m/%Y'", foreground=color)
        return False
