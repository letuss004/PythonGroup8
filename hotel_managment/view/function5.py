from tkinter.ttk import *
import hotel_managment.model.database as db

class Function5(Frame):
    def __init__(self, container, attr_root):
        super(Function5, self).__init__(container)
        # labels
        self.label_status = Label(self, text="History", foreground="red")
        self.label_status.grid(row=0, column=0, columnspan=5, padx=2, pady=2, sticky="NS")

        #
        self.button_back_call(attr_root)
        self.button_history_rooms_call()
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

    def button_history_rooms_call(self):
        self.button_room_id = Button(self, text="Check Out ID")
        self.button_room_id.grid(row=1, column=0, columnspan=1, padx=2, pady=2, sticky="SNEW")

        self.button_room_id = Button(self, text="Check In Date")
        self.button_room_id.grid(row=1, column=1, columnspan=1, padx=2, pady=2, sticky="SNEW")

        self.button_room_id = Button(self, text="Check Out Date")
        self.button_room_id.grid(row=1, column=2, columnspan=1, padx=2, pady=2, sticky="SNEW")

        self.button_room_id = Button(self, text="Price")
        self.button_room_id.grid(row=1, column=3, columnspan=1, padx=2, pady=2, sticky="SNEW")
        pass

    def show_information(self, destroy=0):
        """

        :param destroy:
                destroy = 0 => there is no labels to destroy at beginning
                destroy = 1 => destroy labels and update value for showing again
        :return:
        """
        if destroy == 1:
            self.destroy_show_inf()

        # this thing for auto increase row after each row of information
        row = 3
        element = 0
        #
        self.label_room_id_list = []
        self.label_check_out_id_list = []
        self.label_check_in_date_list = []
        self.label_check_out_date_list = []
        self.label_price_list = []
        # data include check out id, in date, out date and price
        data = db.get_history_information()
        print(data)
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
        pass