from tkinter import Tk, PhotoImage
from sys import argv
from os import path, chdir

EXE_DIR = path.dirname(argv[0])
ASSETS_PATH = path.join(EXE_DIR, 'assets')
chdir(ASSETS_PATH)

window = Tk()

window.geometry("382x251")

class Assets:
    image_background = PhotoImage(file="background.png")
    image_titlebanner = PhotoImage(file='titlebanner.png')
    image_button_large = PhotoImage(file='button_large.png')
    image_title = PhotoImage(file='title.png')
    image_grade = PhotoImage(file='grade.png')
    image_progress = PhotoImage(file='progress.png')
    image_volume = PhotoImage(file='volume.png')
