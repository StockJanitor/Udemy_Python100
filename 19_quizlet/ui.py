from tkinter import *
from quiz_brain import QuizBrain

# initiate variables
THEME_COLOR = "#375362"
path_true = r"C:\Users\Gumo\Desktop\Git\Class\Udemy_Python\19_quizlet\images\true.png"
path_false = r"C:\Users\Gumo\Desktop\Git\Class\Udemy_Python\19_quizlet\images\false.png"


class QuizInterface:
    # quiz_brain is QuizBrain type
    def __init__(self,quiz_brain: QuizBrain):
        # define input variable
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        #Score label
        self.score_label = Label(
            text="Score: 0", 
            fg="white", 
            bg=THEME_COLOR,
            font=("Arial",14))
        self.score_label.grid(row=0,column=1)

        # Canvas
        self.canvas=Canvas(width=300,height=250,bg="white")
        # question text
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",20,"italic"))
        # canvas location
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        #initialize image object
        true_image = PhotoImage(file=path_true)
        false_image = PhotoImage(file=path_false)
        #buttons
        self.true_button = Button(image = true_image,highlightthickness=0, command =self.true_pressed)
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)

        # run get next question
        self.get_next_question()

        self.window.mainloop()

    # run the next question and things
    def get_next_question(self):
        # canvas background
        self.canvas.config(bg="white")

        #check if quiz still has questions
        if self.quiz.still_has_questions():
            # track of score and print out
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()

            # change question text
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            # if no more questions, change text to end of question
            self.canvas.itemconfig(self.question_text,text="You've reached end of the quiz.")
            
            # diable the buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        # pass in True to check answer
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self):
        # pass in False to check answer
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # if right green bg
        if is_right:
            self.canvas.config(bg="green",highlightthickness=0)
        
        # else red bg
        else:
            self.canvas.config(bg="red",highlightthickness=0)
        
        # pause for 1 second
        self.window.after(1000,self.get_next_question)