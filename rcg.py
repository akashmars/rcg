import pygame
import turtle
import sys
import time
import random
import json

# Screen
wn = turtle.Screen()
wn.title("Country Generator by CosmicPig")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

n = random.sample(["middle", "south", "north", "Exclave" , "United", "Isle of",] , 1)

m = random.sample(["Warter, Falbaes, Soam, Hulchy, Trintite, Redmont"], 1)








# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)


def generate_random_flag():
    # Flag
    flag_color = get_random_color()
    flag_shape = get_random_shape()
    flag_number = get_number_shape()
    generate_shape(flag_number, flag_shape, flag_color)

def load_flag_defs():
    f = open('flag_defs.json')
    flag_defs = json.load(f)
    f.close()
    return(flag_defs)

def load_flag_maps():
    f = open('flag_maps.json')
    flag_maps = json.load(f)
    f.close()
    return(flag_maps)

def get_flag_info(country):
    flag_defs = load_flag_defs()
    flag_maps = load_flag_maps()
    flag_id = flag_maps[country]
    flag_info = flag_defs[flag_id]
    return(flag_info)

def generate_shape(num, shape, color):
    b = (10,140)
    e = (100, 240)
    turtle.shape(shape)
    turtle.shapesize(stretch_len=8, stretch_wid=4)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.penup() 
    pen.goto(b)
    turtle.pendown()
    pen.goto(e)
    turtle.penup()

def generate_flag(num, shape, color):
    x = (5, 140)
    y = (80, 240)
    turtle.shape('square')
    turtle.shapesize(stretch_len=8, stretch_wid=4)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.penup() 
    pen.goto(x)
    turtle.pendown()
    pen.goto(y)
    turtle.penup()



def get_number_shape():
    sample_number = [1, 2, 3 ]
    random_number = random.sample(sample_number, 1)[0]
    return (random_number)


def get_random_shape():
    sample_shapes = ['square', 'arrow', 'triangle', 'circle', 'turtle']
    random_shape = random.sample(sample_shapes, 1)[0]
    return (random_shape)

def get_random_color():
    sample_colors = ['red', 'orange', 'yellow', 'lime green' ] 
    random_color = random.sample(sample_colors, 1)[0]
    return (random_color)

def adding_things():
    pen.clear()
    n = random.sample(["middle", "south", "north", "Exclave" , "United", "Democratic Republic of", "Kingdom of", "Isle of", "Republic of", "Slovant &",] , 1) [0]
    m = random.sample(["Warter", "Falbaes", "Soam", "Hulchy", "Trintite", "Redmont", "Tharzoan", "Cardanma", "Chitiku", "Fladista", "Maarnolie", ], 1)[0]
    country = "{} {}".format(n ,m)
    country = "Republic of Fladista"
    print(country)
    country_flag_info = get_flag_info(country)
    pen.goto(0,260)
    pen.write(n+m, align="center", font=("Courier", 24, "normal"))
    generate_random_flag()
    


pen.goto(0,220)
pen.write("Press W to generate a random country name!", align="center", font=("Courier", 24, "normal"))    


wn.listen()
wn.onkey(adding_things, "w")
wn.onkey(generate_random_flag, "g")

# Update

while True:
    wn.update()