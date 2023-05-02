from sqlite3 import connect
from os import path, environ, chdir
from get_average import get_average

def grab_lesson_data(public_folder, database):
    tt_math_dir = path.join(environ["PUBLIC"], "Documents", public_folder)
    chdir(tt_math_dir)
    database_connection = connect(database)
    cursor = database_connection.cursor()
    cursor.execute('SELECT LNum, LScore FROM userLessonGrade_2 ORDER BY LNum ASC')
    lesson_and_score = cursor.fetchall()
    cursor.close()
    database_connection.close()
    return lesson_and_score

def sift_lesson_data(input_db, max_lessons):
    total_lessons = 0
    total_percentage = 0
    for lesson in input_db:
        split_lesson_data = [int(x) for x in lesson[1].split(" | ")[10:]]

        problem_correct = 0
        problem_wrong = 0

        for number in split_lesson_data:
            if number == 1:
                problem_correct += 1
            elif number == 0:
                problem_wrong += 1
        try:
            grade_percentage = get_average(
                            problem_correct, 
                            problem_correct + problem_wrong)
        except ZeroDivisionError:
            grade_percentage = 0
        total_lessons += 1
        total_percentage = total_percentage + grade_percentage

    progress = f"{total_lessons}/{max_lessons}"
    progress_percentage = f"{get_average(total_lessons, max_lessons)}%"
    grade_percentage = f"{get_average(total_percentage, total_lessons)}%"
    return progress, progress_percentage, grade_percentage