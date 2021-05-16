"""
Overview:
    - Utility using for processing list into product with higher usage attributes.
Author:
    - Le Anh Tu
Information:
    - letuss004@gmail.com
    - 0336407556
Note:
    - If there is any issue, contact me as above
"""


def insert(list_a, list_b, position):
    """
    :overview:
        - res = insert list 2 into list 1 at position
    :param list_a: a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    :param list_b: b = [9, 8, 7, 6, 5, 4, 3, "m", 1]
    :param position: is 5
    :example: res = [1, 2, 3, 4, 5, 9, 8, 7, 6, 5, 4, 3, 'm', 1, 6, 7, 8, 9]
    :return: res
    """
    res = []
    if 0 <= position <= len(list_a):
        for i in range(0, len(list_a) + 1):
            if i == position:
                for j in range(0, len(list_b)):
                    res.append(list_b[j])
                if i != len(list_a):
                    res.append(list_a[i])
            else:
                if i < len(list_a):
                    res.append(list_a[i])
    else:
        print("List's position is invalid!")
    return res


def intersection(list1, list2):
    """
    :overview:
        - res = list1 - list2
    :param list1:
    :param list2:
    :return:
    """
    list_total = insert(list1, list2, len(list1))
    res = []
    for i in list_total:
        checkpoint = True
        for j in res:
            if i == j:
                checkpoint = False
                break
        if checkpoint:
            res.append(i)
    return res


def union(list1, list2):
    """
    :overview:
        - res = list 1 - list 2
    :param list1: is ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    :param list2: is ['r', 'g', 'y', 'k', 'j', 'u', 'y']
    :example: res = ['r', 'y', 'u']
    :return: res
    """
    res = []
    for i in list1:
        for j in list2:
            check = True
            if i == j:
                for q in res:
                    if i == q:
                        check = False
                        break
                if check:
                    res.append(i)
    return res


def subtract(intersection_list, union_list):
    """
    :overview:
        - using intersection method above
        - using union method above
        - res = intersection_list - union_list
    :param intersection_list: is [1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 44, 11]
    :param union_list: is [6, 7, 8, 9]
    :example: res = [99, 44, 11]
    :return: res
    """
    res = []
    for i in intersection_list:
        check = True
        for j in union_list:
            if i == j:
                check = False
                break
        if check:
            res.append(i)
    return res


def list_no_repetition(list_input):
    """
    :oveview:
    :note:
        -
    :param list_input:
    :return:
    """
    res = []
    for i in list_input:
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
