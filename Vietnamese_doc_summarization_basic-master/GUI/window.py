from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1005x571")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 571,
    width = 1005,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    496.5, 291.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    253.5, 280.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#feffff",
    highlightthickness = 0)

entry0.place(
    x = 35.0, y = 51,
    width = 437.0,
    height = 457)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    754.5, 280.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#feffff",
    highlightthickness = 0)

entry1.place(
    x = 536.0, y = 51,
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
    x = 200, y = 520,
    width = 108,
    height = 39)

window.resizable(False, False)
window.mainloop()
