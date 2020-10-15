import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import datetime

#Creation of the window
root = tkinter.Tk()
root.wm_title("Graph Project G3")

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def calc():
    print("Calc...")

def saveGraph():
    fig.savefig("backups/test" + str(datetime.datetime.now()) + ".png")


label = tkinter.Label(text="Enter your calculation here")
label.pack(side=tkinter.TOP)

entry = tkinter.Entry(text="Quit", justify='center')
entry.insert(0, "2sin(2 * pi * t)")
entry.pack(side=tkinter.TOP)

button = tkinter.Button(master=root, text="Create the graph", command=calc)
button.pack(side=tkinter.TOP)

#Calcul here
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

#Add to canvas
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)

button = tkinter.Button(master=root, text="Save this graph", command=saveGraph)
button.pack(side=tkinter.BOTTOM)


tkinter.mainloop()