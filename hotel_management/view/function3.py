from tkinter.ttk import *
import hotel_management.model.database as db
import hotel_management.control.controller as controller


class Function3(Frame):
    def __init__(self, container, attr_root):
        super(Function3, self).__init__(container)
        # labels
        label_status = Label(self, text="Ordering", foreground="red")
        label_status.grid(row=0, column=1, columnspan=3, padx=3, pady=3, sticky="NS")
        # buttons
        self.button_back_call(attr_root)
        self.button_enter_call()
        # entries
        self.entry_supply_quantity_call()
        # combo boxes
        self.cbb_room_unavailable_call()
        self.cbb_supply_call()
        # grid column figure
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        pass

    def button_back_call(self, attr_root):
        button_back = Button(self, text="<-", width=5, command=lambda: command_to_back())
        button_back.grid(row=0, column=0, padx=2, pady=2, sticky="W")

        #
        def command_to_back():
            self.destroy()
            attr_root.show_frame(attr_root.MenuFrame)
            pass

    def cbb_room_unavailable_call(self):
        room_avail_value = db.get_room_unavailable()
        self.cbb_room_unavail = Combobox(self, value=room_avail_value, state="readonly")
        self.cbb_room_unavail.bind()
        self.cbb_room_unavail.grid(row=1, column=1, columnspan=2, padx=3, pady=3, sticky="SNEW")

        # labels for this entry
        self.label_room_unavail = Label(self, text="Room Available :", foreground="red")
        self.label_room_unavail.grid(row=1, column=0, padx=2, pady=2, sticky="W")

        self.label_room_unavail_annotation = Label(self, text="")
        self.label_room_unavail_annotation.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky="NS")
        pass

    def filter_value_of_cbb(self, event):
        # because id the unique so take id and forget name and price by method filter_value_of_cbb()
        # filter the shape from id || name || price (string) into ['id', 'name', 'price'] (list)

        # value has the shape of id || name || price
        cbb_value = str(self.cbb_supply.get())
        # values variable has shape ['id', 'name', 'price'] of supply
        cbb_value = cbb_value.split("     ")
        #
        self.cbb_values = []
        sid = cbb_value[0].split(": ")[1]
        name = cbb_value[1].split(": ")[1]
        price = cbb_value[2].split(": ")[1]
        self.cbb_values.append(sid)
        self.cbb_values.append(name)
        self.cbb_values.append(price)
        print("---Combobox of Ordering is updated by " + str(event))
        pass

    def cbb_supply_call(self):
        #
        data = db.get_supply_for_cbb()
        supply_value = []
        for supply in data:
            # supply[0] = id of the service
            sid = str(supply[0]).capitalize()
            name = str(supply[1]).capitalize()
            price = str(supply[2]).capitalize()
            #
            supply_value.append(f"ID: {sid}     Name: {name}     Price: {price}")

        #
        self.cbb_supply = Combobox(self, value=supply_value, state="readonly")
        self.cbb_supply.bind("<<ComboboxSelected>>", self.filter_value_of_cbb)
        self.cbb_supply.grid(row=3, column=1, columnspan=2, padx=3, pady=3, sticky="SNEW")

        # labels for this entry
        self.label_supply = Label(self, text="Supplies Information :", foreground="red")
        self.label_supply.grid(row=3, column=0, padx=2, pady=2, sticky="W")

        self.label_supply_annotation = Label(self, text="")
        self.label_supply_annotation.grid(row=4, column=1, columnspan=2, padx=2, pady=2, sticky="NS")

    def button_enter_call(self):
        self.button_enter = Button(self, text="Enter", command=lambda: [command_button_enter()])
        self.button_enter.grid(row=44, column=1, columnspan=2, padx=5, pady=5, sticky="NS")

        #
        def command_button_enter():
            # using try except to handle exception of int(self.entry_supply_quantity.get())
            try:
                # decorating
                self.label_quantity_annotation.config(text="", foreground="red")
                # quantity is number of supply customer want to order
                quantity = int(self.entry_supply_quantity.get())
                if self.cbb_supply.get() == "":
                    # this for decorating not necessary
                    self.label_supply_annotation.config(text="Please select supply", foreground="red")
                elif self.cbb_room_unavail.get() == "":
                    # this for decorating not necessary
                    self.label_room_unavail_annotation.config(text="Please select room", foreground="red")
                    self.label_supply_annotation.config(text="", foreground="red")
                elif controller.input_int_controller(quantity, 1, 20, self.label_quantity_annotation):
                    self.label_room_unavail_annotation.config(text="", foreground="red")
                    self.label_supply_annotation.config(text="", foreground="red")
                    # this necessary
                    for i in range(quantity):
                        room_id = self.cbb_room_unavail.get()
                        supply_id = self.cbb_values[0]
                        # print(supply_id + " this is supply id line 102 f3")
                        check_in_id = int(db.get_check_in_id_by_room_id(room_id))
                        #
                        db.set_room_service_table(check_in_id, supply_id)
                    # this for decorating not necessary
                    self.label_quantity_annotation.config(text="Action is Done !", foreground="red")
            except ValueError:
                self.label_quantity_annotation.config(text="Please enter an correct number", foreground="red")

    def entry_supply_quantity_call(self):
        self.entry_supply_quantity = Entry(self)
        self.entry_supply_quantity.grid(row=5, column=1, columnspan=3, padx=3, pady=3, sticky="SNEW")
        self.entry_supply_quantity.insert(-1, 'Quantity of order supply')

        # labels for this cbb
        self.label_entry_supply = Label(self, text="Quantity :", foreground="red")
        self.label_entry_supply.grid(row=5, column=0, padx=2, pady=2, sticky="W")

        self.label_quantity_annotation = Label(self, text="")
        self.label_quantity_annotation.grid(row=6, column=1, columnspan=2, padx=2, pady=2, sticky="NS")
        pass
