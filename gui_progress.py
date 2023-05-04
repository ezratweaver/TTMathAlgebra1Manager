from tkinter import Canvas, Button
from assets import window, Assets

class ProgressScreen():

    def __init__(self):
        self.progress_screen_canvas = Canvas(
            window,
            bg = "#009DDC",
            height = 251,
            width= 384,
            highlightthickness= 0,
            relief = "ridge"
        )

        self.background = self.progress_screen_canvas.create_image(
            192, 125, image=Assets.image_background)
        
        self.progress_titlebanner = self.progress_screen_canvas.create_image(
            192, 45, image=Assets.image_titlebanner)
        
        self.progress_title = self.progress_screen_canvas.create_image(
            195, 43, image=Assets.image_progress_title) 
        
        self.progress_bar = self.progress_screen_canvas.create_image(
            160, 130, image=Assets.image_progress_bar_frame)
        
        self.percentage_frame = self.progress_screen_canvas.create_image(
            348, 130, image=Assets.image_stat_frame)
        
        self.stats_frame = self.progress_screen_canvas.create_image(
            195, 170, image=Assets.image_stat_frame)
        
        self.percentage = self.progress_screen_canvas.create_text(
            348, 130, text="95%", fill="#FFFFFF", font="AverageSans")
        
    def show_canvas(self):
        self.progress_screen_canvas.pack()

    def hide_canvas(self):
        self.progress_screen_canvas.pack_forget()
