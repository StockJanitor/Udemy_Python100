from data import question_data
from question_model import Question, QuizBrain

# initialize variables
question_bank = []

# save data to question_bank variable
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

# initialize quiz class
q = QuizBrain(question_bank)

# run each question
while not q.still_has_questions():
    q.next_question()
