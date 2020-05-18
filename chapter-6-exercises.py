import sys
import math


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def func_61(direction):
    direct = ["N", "E", "S", "W"]
    if direction == "N" or direction == "E" or direction == "S" or direction == "W":
        return direct[(direct.index(direction) + 1) % 4]


def func_62(number):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if (number < 7 and number > -1):
        return days[number]


def func_63(day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if day in days:
        return days.index(day)


def func_64(day, how_long):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[(func_63(day) + how_long) % 7]


def func_66(month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    if month in months:
        return days[months.index(month)]


def func_67(hours, minutes, seconds):
    return math.floor(hours * 3600 + minutes * 60 + seconds)


def func_69a(seconds):
    return math.floor(seconds / 3600)


def func_69b(seconds):
    return math.floor((seconds - func_69a(seconds) * 3600) / 60)


def func_69c(seconds):
    return math.floor(seconds - func_69a(seconds) * 3600 - func_69b(seconds) * 60)


def func_611(number1, number2):
    if number1 == number2:
        return 0
    else:
        if number1 > number2:
            return 1
        return -1


def func_612(leg1, leg2):
    return math.sqrt(leg1 ** 2 + leg2 ** 2)


def func_613a(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def func_613b(x1, y1, x2, y2):
    slope = func_613a(x1, y1, x2, y2)
    return y1 - slope * x1

def func_614(integer):
    if type(integer) == int:
        return integer % 2 == 0


def func_615(integer):
    if type(integer) == int: return not func_614(integer)

def func_616(f, n):
    return n % f == 0

def func_617(n, f):
    return func_616(f, n)

def func_618(f):
    return round(5/9 * (f - 32))

def func_619(c):
    return round(9/5 * c + 32)

