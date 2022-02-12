import tkinter as tk
from tkinter import *

window = Tk()
window.geometry('300x300')
window.title('Midpoint Calculator')

x1 = tk.Entry(window)
x1.pack()

x2 = tk.Entry(window)
x2.pack()

y1 = tk.Entry(window)
y1.pack()

y2 = tk.Entry(window)
y2.pack()

label1 = tk.Label(window,text='x1')
label1.pack()
label1.place(relx=0.2,rely=0.03,anchor='center')

label2 = tk.Label(window,text='x2')
label2.pack()
label2.place(relx=0.2,rely=0.09,anchor='center')


label3 = tk.Label(window,text='y1')
label3.pack()
label3.place(relx=0.2,rely=0.15,anchor='center')


label4 = tk.Label(window,text='y2')
label4.pack()
label4.place(relx=0.2,rely=0.22,anchor='center')

def calculate_midpoint():
    X_midpoint = (int(x1.get())/2) + (int(x2.get())/2)
    Y_midpoint = (int(y1.get())/2) + (int(y2.get())/2)

    result_X = tk.Label(window,text= '(' + str(X_midpoint))
    result_Y = tk.Label(window,text=str(Y_midpoint) + ')')
    result_X.pack()
    result_Y.pack()

result_button = tk.Button(window,text='Result',command=calculate_midpoint)
result_button.pack()

window.mainloop()
