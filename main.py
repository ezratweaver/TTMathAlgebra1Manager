from database_manger import grab_lesson_data, sift_lesson_data

DATABASE_NAME = "algebra1dat"
PUBLIC_FOLDER = "TT Algebra 1"
TOTAL_LESSONS = 142

lesson_data = grab_lesson_data(
    PUBLIC_FOLDER, DATABASE_NAME)
progress, progress_percentage, grade_percentage, grade = sift_lesson_data(
    lesson_data, TOTAL_LESSONS)

print(f"Lessons: {progress} ({progress_percentage})")
print(f"Total Grade: {grade_percentage} ({grade})")