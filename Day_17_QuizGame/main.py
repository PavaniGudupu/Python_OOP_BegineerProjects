from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    text = i['text']
    ans = i['answer']
    question = Question(text, ans)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")