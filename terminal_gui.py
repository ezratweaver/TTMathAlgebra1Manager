from math import floor

def create_progress_bar(progress):
    progress = int(progress[:-1])
    progress = floor(progress / 5)
    string = "=" * progress
    string = string + (" " * (20 - progress))
    string = "|" + string + "|"
    return string