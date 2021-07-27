import pyautogui as gui
from time import sleep
from sys import exit as sysexit

add_x = 300
add_y = 240
timeline_x = 270
timeline_y = 500

try:
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))
    interval = int(input("Interval: "))
except ValueError:
    print("Invalid data!")
    sysexit()

if minutes < 8 or seconds < 0:
    print("Too short video!")
    sysexit()

currentMinutes = 0
currentSeconds = 0

def can_time_be_incremented():
    global currentMinutes, currentSeconds, minutes, seconds
    return currentMinutes < minutes or (currentMinutes == minutes and currentSeconds <= seconds)

def increment_time():
    global currentSeconds, currentMinutes
    currentSeconds += interval
    if currentSeconds >= 60:
        currentMinutes += currentSeconds // 60
        currentSeconds %= 60

def write_time():
    global currentMinutes, currentSeconds
    gui.write(str(currentMinutes))
    gui.press(["shift", ":"])
    gui.write(str(currentSeconds))
    gui.press(["shift", ":"])
    gui.write("00")

sleep(10)

while can_time_be_incremented():
    gui.click(x=timeline_x, y=timeline_y, clicks=3, interval=0.1)
    gui.press("backspace")
    write_time()
    gui.click(x=add_x, y=add_y)
    increment_time()

print("Finished!")