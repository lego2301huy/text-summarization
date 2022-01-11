from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    -255.0, -74.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f1f9ef",
    highlightthickness = 0)

entry0.place(
    x = -425, y = -274,
    width = 340,
    height = 398)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    238.0, -74.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#a2f5dc",
    highlightthickness = 0)

entry1.place(
    x = 68, y = -274,
    width = 340,
    height = 398)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = -425, y = -340,
    width = 96,
    height = 36)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = -181, y = -340,
    width = 96,
    height = 36)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = -303, y = -340,
    width = 96,
    height = 36)

window.resizable(False, False)
window.mainloop()
