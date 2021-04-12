from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from random import shuffle

question_bank = []

for q in question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))

shuffle(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() and quiz.is_playing:
    quiz.next_question()

if quiz.score == len(question_bank):
    print("Well done. You've completed the quiz")

print(f"You're final score was {quiz.score} out of {len(question_bank)}")
