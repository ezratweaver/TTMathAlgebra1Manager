from math import floor

def create_progress_bar(progress):
    progress = int(progress[:-1])
    progress = floor(progress / 5)
    string = "=" * progress
    string = string + (" " * (20 - progress))
    string = "|" + string + "|"
    return string

def print_gui(type, quiz_numbers, quiz_percentage,
              grade_letter, grade_percentage):
    quiz_progress_bar = create_progress_bar(quiz_percentage)
    grade_progress_bar = create_progress_bar(grade_percentage)

    ws = ''
    ws2 = '     '

    if type == "Quiz":
        ws = '    '
    if quiz_percentage == "100%":
        ws2 = '    '

    print(f"{type}: {quiz_numbers}                {ws}Grade: {grade_letter}")
    print("----------------------         ----------------------")
    print(f"{quiz_progress_bar} {quiz_percentage}{ws2}{grade_progress_bar} {grade_percentage}")
    print("----------------------         ----------------------")