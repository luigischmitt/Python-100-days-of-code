THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:    

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Geo Quiz")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        # --------------- Canvas --------------- 
        self.canvas = Canvas(width=400, height=350, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.quote_text = self.canvas.create_text(200, 150, text="Quotes goes Here!", width=250, font=("Arial", 20, "normal"), fill="black")
        
        # --------------- Buttons --------------- 
        true_img = PhotoImage(file="Python-100-days-of-code/day 34/images/true.png")
        false_img = PhotoImage(file="Python-100-days-of-code/day 34/images/false.png")
        self.true_but = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.false_but = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.true_but.grid(column=0, row=2, pady=20)
        self.false_but.grid(column=1, row=2, pady=20)

        # --------------- Score Label --------------- 
        self.score_label = Label(text=f"Score: 0", font=("Arial", 20, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        







