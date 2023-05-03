from sqlite3 import connect
from os import path, environ, chdir
from get_average import get_average

def grab_lesson_data(public_folder, database):
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
    cursor.execute('SELECT LNum, LScore FROM userLessonGrade_2 ORDER BY LNum ASC')
    lesson_and_score = cursor.fetchall()
    cursor.close()
    database_connection.close()
    return lesson_and_score

def sift_lesson_data(input_data, max_lessons):
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
        Three variables: progress, progress_percentage, grade_percentage 
        
        progress (string): A string showing the completed lessons, and the amount max
                            amount of lessons in the cirriculum EX. "23/142"
        progress_percentage (string): A string percentage of the cirriculum
                            completed, found by dividing the amount of lessons done by
                            the max amount of lessons
        grade_percentage (string): A string percentage of the total grade accuracy of
                            the student, found by dividing the correct score with the
                            incorrect and correct score combined all added into one
                            value, then divided by the complete amount of lessons
    """
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

    progress = f"{total_lessons}/{max_lessons}"
    progress_percentage = f"{get_average(total_lessons, max_lessons)}%"
    grade_percentage = f"{get_average(total_percentage, total_lessons)}%"
    return progress, progress_percentage, grade_percentage
