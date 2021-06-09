from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))
        print(self.score)

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=('Arial', 30, 'normal'))
        self.color('white')
        self.goto(0, -50)
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))

