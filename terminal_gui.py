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

    ws = '     '
    if quiz_percentage == "100%":
        ws = '    '

        
    ws2 = ''
    if type == "Test":
        ws2 = '    '

    print(f"{type}: {quiz_numbers}                {ws2}Grade: {grade_letter}")
    print("----------------------         ----------------------")
    print(f"{quiz_progress_bar} {quiz_percentage}{ws}{grade_progress_bar} {grade_percentage}")
    print("----------------------         ----------------------")