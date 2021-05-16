import mysql.connector as cnt

database = cnt.connect(host="localhost", user="root", passwd="12345678", database="hotel")
cursor = database.cursor()


def get_room_avail():
    return None


def get_room_data():
    condition = f"SELECT * FROM room"
    cursor.execute(condition)
    data = cursor.fetchall()
    return data


def get_room_type():
    condition = f"SELECT * FROM room_type"
    cursor.execute(condition)
    data = cursor.fetchall()
    # filter data into list of string
    result = []
    for i in data:
        result.append(i[0])
    return result


def get_room_available(types=0):
    """

    :param types:
        1 = standard
        2 = business
        3 = president
    :return:
    """
    if types == 0:
        condition = f"SELECT * FROM room WHERE status = 'available'"
    elif types == 1:
        condition = f"SELECT * FROM room WHERE type = 'standard' and status = 'available'"
    elif types == 2:
        condition = f"SELECT * FROM room WHERE type = 'business' and status = 'available'"
    elif types == 3:
        condition = f"SELECT * FROM room WHERE type = 'president' and status = 'available'"
    else:
        condition = f"SELECT * FROM room WHERE status = 'available'"
        print("Types is an bad value!!! Set type as default.")
    # execute and get data
    cursor.execute(condition)
    data = cursor.fetchall()
    # filter data into list of string
    result = []
    for i in data:
        result.append(i[0])
    return result
