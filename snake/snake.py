import turtle
from turtle import Turtle

# positions of blocks
POSITIONS = [(0,0), (-20,0), (-40,0)]

MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    # making the blocks and calling the postions 
    
    def __init__(self):     
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]
    
    def create_snake(self):
        for position in POSITIONS:   
           self.add_block(position)
    def move(self):
        for block_num in range(len(self.blocks) - 1, 0,-1):
                # finding the 2nd to last cordinates 
            x = self.blocks[block_num - 1].xcor()
            y = self.blocks[block_num - 1].ycor()
                # making the third block follow the 2nd blocks recenr cordinates
            self.blocks[block_num].goto(x, y)
        self.head.forward(MOVE)
    
    def up(self):         
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):  
        if self.head.heading() != UP:       
            self.head.setheading(DOWN)
    def left(self):    
        if self.head.heading() != RIGHT:     
            self.head.setheading(LEFT)
    def right(self): 
        if self.head.heading() != LEFT:        
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_block(self.blocks[-1].position())
    
    def add_block(self, position):
        self.block = Turtle()
        self.block.shape("square")
        self.block.color("white")
        self.block.penup()
        self.block.goto(position)
        self.blocks.append(self.block)
        
        # if your going right you cant go left
        # if your going left you cant go  right
        # if your going up you cant go down
        # if your going down you cant go up 


    