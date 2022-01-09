import turtle
gg=turtle.Turtle()
turtle.bgcolor("black")
gg.color("#4285F4","#4285F4")
gg.pensize(5)
gg.speed(8)



def google():
    gg.forward(120)
    gg.right(90)
    gg.circle(-150,50) #first circle for red color
    gg.color("#0F9D58")
    gg.circle(-150,100)
    gg.color("#F4B400")
    gg.circle(-150,60)
    gg.color("#DB4437","#DB4437")

    gg.begin_fill()
    gg.circle(-150,100)
    gg.right(90)
    gg.forward(50)
    gg.right(90)
    gg.circle(100,100)
    gg.right(90)
    gg.forward(50)
    gg.end_fill()

    gg.begin_fill()

#Second circle for yellow color
    gg.color("#F4B400","#F4B400")
    gg.right(180)
    gg.forward(50)
    gg.right(90)

    gg.circle(100,60)
    gg.right(90)
    gg.forward(50)
    gg.right(90)
    gg.circle(-150,60)
    gg.end_fill()

#third circle for green color
    gg.right(90)
    gg.forward(50)
    gg.right(90)
    gg.circle(100,60)
    gg.color("#0F9D58","#0F9D58")
    gg.begin_fill()
    gg.circle(100,100)
    gg.right(90)
    gg.forward(50)
    gg.right(90)
    gg.circle(-150,100)
    gg.right(90)
    gg.forward(50)
    gg.end_fill()

#draw the blue color
    gg.right(90)
    gg.circle(100,100)
    gg.color("#4285F4","#4285F4")
    gg.begin_fill()
    gg.circle(100,25)
    gg.left(115)
    gg.forward(65)  
    gg.right(90)
    gg.forward(42)
    gg.right(90)
    gg.forward(124)
    gg.right(90)
    gg.circle(-150,50)
    gg.right(90)
    gg.forward(50)

    gg.end_fill()
    gg.penup()


    gg.goto(-200,-250)
    gg.color("purple")
    # gg.write("By Idris Adeyemi", font=("couruer",32,"bold"))
    gg.hideturtle()
    gg.exitonclick()
google()