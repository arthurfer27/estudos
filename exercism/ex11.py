"""Functions for organizing and calculating student exam scores."""
def round_scores(student_scores):
    ordered_list=[]
    for scores in student_scores:
        ordered_list.append(round(scores))
    return ordered_list


def count_failed_students(student_scores):
    i = 0
    for students in student_scores:
        if students <= 40:
            i += 1
        else: continue
    return i


def above_threshold(student_scores, threshold):
    best_students = []
    for student in student_scores:
        if student >= threshold:
            best_students.append(student)
        else: continue
    return best_students

def letter_grades(highest):
    interval = (highest - 40) // 4
    return [41, 41 + interval, 41 + 2 * interval, 41 + 3 * interval]
    
def student_ranking(student_scores, student_names):
    rankings = []
    for rank, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        rankings.append(f"{rank}. {name}: {score}")
    return rankings

def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []
