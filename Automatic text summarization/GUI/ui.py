window = Tk()

    window.geometry("1005x571")
    window.configure(bg = "#ffffff")
    window.title("Auto Text Summarization")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 571,
        width = 1005,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"GUI/background.png")
    background = canvas.create_image(
        496.5, 291.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"GUI/img_textBox0.png")
    entry0_bg = canvas.create_image(
        253.5, 280.5,
        image = entry0_img)

    entry0 = Text(
        bd = 0,
        bg = "#feffff",
        highlightthickness = 0)

    entry0.place(
        x = 35.0, y = 56,
        width = 437.0,
        height = 457)

    entry1_img = PhotoImage(file = f"GUI/img_textBox1.png")
    entry1_bg = canvas.create_image(
        754.5, 280.5,
        image = entry1_img)

    entry1 = Text(
        bd = 0,
        bg = "#feffff",
        highlightthickness = 0)

    entry1.place(
        x = 536.0, y = 56,
        width = 437.0,
        height = 457)
    
    scale = Scale(
        window,
        from_=1,
        to=3,
        orient = 'horizontal',
        length = 150,)
    scale.place(x = 115, y = 5)
    
    label = Label(window, text = "Mức độ tóm tắt:")
    label.place(x = 25, y = 5)

    img0 = PhotoImage(file = f"GUI/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn_clicked(),
        relief = "flat")

    b0.place(
        x = 200, y = 525,
        width = 108,
        height = 39)
    
    window.resizable(False, False)
    window.mainloop()