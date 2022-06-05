# This and that
from cgitb import text
from hashlib import new
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#print(question_bank)
#print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Game over. You got {quiz.score} out of {quiz.question_number} questions")
print(f"That is {round((quiz.score / quiz.question_number)*100,1)}%")