from sqlite3 import connect
from os import path, environ, chdir
from get_average import get_average

def grab_math_data(public_folder, database, test=False):
    """
    Goes into the Teaching Textbooks local database and collects data from the
    LNum (Lesson Number) and LScore (Lesson Score) columns and returns a large list with
    tuples containing the data

    Args:
        public_folder (string): The name of the folder of the TT Math database
                                this is a agrument to possibly support other legacy
                                TT math versions
        database (string): The name of the database file the program will dig through
                            agrument for the same reason as previous
    Returns:
        A large list of tuples, the tuples contain the lesson number and lesson score
        stored as digits such as '1 | 1 | 0 | 1' to represent correct and wrong scores
        1's represent correct and 0's represent incorrect
    """
    tt_math_dir = path.join(environ["PUBLIC"], "Documents", public_folder)
    chdir(tt_math_dir)
    database_connection = connect(database)
    cursor = database_connection.cursor()
    sql_execute = "SELECT LNum, LScore FROM userLessonGrade_2 ORDER BY LNum ASC"
    if test:
        sql_execute = "SELECT QNum, QScore FROM userQuizGrade_2 ORDER BY QNum ASC"
    cursor.execute(sql_execute)
    number_and_score = cursor.fetchall()
    cursor.close()
    database_connection.close()
    return number_and_score

def sift_math_data(input_data, max_lessons):
    """
    Sifts through a predetermined style of data and comes up with statistical data
    for a students math performance
    
    Args:
        input_data (list): A large list of tuples, where the tuples contain the lesson
                            number and lesson score stored as digits in the style
                            as such '1 | 0 | 1 | 1...' for the algorithm the count
                            through
        max_lessons (int): A constant that contains the curriculums max amount of
                            lessons for proper tracking of progress
    Returns:
        Three variables: progress, progress_percentage, grade_percentage, grade 
        
        progress (string): A string showing the completed lessons, and the amount max
                            amount of lessons in the cirriculum EX. "23/142"
        progress_percentage (string): A string percentage of the cirriculum
                            completed, found by dividing the amount of lessons done by
                            the max amount of lessons
        grade_percentage (string): A string percentage of the total grade accuracy of
                            the student, found by dividing the correct score with the
                            incorrect and correct score combined all added into one
                            value, then divided by the complete amount of lessons
        grade (string): A string that reflects the academic grade equivalent of the
                        grade percentage
    """
    grade_to_percentage = {
    "A+": 97, "A": 93, "A-": 90,
    "B+": 87, "B": 83, "B-": 80,
    "C+": 77, "C": 73, "C-": 70,
    "D+": 67, "D": 63, "D-": 60,
    "F": 0,}
    total_lessons = 0
    total_percentage = 0
    for lesson in input_data:
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
        if problem_correct + problem_wrong > 0:
            total_lessons += 1
        total_percentage = total_percentage + grade_percentage

    for grade in sorted(grade_to_percentage.keys()):
        if get_average(total_percentage, total_lessons) >= grade_to_percentage[grade]:
            grade = grade
            break

    progress = f"{total_lessons}/{max_lessons}"
    progress_percentage = f"{get_average(total_lessons, max_lessons)}%"
    grade_percentage = f"{get_average(total_percentage, total_lessons)}%"
    return progress, progress_percentage, grade, grade_percentage

