from os import system
from database_manger import grab_math_data, sift_math_data
from terminal_gui import print_gui

DATABASE_NAME = "algebra1dat"
PUBLIC_FOLDER = "TT Algebra 1"
TOTAL_LESSONS = 142
TOTAL_TESTS = 19

lesson_data = grab_math_data(PUBLIC_FOLDER, DATABASE_NAME)
quiz_data = grab_math_data(PUBLIC_FOLDER, DATABASE_NAME, quiz=True)

lesson_variables = sift_math_data(lesson_data, TOTAL_LESSONS)
quiz_variables = sift_math_data(quiz_data, TOTAL_TESTS)

def main_terminal_gui():
    system("cls")
    print("Welcome to Teaching Textbooks Algebra 1 Manager\n")
    print("[1] Lessons\n[2] Quizzes\n")
    try:
        user_view_choice = input("What would you like to view? ")
    except KeyboardInterrupt:
        system("cls")
        quit()

    system("cls")


    try:
        if user_view_choice == "1":
            print_gui("Lesson", *lesson_variables)
            input('')
            main_terminal_gui()
        elif user_view_choice == "2":
            print_gui("Quiz", *quiz_variables)
            input()
            main_terminal_gui()
        else:
            system('cls')
            print("Invalid Input")
            quit()
    except KeyboardInterrupt:
        main_terminal_gui()

main_terminal_gui()