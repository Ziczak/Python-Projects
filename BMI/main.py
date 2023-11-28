from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")


def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    m = h / 100
    bmi = round(float(w / m ** 2), 1)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="You have a lower weight \n than that of a normal body!")

    elif 18.5 < bmi <= 25:
        label2.config(text="Normal!")
        label3.config(text="You are healthy as your \n weight is normal for your body!")

    elif 25 < bmi <= 30:
        label2.config(text="Overweight!")
        label3.config(text="You have a higher weight \n than what is considered normal! \n A doctor may advise to lose \n some weight for health reasons!")

    else:
        label2.config(text="Obese!")
        label3.config(text="Health may be at risk \n if you do not lose weight!")


image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

top = PhotoImage(file="Images/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

box = PhotoImage(file="Images/box.png")
Label(root, image=box).place(x=20, y=90)
Label(root, image=box).place(x=240, y=90)

scale = PhotoImage(file="Images/scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)

current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = (Image.open("Images/man.png"))
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 - size)
    secondimage.image = photo2


style = ttk.Style()
style.configure("TScale", background="white")

slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed,
                   variable=current_value)
slider.place(x=80, y=250)

current_value2 = tk.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider_changed2(event):
    Weight.set(get_current_value2())


style2 = ttk.Style()
style2.configure("TScale", background="white")

slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=slider_changed2,
                    variable=current_value2)
slider2.place(x=300, y=250)

Height = StringVar()
Weight = StringVar()
height_label = Label(root, text="Height (cm)", font='arial 10 bold', bg="#f0f1f5")
height_label.place(x=60, y=120)

weight_label = Label(root, text="Weight (kg)", font='arial 10 bold', bg="#f0f1f5")
weight_label.place(x=280, y=120)

height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=60, y=155)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=280, y=155)
Weight.set(get_current_value2())

secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(
    x=280, y=340)

label1 = Label(root, font="arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y=305)

label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280, y=430)

label3 = Label(root, font="arial 10", bg="lightblue")
label3.place(x=200, y=500)

root.mainloop()

