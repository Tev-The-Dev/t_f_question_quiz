from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for text in question_data:
    question_bank.append(Question(text['question'], text['correct_answer']))

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")