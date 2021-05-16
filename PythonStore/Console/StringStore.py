"""
Overview:
    - Utility using for processing string value into product with higher usage attributes.
Author:
    - Le Anh Tu
Information:
    - letuss004@gmail.com
    - 0336407556
Note:
    - If there is any issue, contact me as above
"""


def split_string(string):
    """
    :overview:
    :param string:
    :return:
    """
    return [char for char in string]


def ordinal(number):
    """

    :param number:
    :return:
    """

    if number >= 1:
        if number % 10 == 1:
            result = str(number) + "st"
        elif number % 10 == 2:
            result = str(number) + "nd"
        elif number % 10 == 3:
            result = str(number) + "rd"
        else:
            result = str(number) + "th"
    else:
        result = str(number) + ""
    return result


def list_ele_on_string(string):
    """
    :overview:
    :param string:
    :return:
    """
    res = []
    string = str(string)
    a = string.split(" ")
    for i in a:
        check = True
        if len(res) == 0:
            res.append(i)
        else:
            for j in res:
                if j == i:
                    check = False
                    break
            if check:
                res.append(i)
    return res


def count_num_of_ele_on_string(string):
    """
    :overview:
    :param string:
    :return:
    """
    string = str(string)
    a = string.split(" ")
    ele_already = []
    res = []
    for i in a:
        check = True
        if len(ele_already) == 0:
            count = 0
            for j in a:
                if i == j:
                    count += 1
            res.append(count)
            ele_already.append(i)
        else:
            for j in ele_already:
                if j == i:
                    check = False
                    break
            if check:
                count = 0
                for j in a:
                    if i == j:
                        count += 1
                ele_already.append(i)
                res.append(count)
    return res
