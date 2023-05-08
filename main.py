from os import system
from database_manger import grab_math_data, sift_math_data
from terminal_gui import print_gui

system("cls")

DATABASE_NAME = "algebra1dat"
PUBLIC_FOLDER = "TT Algebra 1"
TOTAL_LESSONS = 142

lesson_data = grab_math_data(
    PUBLIC_FOLDER, DATABASE_NAME)
lesson_numbers, progress_percentage, grade_percentage, grade_letter = sift_math_data(
    lesson_data, TOTAL_LESSONS)


print_gui(lesson_numbers, progress_percentage,
          grade_letter, grade_percentage)


