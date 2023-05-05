from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain ):
        self.quiz =quiz_brain
        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,width= 280 ,text="some question text",fill = THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")
        self.right = Button(image=right_img,highlightthickness=0,command=self.command_right)
        self.right.grid(row=2,column=0)

        self.wrong = Button(image=wrong_img,highlightthickness=0,command=self.command_wrong)
        self.wrong.grid(row=2,column=1)


        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
    def command_right(self):

        self.give_feedback(self.quiz.check_answer("True"))
    def command_wrong(self):

        self.give_feedback(self.quiz.check_answer("False"))





    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question )




