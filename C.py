import turtle
t = turtle.Turtle()
for i in range (180) :
    t.speed(0)
    t.color('#278bc0')
    t.circle(190 - i, 90)
    t.left(90)
    t.color('#E38BC0')
    t.circle(190 - i, 90)
    t.left(18)