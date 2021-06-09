from turtle import Turtle, Screen

STARTING_POSITION=[(0,0),(-20,0), (-40,0),(-60,0),(-80,0),(-100,0),(-120,0)]
MOVE_DISTANCE=20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
        self.game_on = True

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        #add new segment
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
            if self.segments[seg].xcor() > 300:
                self.game_on = False
        self.head.forward(MOVE_DISTANCE)
        return  self.game_on

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

