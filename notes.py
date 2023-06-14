import turtle

wn = turtle.Screen()
wn.title("History notes")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-260, 300)
pen.write("Part 1;Portuguese map. Answers are D. because Portoguese was dominant in the age of colonization, as Vasco de Gama discovered india and they enslaved many in Africa.")
pen.goto(-260, 200)
pen.write("part 2: C; because europe was cooped up and decided to extend outward, sparking the fire that became the age of exploration and colonization.")
pen.goto(-260, 175)
pen.write("part 3: A, because Japan interacted with many porteguese because porteguese gave better weapons like guns, and the japanese gave silk, and pepper, which were very expensive at the time.")
pen.goto(-260, 150)
pen.write("Part 4: D, because slavery was common at the time and many africans were brought to brazil to work on cacao farms, for chocolate and other crop plantations.") 
pen.goto(-260, 400)
pen.write("HISTORY PART I: PORTEGUESE EXPLORATION")          
pen.goto(-260, 125)
pen.write("The portoguese enslaved many, and explored the farthest regions of the Earth. With this, they quickly changed how life was at that point, and time became HISTORY!!!!")
pen.goto(-230, 5)
pen.write("The portoguese were not exactly the strongest power, but they found the wormhole and cheat code for new routes, ideas, and production.")
pen.goto(-230, -20)
pen.write("Portugal quickly became very rich from their slaves and relationships, and their economy and wealth expanded. They would go on to capture brazil, which is why they speak portoguese there today, then they would get the highest instagram man; Cristiano RONALDO! SIUUU!")
pen.goto(-230, -50)
pen.write("Portugal explored many areas, the final areas are D, C, A, and D, and this is officialy TTTTHHHHHEEEEE EEEENNNNNNDDDD...    Coded with Python Turtle.")
pen.size=5

# Graphic
graphic = turtle.Turtle()
graphic.penup()
graphic.goto(-260, 60)
graphic.color("green")
graphic.shape("square")
graphic.shapesize(stretch_wid=5, stretch_len=5)


print ("Part 1: Portuguese map.")

print("Answers: DCAD")
print("D. because the protuguese were dominant")

while True:
       wn.update()
