from tkinter import *

class Window:

    def __init__(self):
        
        self.main_window = Tk()

        self.main_window.title("Temparature convertor")
        self.main_window.geometry("1080x720")





        self.main_window.config(bg="#ff6b81")

        self.isPressed = False

        self.create_items()

        self.main_window.mainloop()

    def create_items(self):
        self.new_button()
        self.new_spin_box()

    def new_label(self):
        if not(self.isPressed):
            label = Label(self.main_window, text="Holy fuck !")
            label.grid()
        
            self.isPressed = True

    def new_button(self):


        btn = Button(self.main_window, text="Push me !", command=self.new_label)
        btn.grid()

    def new_spin_box(self):
        spnbox = Spinbox(self.main_window)
        spnbox.grid()

w = Window()
