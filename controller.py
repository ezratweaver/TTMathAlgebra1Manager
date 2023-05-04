from gui_main import MainScreen, window
from gui_progress import ProgressScreen
from gui_grade import *
from gui_volume import *

main_screen = MainScreen()
progress_screen = ProgressScreen()

def progress_button_check():
    if main_screen.progress_button_pressed:
        main_screen.progress_button_pressed = False
        main_screen.hide_canvas()
        progress_screen.show_canvas()
    window.after(50, progress_button_check)

def grade_button_check():
    if main_screen.grade_button_pressed:
        main_screen.grade_button_pressed = False
        main_screen.hide_canvas()
        # grade_screen.show_canvas()
    window.after(50, grade_button_check)
    
def volume_button_check():
    if main_screen.volume_button_pressed:
        main_screen.volume_button_pressed = False
        main_screen.hide_canvas()
        # volume_screen.show_canvas()
    window.after(50, volume_button_check)

progress_button_check()
grade_button_check()
volume_button_check()