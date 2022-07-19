class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number == len(self.question_list)

    def check_answer(self):
        pass

    def next_question(self):
        # retrieve current number
        input(
            f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?: "
        )
        self.question_number += 1
