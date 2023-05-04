from tkinter import Tk, PhotoImage
from sys import argv
from os import path, chdir

EXE_DIR = path.dirname(argv[0])
ASSETS_PATH = path.join(EXE_DIR, 'assets')
chdir(EXE_DIR)

window = Tk()

window.geometry("384x251")
window.resizable(False, False)

class Assets:
    image_background = PhotoImage(file="assets/background.png")
    image_titlebanner = PhotoImage(file='assets/titlebanner.png')
    image_button_large = PhotoImage(file='assets/button_large.png')
    image_button_small = PhotoImage(file="assets/button_small.png")
    image_main_title = PhotoImage(file='assets/title.png')
    image_grade = PhotoImage(file='assets/grade.png')
    image_progress = PhotoImage(file='assets/progress.png')
    image_volume = PhotoImage(file='assets/volume.png')
    image_progress_title = PhotoImage(file="assets/progress_title.png")
    image_progress_bar_frame = PhotoImage(file="assets/progress_bar_frame.png")
    image_stat_frame = PhotoImage(file="assets/stat_frame.png")
    image_menu = PhotoImage(file="assets/menu.png")
