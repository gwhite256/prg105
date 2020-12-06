import tkinter
import tkinter.messagebox
import pickle


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look Up Item',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Item',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change SKU/Description',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete Item',
                                          variable=self.radio_var, value=4)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = ChangeGUI(self.master)
        elif self.radio_var.get() == 4:
            _ = DeleteGUI(self.master)

        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')


class LookGUI:
    def __init__(self, master):

        try:
            input_file = open("inventory.dat", 'wb')
            self.inventory = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.inventory = {}

        self.look = tkinter.Toplevel(master)
        self.look.title('Search for item and get the quantity')

        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        self.search_label = tkinter.Label(self.top_frame, text='Enter a SKU to get the quantity of an item: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        sku = self.search_entry.get()
        result = self.inventory.get(sku, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master):

        try:
            input_file = open("inventory.dat", 'wb')
            self.inventory = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.inventory = {}

        self.add = tkinter.Toplevel(master)
        self.add.title('Add a SKU to the system')

        self.top_frame = tkinter.Frame(self.add)
        self.middle_frame = tkinter.Frame(self.add)
        self.bottom_frame = tkinter.Frame(self.add)

        self.add_label = tkinter.Label(self.top_frame, text='Enter a 6 digit number: ')
        self.add_entry = tkinter.Entry(self.top_frame, width=15)
        self.description_label = tkinter.Label(self.top_frame, text='Enter a item description: ')
        self.description_entry = tkinter.Entry(self.top_frame, width=15)
        self.quantity_label = tkinter.Label(self.top_frame, text='Enter a quantity: ')
        self.quantity_entry = tkinter.Entry(self.top_frame, width=15)

        self.add_label.pack(side='left')
        self.add_entry.pack(side='left')
        self.description_label.pack(side='left')
        self.description_entry.pack(side='left')
        self.quantity_label.pack(side='left')
        self.quantity_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.add_button = tkinter.Button(self.bottom_frame, text='Add', command=self.add_sku)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add_sku(self):
        sku = self.add_entry.get()
        description = self.description_entry.get()
        quantity = self. quantity_entry.get()
        if sku in self.inventory:
            result = sku + " is already in the system."
        else:
            result = description + " will be added into the system."
            self.inventory[sku] = description + quantity
            output_file = open("inventory.dat", 'wb')
            pickle.dump(self.inventory, output_file)
            output_file.close()
        self.value.set(result)

    def back(self):
        self.add.destroy()


class ChangeGUI:
    def __init__(self, master):

        try:
            input_file = open("inventory.dat", 'wb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.look = tkinter.Toplevel(master)
        self.look.title('Change SKU')

        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        self.change_label = tkinter.Label(self.top_frame, text='Enter a SKU to change:  ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        self.change_label.pack(side='left')
        self.search_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.search_button = tkinter.Button(self.bottom_frame, text='Change', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'SKU not found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class DeleteGUI:
    def __init__(self, master):

        try:
            input_file = open("inventory.dat", 'wb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.look = tkinter.Toplevel(master)
        self.look.title('Delete a SKU')

        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        self.search_label = tkinter.Label(self.top_frame, text='Enter a SKU to delete: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.search_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'SKU Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handles the remaining program logic
    _ = CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
