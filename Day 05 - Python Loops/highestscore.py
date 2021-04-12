#student_scores = [62,23,42,12,34,53,64,23,213]
### Recreating the min() // max() built in functions

highscore = 0

student_scores = input("Please enter all student scores, seperated by spaces :").split(" ")

for score in student_scores:
    score = int(score)
    if score > highscore:
        highscore = score

print(f"The highest score in the class is {highscore}")