from question import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    # We save the object of new question in question bank so we append it
    question_bank.append(new_question)


quiz = QuizBrain(question_bank) # حالا لیست سوالات question_bank در فایل quiz_brain داخل attribute question_list ذخیره میشود

while quiz.still_has_question(): #if quiz still has questions remaining:
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
