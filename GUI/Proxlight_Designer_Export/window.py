# -*- coding: utf-8 -*-
from tkinter import *


def btn_clicked():
    Take_input()

def Take_input():
    INPUT = entry0.get("1.0", "end-1c")
    print(INPUT)
    


window = Tk()

window.geometry("1000x573")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 573,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    255.0, 287.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    254.5, 315.5,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#ecfeff",
    highlightthickness = 0)

entry0.place(
    x = 36.0, y = 86,
    width = 437.0,
    height = 457)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    757.5, 315.5,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#cefcff",
    highlightthickness = 0)

entry1.place(
    x = 539.0, y = 86,
    width = 437.0,
    height = 457)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 337, y = 25,
    width = 116,
    height = 44)

window.resizable(False, False)
window.mainloop()
