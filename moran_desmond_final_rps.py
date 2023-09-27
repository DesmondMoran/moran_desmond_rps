# This file was created by: Desmond Moran

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
import winsound
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
sounds_folder = os.path.join(game_folder, 'sounds')

# sound
def play_rock():
    winsound.PlaySound(os.path.join(sounds_folder, 'rock.wav'), winsound.SND_ASYNC)
def play_paper():
    winsound.PlaySound(os.path.join(sounds_folder, 'paper.wav'), winsound.SND_ASYNC)
def play_scissors():
    winsound.PlaySound(os.path.join(sounds_folder, 'scissors.wav'), winsound.SND_ASYNC)

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

player_choice = ""

cpu_choice = ""

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
cpu_rock_instance = turtle.Turtle()

paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
cpu_paper_instance = turtle.Turtle()

scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
cpu_scissors_instance = turtle.Turtle()

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def cpu_show_rock(x,y):
    screen.addshape(cpu_rock_image)
    cpu_rock_instance.shape(cpu_rock_image)
    cpu_rock_instance.penup()
    cpu_rock_instance.setpos(x,y)

def show_paper(x,y):
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    screen.addshape(cpu_paper_image)
    cpu_paper_instance.shape(cpu_paper_image)
    cpu_paper_instance.penup()
    cpu_paper_instance.setpos(x,y)

def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

def cpu_show_scissors(x,y):
    screen.addshape(cpu_scissors_image)
    cpu_scissors_instance.shape(cpu_scissors_image)
    cpu_scissors_instance.penup()
    cpu_scissors_instance.setpos(x,y)


text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

show_rock(-300,0)
show_paper(0,0)
show_scissors(300,0)



# function that passes through wn onlick
def mouse_pos(x, y):
    print(cpu_select())
    cpu_picked = cpu_select()
    if collide(x,y,rock_instance,rock_w,rock_h):
        print("I collided with rock...")
        play_rock()
        if cpu_picked == "rock":
            cpu_show_rock(300,0)
            show_rock(-300,0)
            scissors_instance.hideturtle()
            paper_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("It is a Tie...", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "paper":
            cpu_show_paper(300,0)
            show_rock(-300,0)
            paper_instance.hideturtle()
            scissors_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("CPU Wins! Paper beats Rock", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "scissors":
            cpu_show_scissors(300,0)
            show_rock(-300,0)
            paper_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("You Win! Rock beats Scissors", False, "left", ("Arial", 24, "normal"))
    elif collide(x,y,paper_instance,paper_w,paper_h):
        print("I collided with paper")
        play_paper()
        if cpu_picked == "rock":
            cpu_show_rock(300,0)
            show_paper(-300,0)
            scissors_instance.hideturtle()
            rock_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("You Win! Paper beats Rock", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "paper":
            cpu_show_paper(300,0)
            show_paper(-300,0)
            scissors_instance.hideturtle()
            rock_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("It is a Tie...", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "scissors":
            cpu_show_scissors(300,0)
            show_paper(-300,0)
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("CPU Wins! Sciccors beat Paper", False, "left", ("Arial", 24, "normal"))
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        play_scissors()
        if cpu_picked == "rock":
            text.clear()
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            cpu_show_rock(300,0)
            show_scissors(-300,0)
            text.setpos(270,-180)
            text.write("CPU", False, "left", ("Arial", 24, "normal"))
            text.setpos(-355,-180)
            text.write("Player 1", False, "left", ("Arial", 24, "normal"))
            text.setpos(-200,150)
            text.write("CPU Wins! Rock beats Scissors", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "paper":
            text.clear()
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            cpu_show_paper(300,0)
            show_scissors(-300,0)
            text.setpos(270,-180)
            text.write("CPU", False, "left", ("Arial", 24, "normal"))
            text.setpos(-355,-180)
            text.write("Player 1", False, "left", ("Arial", 24, "normal"))
            text.penup()
            text.setpos(-200,150)
            text.write("You Win! Scissors beat Paper", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "scissors":
            text.clear()
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            cpu_show_scissors(300,0)
            show_scissors(-300,0)
            text.setpos(270,-180)
            text.write("CPU", False, "left", ("Arial", 24, "normal"))
            text.setpos(-355,-180)
            text.write("Player 1", False, "left", ("Arial", 24, "normal"))
            text.penup()
            text.setpos(-100,150)
            text.write("It is a Tie...", False, "left", ("Arial", 24, "normal"))
    else:
        print("pick somethign fool...")

text.penup()
text.setpos(0,150)
text.write("Choose rock or paper or scissors", False, "left", ("Arial", 24, "normal"))


screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last  

screen.mainloop()




