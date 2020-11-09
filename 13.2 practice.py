
import tkinter


class MPG:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.gallon_prompt = tkinter.Label(self.top_frame,
                                           text='How many gallons can your car hold?: ')
        self.gallon_get = tkinter.Entry(self.top_frame, width=15)
        self.gallon_prompt.pack(side='left')
        self.gallon_get.pack(side='left')

        self.mile_prompt = tkinter.Label(self.mid_frame,
                                         text='How many miles did you drive?: ')
        self.mile_get = tkinter.Entry(self.mid_frame,
                                      width=15)
        self.mile_prompt.pack(side='left')
        self.mile_get.pack(side='left')

        self.value = tkinter.StringVar()
        self.results_label = tkinter.Label(self.bottom_frame, textvariable=self.value)
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.results_label.pack(side='top')
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


    def calculate(self):
        gas = float(self.gallon_get.get())
        miles = float(self.mile_get.get())

        mpg = "You get " + format(miles/gas, ',.2f') + " miles per gallon"
        self.value.set(mpg)


car = MPG()
