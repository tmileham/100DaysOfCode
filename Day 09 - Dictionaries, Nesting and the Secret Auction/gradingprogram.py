student_scores = {
    "Tom": 100,
    "Chris:":82,
    "Keeley":99,
    "Oli":12,
    "Harry":45,
}

student_grade = {}

def exam_grade(score):
    if score > 90:
        return "Outstanding"
    elif score > 80:
        return "Exceeds Expectations"
    elif score > 70:
        return "Acceptable"
    else:
        return "Fail"


for key,value in student_scores.items():
        student_grade[key] = exam_grade(value)
    
print(student_grade)