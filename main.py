from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()

cursor.speed(0)

def move_forward():
  cursor.forward(5)

def move_backwards():
  cursor.backward(5)

def rotate_clockwise():
  cursor.right(10)

def rotate_counter_clockwise():
  cursor.left(10)

def clear():
  cursor.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
