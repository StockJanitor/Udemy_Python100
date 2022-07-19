class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            print(f"your final score is {self.score}/{self.question_number+1}")
            return True
        else:
            return False

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("you got it right")
            self.score += 1
        else:
            print("good try")

        print(f"{self.score}/{self.question_number+1}\n")

    def next_question(self):
        # retrieve current number
        user_answer = input(
            f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?: "
        )
        self.check_answer(user_answer, self.question_list[self.question_number].answer)

        self.question_number += 1
