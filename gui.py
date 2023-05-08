from tkinter import Tk, Label



class MainScreen():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("424x241")

        self.progress = Label()

    def run(self):
        self.window.mainloop()


m = MainScreen()
m.run()