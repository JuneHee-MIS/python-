import turtle as t
import random as r
s=r.randint(1,5)
t.pensize(s)
t.color('green')
t.shape('turtle')
t.speed(0)

for x in range(1000):
    a=r.randint(1,360)
    t.setheading(a)
    b=r.randint(1,20)
    t.fd(b)
    
