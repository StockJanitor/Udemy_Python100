from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface





question_bank = []

# store question data into question bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    #Question Class object - q_text and q_answer
    new_question = Question(question_text, question_answer)

    # append each object into question_bank list
    question_bank.append(new_question)

# pass in question bank to QuizBrain
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
