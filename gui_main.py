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
            192,
            125,
            image=Assets.image_background
        )

        self.main_titlebanner = self.main_screen_canvas.create_image(
            192,
            40,
            image=Assets.image_titlebanner
        )

        self.main_title = self.main_screen_canvas.create_image(
            195,
            38,
            image=Assets.image_main_title
        )

        self.progress_button_bg = self.main_screen_canvas.create_image(
            192,
            115,
            image=Assets.image_button_large
        )

        self.grade_button_bg = self.main_screen_canvas.create_image(
            192,
            165,
            image=Assets.image_button_large
        )

        self.volume_button_bg = self.main_screen_canvas.create_image(
            192,
            215,
            image=Assets.image_button_large
        )




    def show_canvas(self):
        self.main_screen_canvas.pack()

    def hide_canvas(self):
        self.main_screen_canvas.pack_forget()




m = MainScreen()
m.show_canvas()
window.mainloop()
