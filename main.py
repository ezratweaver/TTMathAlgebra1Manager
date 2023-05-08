from os import system
from database_manger import grab_math_data, sift_math_data
from terminal_gui import print_gui

system("cls")

DATABASE_NAME = "algebra1dat"
PUBLIC_FOLDER = "TT Algebra 1"
TOTAL_LESSONS = 142
TOTAL_TESTS = 19

lesson_data = grab_math_data(PUBLIC_FOLDER, DATABASE_NAME)
test_data = grab_math_data(PUBLIC_FOLDER, DATABASE_NAME, test=True)

lesson_variables = sift_math_data(lesson_data, TOTAL_LESSONS)
test_variables = sift_math_data(test_data, TOTAL_TESTS)

print("Welcome to Teaching Textbooks Algebra 1 Manager\n")
print("[1] Lessons\n[2] Tests\n")
try:
    user_view_choice = input("What would you like to view? ")
except KeyboardInterrupt:
    system("cls")
    quit()

system("cls")

if user_view_choice == "1":
    print_gui("Lesson", *lesson_variables)
elif user_view_choice == "2":
    print_gui("Test", *test_variables)
else:
    system('cls')
    print("Invalid Input")
    quit()
