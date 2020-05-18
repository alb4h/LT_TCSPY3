import turtle
import math
no = turtle.Turtle()
no.color("blue", "red")
no.pensize(3)
no.pu()
wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

def func_51(day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[day]

def func_52(day, length):
    return_day = (day + length + 1) % 7
    return func_51(return_day)


def grading(grade):
    if(grade >= 75):
        return "First"
    elif(grade < 75 and grade >= 70):
        return "Upper Second"
    elif (grade < 70 and grade >= 60):
        return "Second"
    elif (grade < 60 and grade >= 50):
        return "Third"
    elif (grade < 50 and grade >= 45):
        return "F1 Supp"
    elif (grade < 45 and grade >= 40):
        return "F2"
    elif (grade < 40):
        return "F3"

def func_56():
    grades = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]
    for i in range(len(grades)):
        print(grading(grades[i]))

def draw_bar(t, height):
    t.pd()
    t.begin_fill()
    t.lt(90)
    t.fd(height)
    if (height < 0):
        t.pu()
        t.fd(-15)
        t.write(" " + str(height))
        t.bk(-15)
        t.pd()
    else:
        t.write(" " + str(height))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()
    t.pu()
    t.fd(10)

def func_59():
    no.setx(-300)
    xs = [48, 117, 200, 240, 160, 260, 220, -100]
    for i in range (len(xs)):
        height = xs[i]
        if(height >= 200):
            no.color("blue", "red")
        elif(height < 200 and height >= 100):
            no.color("blue", "yellow")
        elif(height < 100):
            no.color("blue", "green")
        draw_bar(no, height)

def func_510(leg1, leg2):
    return math.sqrt(leg1**2 + leg2**2)

def func_511(side, side2, side3):
    arr = [side, side2, side3]
    arr.sort()
    hypot = func_510(arr[0], arr[1])
    if abs(arr[2] - hypot) < 0.00000001:
        return True
    else:
        return False


wn.mainloop()