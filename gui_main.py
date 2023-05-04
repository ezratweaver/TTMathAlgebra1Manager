from tkinter import Canvas, Button
from assets import window, Assets

class MainScreen():

    def __init__(self):
        self.main_screen_canvas = Canvas(
            window,
            bg = "#009DDC",
            height = 251,
            width= 384,
            highlightthickness= 0,
            relief = "ridge"
        )

        self.background = self.main_screen_canvas.create_image(
            192, 125, image=Assets.image_background)

        self.main_titlebanner = self.main_screen_canvas.create_image(
            192, 40, image=Assets.image_titlebanner)

        self.main_title = self.main_screen_canvas.create_image(
            195, 38, image=Assets.image_main_title)

        self.progress_button_bg = self.main_screen_canvas.create_image(
            192, 115, image=Assets.image_button_large)

        self.grade_button_bg = self.main_screen_canvas.create_image(
            192, 165, image=Assets.image_button_large)

        self.volume_button_bg = self.main_screen_canvas.create_image(
            192, 215, image=Assets.image_button_large)
        
        self.progress_button_pressed = False
        self.progress_button = Button(
            self.main_screen_canvas,
            image=Assets.image_progress,
            borderwidth= 0,
            bg="#F58025",
            activebackground="#F58025",
            command=lambda: setattr(
                self, "progress_button_pressed", 
                not self.progress_button_pressed)
        )
        self.progress_button.place(
            x=158, y=103,
            width= 73, height= 22
        )

        self.grade_button_pressed = False
        self.grade_button = Button(
            self.main_screen_canvas,
            image=Assets.image_grade,
            borderwidth= 0,
            bg="#F58025",
            activebackground="#F58025",
            command=lambda: setattr(
                self, "grade_button_pressed", 
                not self.grade_button_pressed)
        )
        self.grade_button.place(
            x=156, y=151,
            width= 73, height= 22
        )

        self.volume_button_pressed = False
        self.volume_button = Button(
            self.main_screen_canvas,
            image=Assets.image_volume,
            borderwidth= 0,
            bg="#F58025",
            activebackground="#F58025",
            command=lambda: setattr(
                self, "volume_button_pressed", 
                not self.volume_button_pressed)
        )
        self.volume_button.place(
            x=158, y=201,
            width= 74, height= 22
        )

    def show_canvas(self):
        self.main_screen_canvas.pack()

    def hide_canvas(self):
        self.main_screen_canvas.pack_forget()




