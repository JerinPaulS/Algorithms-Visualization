from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.axisartist.axislines import Subplot
import numpy as np
import math
import random
import time

plt.ion()

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class GUI:

    def __init__(self):
        self.window = Tk()
        self.setup_main_window()

    def run(self):
        self.window.mainloop()

    def setup_main_window(self):
        self.window.title("Hill Climbing")
        self.window.resizable(width = False, height = False)
        self.window.configure(width = 1200, height = 700, bg = BG_COLOR)

        self.x = np.arange(0, 10, 0.1)
        self.y = np.sin(self.x) + np.random.normal(scale=0.1, size=len(self.x))
        self.y = np.array(self.y)
        self.xpoints = 0
        self.ypoints = 0
        self.point_color = 'bo'

        self.fig = plt.figure(figsize =(4, 4))
        self.ax = Subplot(self.fig, 111)
        self.hill, = self.ax.plot(self.x, self.y, 'black')
        self.fig.add_subplot(self.ax)

        self.graph_widget = FigureCanvasTkAgg(self.fig, self.window)
        self.graph_widget.get_tk_widget().place(relheight = 0.745, relwidth = 1, rely = 0.08)

        bottom_label = Label(self.window, bg = BG_COLOR, height = 80)
        bottom_label.place(relwidth = 1, rely = 0.825)

        Local_label = Label(bottom_label, text = 'Count of Locals', font = FONT_BOLD, width = 450, bg = BG_COLOR)
        Local_label.place(relx = 0.07, rely = 0.025, relheight = 0.03, relwidth = 0.12)

        self.Count = Text(bottom_label, width = 150)
        self.Count.place(relx = 0.20, rely = 0.027, relheight = 0.02, relwidth = 0.1)

        send_button = Button(bottom_label, text = "Generate Graph", font = FONT_BOLD, width = 20, bg = BG_GRAY, command = self.generate_graph)
        send_button.place(relx = 0.47, rely = 0.025, relheight = 0.03, relwidth = 0.15)

        send_button = Button(bottom_label, text = "Start", font = FONT_BOLD, width = 20, bg = BG_GRAY, command = self.start_algo)
        send_button.place(relx = 0.67, rely = 0.025, relheight = 0.03, relwidth = 0.12)

        line = Label(bottom_label, width = 450, bg = BG_GRAY)
        line.place(relwidth = 1, rely = 0.07, relheight = 0.012)

    def start_algo(self):
        if len(self.x) == 0:
            self.generate_graph()
        count = self.Count.get("1.0",'end-1c')
        local_count = 5
        if count.isdigit():
            local_count = int(count)
        if local_count < 1 or local_count > 5:
            local_count = 5
        current = random.randint(1, len(self.y) - 1)
        print("mid" + str(current))
        plt.cla()
        self.ax.plot(self.x, self.y, 'black')
        plt.draw()
        while (0 < current < len(self.y) - 1) and (self.y[current - 1] < self.y[current] or self.y[current + 1] < self.y[current]):
            print("Loop1")
            self.point_color = 'bo'
            self.xpoints, self.ypoints = current, current
            self.ax.plot(self.x[self.xpoints], self.y[self.ypoints], self.point_color)
            plt.draw()
            #time.sleep(5)
            plt.pause(0.0001)
            if self.y[current - 1] < self.y[current + 1] and self.y[current - 1] < self.y[current]:
                current -= 1
            elif self.y[current - 1] > self.y[current + 1] and self.y[current] > self.y[current + 1]:
                current += 1
            else:
                break
        self.xpoints, self.ypoints = current, current
        self.point_color = 'gs'
        self.ax.plot(self.x[self.xpoints], self.y[self.ypoints], self.point_color)
        self.ax.plot(self.x, self.y, 'black')
        plt.draw()
        print(self.y[current - 1], self.y[current], self.y[current + 1])
        print("Done")

    def generate_graph(self):
        plt.cla()
        self.x = np.arange(0, 10, 0.1)
        self.y = np.array(np.sin(self.x) + np.random.normal(scale=0.1, size=len(self.x)))
        self.hill, = self.ax.plot(self.x, self.y, 'black')
        plt.draw()

if __name__ == "__main__":
    app = GUI()
    app.run()
