from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.axisartist.axislines import Subplot
import numpy as np

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

        self.fig = plt.figure(figsize =(4, 4))
        self.ax = Subplot(self.fig, 111)
        self.fig.add_subplot(self.ax)
        self.ax.axis["top"].set_visible(False)
        self.ax.axis["right"].set_visible(False)

        self.graph_widget = FigureCanvasTkAgg(self.fig, self.window)
        self.graph_widget.get_tk_widget().place(relheight = 0.745, relwidth = 1, rely = 0.08)

        bottom_label = Label(self.window, bg = BG_COLOR, height = 80)
        bottom_label.place(relwidth = 1, rely = 0.825)

        Local_label = Label(bottom_label, text = 'Count of Locals', font = FONT_BOLD, width = 450, bg = BG_COLOR)
        Local_label.place(relx = 0.07, rely = 0.025, relheight = 0.03, relwidth = 0.12)

        Count = Text(bottom_label, width = 150)
        Count.place(relx = 0.20, rely = 0.027, relheight = 0.02, relwidth = 0.1)

        send_button = Button(bottom_label, text = "Generate Graph", font = FONT_BOLD, width = 20, bg = BG_GRAY, command = self.generate_graph)
        send_button.place(relx = 0.47, rely = 0.025, relheight = 0.03, relwidth = 0.15)

        send_button = Button(bottom_label, text = "Start", font = FONT_BOLD, width = 20, bg = BG_GRAY, command = self.start_algo)
        send_button.place(relx = 0.67, rely = 0.025, relheight = 0.03, relwidth = 0.12)

        line = Label(bottom_label, width = 450, bg = BG_GRAY)
        line.place(relwidth = 1, rely = 0.07, relheight = 0.012)

    def start_algo(self):
        pass

    def generate_graph(self):
        np.random.seed(19680801)
        x1 = [2, 4, 6, 8]
        y1 = [3, 5, 7, 9]
        self.ax.plot(x1, y1, color ='tab:blue')
        plt.draw()
        pass

if __name__ == "__main__":
    app = GUI()
    app.run()