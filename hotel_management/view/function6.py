from tkinter.ttk import *
import tkinter as tk


class Function6(Frame):
    def __init__(self, container, attr_root):
        super(Function6, self).__init__(container)
        self.root = attr_root
        self.var = tk.IntVar()
        # labels
        self.label_status = Label(self, text="            Change any themes you want", foreground="red")
        self.label_status.grid(row=0, column=0, columnspan=10, padx=2, pady=2, sticky="NS")
        # buttons
        self.button_back_call(attr_root)
        # radio
        self.radio_buttons_call()
        #
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=3)
        self.grid_columnconfigure(3, weight=3)
        self.grid_columnconfigure(4, weight=3)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=3)
        self.grid_columnconfigure(7, weight=3)
        self.grid_columnconfigure(8, weight=3)
        self.grid_columnconfigure(9, weight=3)
        pass

    def radio_buttons_call(self):
        self.radiobutton1 = Radiobutton(self, text="Arc    ", variable=self.var, value=1,
                                        command=lambda: self.radiobutton_command())
        self.radiobutton1.grid(row=1, column=5, columnspan=1, padx=2, pady=2, sticky="W")
        #
        self.radiobutton2 = Radiobutton(self, text="Equilux", variable=self.var, value=2,
                                        command=lambda: self.radiobutton_command())
        self.radiobutton2.grid(row=2, column=5, columnspan=1, padx=2, pady=2, sticky="W")
        #
        self.radiobutton3 = Radiobutton(self, text="Ubuntu ", variable=self.var, value=3,
                                        command=lambda: self.radiobutton_command())
        self.radiobutton3.grid(row=3, column=5, columnspan=1, padx=2, pady=2, sticky="W")
        #
        self.radiobutton4 = Radiobutton(self, text="Black   ", variable=self.var, value=4,
                                        command=lambda: self.radiobutton_command())
        self.radiobutton4.grid(row=4, column=5, columnspan=1, padx=2, pady=2, sticky="W")
        #
        self.radiobutton5 = Radiobutton(self, text="Blue   ", variable=self.var, value=5,
                                        command=lambda: self.radiobutton_command())
        self.radiobutton5.grid(row=5, column=5, columnspan=1, padx=2, pady=2, sticky="W")
        #
        self.radiobutton6 = Radiobutton(self, text="Adapta ", variable=self.var, value=6,
                                        command=lambda: self.radiobutton_command())
        self.radiobutton6.grid(row=6, column=5, columnspan=1, padx=2, pady=2, sticky="W")
        pass

    def radiobutton_command(self):
        theme = ""
        if self.var.get() == 1:
            print("---Theme root is updated. Arc is selected !")
            theme = "arc"
        elif self.var.get() == 2:
            theme = "equilux"
            print("---Theme root is updated. Equilux is selected !")
        elif self.var.get() == 3:
            theme = "ubuntu"
            print("---Theme root is updated. Ubuntu is selected !")
        elif self.var.get() == 4:
            theme = "black"
            print("---Theme root is updated. Black is selected !")
        elif self.var.get() == 5:
            theme = "blue"
            print("---Theme root is updated. Blue is selected !")
        elif self.var.get() == 6:
            theme = "adapta"
            print("---Theme root is updated. Adapta is selected !")
        self.root.style.theme_use(theme)
        pass

    def button_back_call(self, attr_root):
        button_back = Button(self, text="<-", width=5, command=lambda: command_to_back())
        button_back.grid(row=0, column=0, padx=2, pady=2, sticky="W")

        #
        def command_to_back():
            self.destroy()
            attr_root.show_frame(attr_root.MenuFrame)

        pass
