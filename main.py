import pyautogui
import time
import PySimpleGUI as sg
import keyboard
import threading
from PIL import Image, ImageTk, ImageGrab, ImageEnhance
import tkinter as tk


Dis = False

def MainFuncs():
    while not Dis:
        pyautogui.click(x1, y1)
        time.sleep(b)
        pyautogui.click(x2, y2)
        time.sleep(b)
        pyautogui.click(x3, y3)
        time.sleep(b)



def On():
    global Dis
    Dis = False
    threading.Thread(target=MainFuncs()).start

def Off():
    global Dis
    Dis = True

def Pos1():
    global x1
    global y1
    x, y = pyautogui.position()
    print(x, y)
    x1 = x
    y1 = y
    window.Element('_LISTBOX_1').Update(value=x)
    window.Element('_LISTBOX_2').Update(value=y)

def Pos2():
    global x2
    global y2
    x, y = pyautogui.position()
    print(x, y)
    x2 = x
    y2 = y
    window.Element('_LISTBOX_3').Update(value=x)
    window.Element('_LISTBOX_4').Update(value=y)
def Pos3():
    global x3
    global y3
    x, y = pyautogui.position()
    print(x, y)
    x3 = x
    y3 = y
    window.Element('_LISTBOX_5').Update(value=x)
    window.Element('_LISTBOX_6').Update(value=y)


keyboard.add_hotkey('Ctrl + Q' , lambda: Off())
keyboard.add_hotkey('Ctrl + S + 1' , lambda:Pos1())
keyboard.add_hotkey('Ctrl + S + 2' , lambda:Pos2())
keyboard.add_hotkey('Ctrl + S + 3' , lambda:Pos3())


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('AutoClicker 0.0.5')],
            [sg.Text('Задержка между действиями'), sg.Combo(('0.1','1', '2', '3') ,change_submits = False ) ],
            [sg.Text('Кол-во кликов (Хуйня, не работает)'), sg.InputCombo(('1','2', '3'))],
            [sg.Text('X'), sg.InputText(key='_LISTBOX_1'),sg.Text('Y'), sg.InputText(key='_LISTBOX_2'),sg.Button('1')],
            [sg.Text('X'), sg.InputText(key='_LISTBOX_3'),sg.Text('Y'), sg.InputText(key='_LISTBOX_4'),sg.Button('2')],
            [sg.Text('X'), sg.InputText(key='_LISTBOX_5'),sg.Text('Y'), sg.InputText(key='_LISTBOX_6'),sg.Button('3')],
            [sg.Button('Ok'), sg.Button('Start'), sg.Button('Quit') ],
            [sg.Text('Ctrl + Q (Stop)')],
            [sg.Text('Ctrl + S + X,Y')]]

# Create the Window
window = sg.Window('AutoClicker', layout)

canvas = sg.Canvas(window)


while True:
    event, values = window.read()
    if event == 'Start':
        On()
    elif event == 'Ok':
        print('You entered ', values[0])
        a = values[0]
        global b
        b = float(a)
    break
    sg.WIN_CLOSED()


window.close()

