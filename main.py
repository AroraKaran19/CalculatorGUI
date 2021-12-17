# Calculator GUI
# Made By Karan Arora
# Date Started:- 2/2/2020
# Website - bit.ly/codewithk

import tkinter as tk
import webbrowser
from tkinter import messagebox
empty_box = 0
url = 'https://codewithk.wixsite.com/codewithk/forum/_help'
new = 1
box = ""
length_limit = True
max_length = 26
box_list = []

def no1():
    global box
    if length_limit == True:
        box = box + "1"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def no2():
    global box
    if length_limit == True:
        box = box + "2"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def no3():
    global box
    if length_limit == True:
        box = box + "3"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def no4():
    global box
    if length_limit == True:
        box = box + "4"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def no5():
    global box
    if length_limit == True:
        box = box + "5"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def no6():
    global box
    if length_limit == True:
        box = box + "6"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def no7():
    global box
    if length_limit == True:
        box = box + "7"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def no8():
    global box
    if length_limit == True:
        box = box + "8"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def no9():
    global box
    if length_limit == True:
        box = box + "9"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def no0():
    global box
    if length_limit == True and box[0] != "0":
        box = box + "0"
        for g in box:
            base_box = tk.Label(base, text=box)
            base_box.config(font=('helvetica', 20), bg="white", fg="black")
            base_canvas.create_window(300, 130, window=base_box)

def backspace():
    global box, base_box
    if (len(box)<=0):
        box = "0"
        base_box = tk.Label(base, text=box)
        base_box.config(font=('helvetica', 20), bg="white", fg="black")
        base_canvas.create_window(300, 130, window=base_box)
    box = box[:-1]
    for g in box:
        blank_box = tk.Label(base, text="                                                  ")
        blank_box.config(font=('helvetica', 20), bg="white", fg="white")
        base_canvas.create_window(300, 130, window=blank_box)

        base_box = tk.Label(base, text=box)
        base_box.config(font=('helvetica', 20), bg="white", fg="black")
        base_canvas.create_window(300, 130, window=base_box)

def add():
    global box
    if box[-1] == "+" or box[-1] == "-" or box[-1] == "/" or box[-1] == "*":
        messagebox.showerror("Error!", "You Can't use 2 Symbols at same time!")
    else:
        box = box + "+"
        base_box = tk.Label(base, text=box)
        base_box.config(font=('helvetica', 20), bg="white", fg="black")
        base_canvas.create_window(300, 130, window=base_box)

def sub():
    global box
    if box[-1] == "+" or box[-1] == "-" or box[-1] == "/" or box[-1] == "*":
        messagebox.showerror("Error!", "You Can't use 2 Symbols at same time!")
    else:
        box = box + "-"
        base_box = tk.Label(base, text=box)
        base_box.config(font=('helvetica', 20), bg="white", fg="black")
        base_canvas.create_window(300, 130, window=base_box)

def mul():
    global box
    if box[-1] == "+" or box[-1] == "-" or box[-1] == "/" or box[-1] == "*":
        messagebox.showerror("Error!", "You Can't use 2 Symbols at same time!")
    else:
        box = box + "*"
        base_box = tk.Label(base, text=box)
        base_box.config(font=('helvetica', 20), bg="white", fg="black")
        base_canvas.create_window(300, 130, window=base_box)

def div():
    global box
    if box[-1] == "+" or box[-1] == "-" or box[-1] == "/" or box[-1] == "*":
        messagebox.showerror("Error!", "You Can't use 2 Symbols at same time!")
    else:
        box = box + "/"
        base_box = tk.Label(base, text=box)
        base_box.config(font=('helvetica', 20), bg="white", fg="black")
        base_canvas.create_window(300, 130, window=base_box)

def calculate():
    total = 0
    """Calculates all values"""
    global box
    total = str(eval(box))
    answer = messagebox.askretrycancel("Answer:- ", "You Answer is:- {}".format(total))
    if answer == True:
        box = ""
        blank_box = tk.Label(base, text="                                                  ")
        blank_box.config(font=('helvetica', 20), bg="white", fg="white")
        base_canvas.create_window(300, 130, window=blank_box)

        base_box = tk.Label(base, text=empty_box)
        base_box.config(font=('helvetica', 20), bg="white", fg="black")
        base_canvas.create_window(300, 130, window=base_box)
    else:
        base.destroy()

def report():
    webbrowser.open(url, new=new)

def main():
    global base, base_canvas, base_box
    base = tk.Tk()
    base.title("Calculator")

    base_canvas = tk.Canvas(base, height=600, width=600, bg="#03fca9")
    base_canvas.pack()

    heading = tk.Label(base, text="Calculator\nMade By:- Karan Arora")
    heading.config(font=('helvetica', 15, "bold underline"), bg="#03fca9", fg="black")
    base_canvas.create_window(300, 30, window=heading)

    blank_box = tk.Label(base, text="                                                  ")
    blank_box.config(font=('helvetica', 20), bg="white", fg="white")
    base_canvas.create_window(300, 130, window=blank_box)

    base_box = tk.Label(base, text=empty_box)
    base_box.config(font=('helvetica', 20), bg="white", fg="black")
    base_canvas.create_window(300, 130, window=base_box)

    button_1 = tk.Button(base, text=" 1 ", height=3, width=9, command=no1).place(x=95, y=180)
    button_2 = tk.Button(base, text=" 2 ", height=3, width=9, command=no2).place(x=169, y=180)
    button_3 = tk.Button(base, text=" 3 ", height=3, width=9, command=no3).place(x=243, y=180)

    button_4 = tk.Button(base, text=" 4 ", height=3, width=9, command=no4).place(x=95, y=237)
    button_5 = tk.Button(base, text=" 5 ", height=3, width=9, command=no5).place(x=169, y=237)
    button_6 = tk.Button(base, text=" 6 ", height=3, width=9, command=no6).place(x=243, y=237)

    button_7 = tk.Button(base, text=" 7 ", height=3, width=9, command=no7).place(x=95, y=294)
    button_8 = tk.Button(base, text=" 8 ", height=3, width=9, command=no8).place(x=169, y=294)
    button_9 = tk.Button(base, text=" 9 ", height=3, width=9, command=no9).place(x=243, y=294)

    button_0 = tk.Button(base, text=" 0 ", height=3, width=30, command=no0).place(x=95, y=351)

    # Symbols Buttons

    addition_button = tk.Button(base, text=" + ", height=3, width=9, command=add).place(x=425, y=294)

    equal_button = tk.Button(base, text=" = ", height=3, width=20, command=calculate).place(x=350, y=351)

    subtraction_button = tk.Button(base, text=" - ", height=3, width=9, command=sub).place(x=350, y=294)

    multiplication_button = tk.Button(base, text=" x ", height=3, width=9, command=mul).place(x=425, y=235)

    division_button = tk.Button(base, text=" / ", height=3, width=9, command=div).place(x=350, y=235)

    # Backspace Button

    backspace_button = tk.Button(base, text=" <--- ", height=3, width=20, command=backspace).place(x=350, y=175)

    # Report Bugs Button

    report_button = tk.Button(base, text="(!) Report Bugs (!)", height=3, width=15, bg="#cc1e18", fg="white",
                              command=report).place(x=250, y=540)


    base.mainloop()

if __name__ == '__main__':
    main()
