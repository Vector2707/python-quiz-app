from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Interface:
    def __init__(self, brain: QuizBrain):
        self.brain = brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.label = Label(text='Score:0', bg=THEME_COLOR, fg='white', font=('Ariel', 15))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg='white')
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text='', fill='black',
                                                   font=('Ariel', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.right_button = Button(image=true_image, highlightthickness=0, command=self.right)
        self.right_button.grid(row=2, column=0)

        false_image = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.wrong)
        self.wrong_button.grid(row=2, column=1)

        self.get_new_questions()

        self.window.mainloop()

    def get_new_questions(self):
        if self.brain.still_has_questions():
            self.canvas.config(bg='white')
            question = self.brain.next_question()[0]
            self.canvas.itemconfig(self.canvas_text, text=question)

        else:
            self.canvas.itemconfig(self.canvas_text, text="You've Reached the end of the quiz")
            self.canvas.config(bg='white')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def right(self):
        check = self.brain.check_answer('true')
        self.feedback(check)

    def wrong(self):
        check = self.brain.check_answer('true')
        self.feedback(check)

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg='green')
            self.label.config(text=f'Score:{self.brain.score}')

        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_new_questions)
