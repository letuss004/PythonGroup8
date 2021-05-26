from tkinter.ttk import *
import hotel_management.model.database as db


class Function5(Frame):
    def __init__(self, container, attr_root):
        super(Function5, self).__init__(container)
        # labels
        self.label_status = Label(self, text="History", foreground="red")
        self.label_status.grid(row=0, column=0, columnspan=5, padx=2, pady=2, sticky="NS")

        # buttons calling
        self.button_back_call(attr_root)
        self.button_check_out_id_call()
        self.button_check_in_date_call()
        self.button_check_out_date_call()
        self.button_price_call()
        #
        self.show_information()
        #

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=2)
        pass

    def button_back_call(self, attr_root):
        button_back = Button(self, text="<-", width=5, command=lambda: command_to_back())
        button_back.grid(row=0, column=0, padx=2, pady=2, sticky="W")

        #
        def command_to_back():
            self.destroy()
            attr_root.show_frame(attr_root.MenuFrame)
            pass

    def button_price_call(self):
        def command_sort_up():
            sort_value = db.sort_history_price_up()
            self.button_price.config(command=lambda: command_sort_down())
            self.show_information(sort=True, sort_value=sort_value)
            pass

        def command_sort_down():
            sort_value = db.sort_history_price_down()
            self.button_price.config(command=lambda: command_sort_up())
            self.show_information(sort=True, sort_value=sort_value)
            pass

        #
        self.button_price = Button(self, text="Price", command=lambda: command_sort_up())
        self.button_price.grid(row=1, column=3, columnspan=1, padx=2, pady=2, sticky="SNEW")

    def button_check_out_date_call(self):
        def command_sort_up():
            sort_value = db.sort_history_check_out_date_up()
            self.button_check_out_date.config(command=lambda: command_sort_down())
            self.show_information(sort=True, sort_value=sort_value)
            pass

        def command_sort_down():
            sort_value = db.sort_history_check_out_date_down()
            self.button_check_out_date.config(command=lambda: command_sort_up())
            self.show_information(sort=True, sort_value=sort_value)
            pass

        #
        self.button_check_out_date = Button(self, text="Check Out Date", command=lambda: command_sort_up())
        self.button_check_out_date.grid(row=1, column=2, columnspan=1, padx=2, pady=2, sticky="SNEW")

    def button_check_in_date_call(self):
        def command_sort_up():
            sort_value = db.sort_history_check_in_date_up()
            self.button_check_in_date.config(command=lambda: command_sort_down())
            self.show_information(sort=True, sort_value=sort_value)
            pass

        def command_sort_down():
            sort_value = db.sort_history_check_in_date_down()
            self.button_check_in_date.config(command=lambda: command_sort_up())
            self.show_information(sort=True, sort_value=sort_value)
            pass

        #
        self.button_check_in_date = Button(self, text="Check In Date", command=lambda: command_sort_up())
        self.button_check_in_date.grid(row=1, column=1, columnspan=1, padx=2, pady=2, sticky="SNEW")

    def button_check_out_id_call(self):
        def command_sort_up():
            sort_value = db.sort_history_check_out_id_up()
            self.button_check_out_id.config(command=lambda: command_sort_down())
            self.show_information(sort=True, sort_value=sort_value)
            pass

        def command_sort_down():
            sort_value = db.sort_history_check_out_id_down()
            self.button_check_out_id.config(command=lambda: command_sort_up())
            self.show_information(sort=True, sort_value=sort_value)
            pass

        #
        self.button_check_out_id = Button(self, text="Check Out ID", command=lambda: command_sort_up())
        self.button_check_out_id.grid(row=1, column=0, columnspan=1, padx=2, pady=2, sticky="SNEW")

    def show_information(self, sort=False, sort_value=None):
        """

        :param sort:
        :param sort_value:
        :return:
        """
        # can not declared parameter directly in constructor
        # so pycharm hint this below
        if sort_value is None:
            sort_value = [1]
        #
        if sort:
            self.destroy_show_inf()
            data = sort_value
        else:
            # data include check out id, in date, out date and price
            data = db.get_history_information()
        # this thing for auto increase row after each row of information
        row = 3
        element = 0
        #
        # self.label_room_id_list = []
        self.label_check_out_id_list = []
        self.label_check_in_date_list = []
        self.label_check_out_date_list = []
        self.label_price_list = []
        # print(data)
        # data1 only room
        for information in data:
            check_out_id = information[0]
            check_in_date = information[1]
            check_out_date = information[2]
            price = information[3]
            #
            self.label_check_out_id_list.append(Label(self, text=check_out_id))
            self.label_check_out_id_list[element].grid(row=row, column=0, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            self.label_check_in_date_list.append(Label(self, text=check_in_date))
            self.label_check_in_date_list[element].grid(row=row, column=1, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            self.label_check_out_date_list.append(Label(self, text=check_out_date))
            self.label_check_out_date_list[element].grid(row=row, column=2, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            self.label_price_list.append(Label(self, text=price))
            self.label_price_list[element].grid(row=row, column=3, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            element += 1
            row += 1
        pass

    def destroy_show_inf(self):
        # self.label_room_id_list = []
        for i in self.label_check_out_id_list:
            i.destroy()

        for i in self.label_check_in_date_list:
            i.destroy()

        for i in self.label_check_out_date_list:
            i.destroy()

        for i in self.label_price_list:
            i.destroy()
        pass
