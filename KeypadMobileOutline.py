import turtle

t = turtle.Turtle()

t.penup()
t.goto(-100,200)
t.pendown()
t.fd(200)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(400)

t.rt(180)
t.fd(200)
t.lt(90)
t.penup()
t.fd(10)
t.lt(90)
t.pendown()
t.begin_fill()
t.fd(190)
t.rt(90)
t.fd(180)
t.rt(90)
t.fd(190)
t.rt(90)
t.fd(180)
t.end_fill()

t.lt(90)
t.penup()
t.fd(10)
t.pendown()
t.fd(180)
t.lt(90)
t.fd(180)
t.lt(90)
t.fd(180)
t.lt(90)
t.fd(180)

t.rt(180)
t.fd(60)
t.rt(90)
t.fd(180)
t.lt(90)
t.fd(60)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(60)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(180)
t.fd(180)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(180)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(180)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(180)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(180)

turtle.done()