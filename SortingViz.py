from tkinter import *
from tkinter import ttk
import random
import time

win  =  Tk()
win.title('Sorting Algorithm Visualisation')
WIDTH = 620
HEIGHT = 835
CANVAS_H = 500
win.maxsize(HEIGHT, WIDTH)
win.minsize(HEIGHT, WIDTH)
win.config(bg = 'black')
selected_alg = StringVar()
data = []
color = []

def drawData():
    global data, color
    canvas.delete("all")
    c_height  =  CANVAS_H
    c_width  =  700
    x_width  =  c_width / (len(data) + 1)
    offset  =  25
    spacing  =  10
    normalizedData  =  [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0  =  i * x_width + offset + spacing
        y0  =  c_height - height * 410
        x1  =  (i + 1) * x_width + offset
        y1  =  c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill = color[i])
        canvas.create_text(x0 + 2, y0, anchor = SW, text = str(data[i]))
    win.update_idletasks()


def Generate():
    #print('Alg Selected: ' + selected_alg.get())
    global data, color
    data = []
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 20
    try:
        size = int(sizeEntry.get())
    except:
        size = 20

    if minVal < 0:
        minVal = 0
    if maxVal > 150:
        maxVal = 150
    if size > 50 or size < 3:
        size = 50
    if minVal > maxVal:
        minVal, maxVal = maxVal, minVal
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))
    color = ["#116562"] * len(data)

    drawData()

def Sort():
    global data
    if len(data) == 0:
        return
    algorithm = selected_alg.get()
    if algorithm == "Bubble Sort":
        bubble_sort()
    if algorithm == "Selection Sort":
        selection_sort()
    if algorithm == "Insertion Sort":
        insertion_sort()

def bubble_sort():
    global data, color

    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            color = ["#116562"] * len(data)
            if data[j] > data[j + 1] :
                data[j], data[j + 1] = data[j + 1], data[j]
                color[j] = "green"
                color[j + 1] = "green"
                drawData()
                time.sleep(0.6)
    return

def selection_sort():
    global data, color

    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            color = ["#116562"] * len(data)
            if data[min_idx] > data[j]:
                min_idx = j
                color[j] = "yellow"
                drawData()
                time.sleep(0.6)
        data[i], data[min_idx] = data[min_idx], data[i]
        color[i] = "green"
        color[min_idx] = "green"
        drawData()
        time.sleep(0.6)
    return

def insertion_sort():
    global data, color
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j] :
            color = ["#116562"] * len(data)
            data[j + 1] = data[j]
            j = j - 1
            color[i] = "yellow"
            color[j] = "cyan"
            color[j + 1] = "cyan"
            drawData()
            time.sleep(0.6)
        data[j + 1] = key
        color[i] = "green"
        color[j + 1] = "green"
        drawData()
        time.sleep(0.6)
    return

UI_frame  =  Frame(win, width = WIDTH, height = 200, bg = 'grey')
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

canvas  =  Canvas(win, width = 750, height = CANVAS_H, bg = 'white')
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

Label(UI_frame, text = "Algorithm: ", bg = 'grey').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
algMenu  =  ttk.Combobox(UI_frame, textvariable = selected_alg, values = ['Bubble Sort', 'Selection Sort', 'Insertion Sort'])
algMenu.grid(row = 0, column = 1, padx = 5, pady = 5)
algMenu.current(0)
Button(UI_frame, text = "Generate", command = Generate, font=('Times', 20), padx = 5, pady = 5, bg = '#5a7abc', fg = 'black', activebackground = 'green', activeforeground = 'white').grid(row = 0, column = 3, padx = 5, pady = 5)
Button(UI_frame, text = "Sort", command = Sort, font=('Times', 20), padx = 5, pady = 5, bg = '#5a7abc', fg = 'black', activebackground = 'green', activeforeground = 'white').grid(row = 0, column = 5, padx = 5, pady = 5)

Label(UI_frame, text = "Size ", bg = 'grey').grid(row = 1, column = 0, padx = 2, pady = 2, sticky = W)
sizeEntry  =  Entry(UI_frame)
sizeEntry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

Label(UI_frame, text = "Min Value ", bg = 'grey').grid(row = 1, column = 2, padx = 5, pady = 5, sticky = W)
minEntry  =  Entry(UI_frame)
minEntry.grid(row = 1, column = 3, padx = 5, pady = 5, sticky = W)

Label(UI_frame, text = "Max Value ", bg = 'grey').grid(row = 1, column = 4, padx = 5, pady = 5, sticky = W)
maxEntry  =  Entry(UI_frame)
maxEntry.grid(row = 1, column = 5, padx = 5, pady = 5, sticky = W)

win.mainloop()
