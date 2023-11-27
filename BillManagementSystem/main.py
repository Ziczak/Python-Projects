from tkinter import *

root = Tk()
root.geometry("1000x455")
root.title("Bill Management")
root.resizable(False, False)


def Reset():
    entry_friedrice.delete(0, END)
    entry_mixdimsims.delete(0, END)
    entry_springrolls.delete(0, END)
    entry_assorteddrinks.delete(0, END)
    entry_hokkiennoodles.delete(0, END)
    entry_soupoftheday.delete(0, END)
    entry_stirfryvegetables.delete(0, END)


def Total():
    try:
        a1 = int(friedrice.get())
    except:
        a1 = 0

    try:
        a2 = int(mixeddimsims.get())
    except:
        a2 = 0

    try:
        a3 = int(springrolls.get())
    except:
        a3 = 0

    try:
        a4 = int(assorteddrinks.get())
    except:
        a4 = 0

    try:
        a5 = int(hokkiennoodles.get())
    except:
        a5 = 0

    try:
        a6 = int(soupoftheday.get())
    except:
        a6 = 0

    try:
        a7 = int(stirfryvegetables.get())
    except:
        a7 = 0

    c1 = 12 * a1
    c2 = 13 * a7
    c3 = 11 * a2
    c4 = 12 * a3
    c5 = 3 * a4
    c6 = 14 * a5
    c7 = 15 * a6

    lbl_total = Label(f2, font=('aria', 20, 'bold'), text="Total", width=16, fg='lightyellow', bg="black")
    lbl_total.place(x=25, y=50)

    entry_total = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
    entry_total.place(x=20, y=100)

    totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7
    string_bill = "$", str('%.2f' % totalcost)
    Total_bill.set(string_bill)


Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

f = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=85)

Label(f, text="Menu", font=("Gabriola", 40, "bold"), fg="black", bg="lightgreen").place(x=80, y=0)

Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Fried rice...................$12/plate", fg="black",
      bg="lightgreen").place(x=10, y=80)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Stir-fry vegetables..........$13/plate", fg="black",
      bg="lightgreen").place(x=10, y=110)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Mixed dim sims...............$11/plate", fg="black",
      bg="lightgreen").place(x=10, y=140)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Spring rolls..................$12/plate", fg="black",
      bg="lightgreen").place(x=10, y=170)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Assorted drinks..............$3/can", fg="black",
      bg="lightgreen").place(x=10, y=200)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Hokkien noodles..............$14/plate", fg="black",
      bg="lightgreen").place(x=10, y=230)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Soup of the day..............$15/bowl", fg="black",
      bg="lightgreen").place(x=10, y=260)

f2 = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=83)

Bill = Label(f2, text="Bill", font=('calibri', 20), bg="lightyellow")
Bill.place(x=120, y=10)

f1 = Frame(root, bd=5, height=370, width=300, relief=RAISED)
f1.pack()

friedrice = StringVar()
stirfryvegetables = StringVar()
mixeddimsims = StringVar()
springrolls = StringVar()
assorteddrinks = StringVar()
hokkiennoodles = StringVar()
soupoftheday = StringVar()
Total_bill = StringVar()

lbl_friedrice = Label(f1, font=("aria", 20, 'bold'), text="Fried rice", width=12, fg="blue4")
lbl_stirfryvegetables = Label(f1, font=("aria", 20, 'bold'), text="Stir-fry vegetables", width=12, fg="blue4")
lbl_mixdimsims = Label(f1, font=("aria", 20, 'bold'), text="Mix dim sims", width=12, fg="blue4")
lbl_springrolls = Label(f1, font=("aria", 20, 'bold'), text="Spring rolls", width=12, fg="blue4")
lbl_assorteddrinks = Label(f1, font=("aria", 20, 'bold'), text="Assorted drinks", width=12, fg="blue4")
lbl_hokkiennoodles = Label(f1, font=("aria", 20, 'bold'), text="Hokkien noodles", width=12, fg="blue4")
lbl_soupoftheday = Label(f1, font=("aria", 20, 'bold'), text="Soup of the day", width=12, fg="blue4")
lbl_friedrice.grid(row=1, column=0)
lbl_stirfryvegetables.grid(row=2, column=0)
lbl_mixdimsims.grid(row=3, column=0)
lbl_springrolls.grid(row=4, column=0)
lbl_assorteddrinks.grid(row=5, column=0)
lbl_hokkiennoodles.grid(row=6, column=0)
lbl_soupoftheday.grid(row=7, column=0)

entry_friedrice = Entry(f1, font=("aria", 20, 'bold'), textvariable=friedrice, bd=6, width=8, bg="lightpink")
entry_stirfryvegetables = Entry(f1, font=("aria", 20, 'bold'), textvariable=stirfryvegetables, bd=6, width=8,
                                bg="lightpink")
entry_mixdimsims = Entry(f1, font=("aria", 20, 'bold'), textvariable=mixeddimsims, bd=6, width=8, bg="lightpink")
entry_springrolls = Entry(f1, font=("aria", 20, 'bold'), textvariable=springrolls, bd=6, width=8, bg="lightpink")
entry_assorteddrinks = Entry(f1, font=("aria", 20, 'bold'), textvariable=assorteddrinks, bd=6, width=8, bg="lightpink")
entry_hokkiennoodles = Entry(f1, font=("aria", 20, 'bold'), textvariable=hokkiennoodles, bd=6, width=8, bg="lightpink")
entry_soupoftheday = Entry(f1, font=("aria", 20, 'bold'), textvariable=soupoftheday, bd=6, width=8, bg="lightpink")

entry_friedrice.grid(row=1, column=1)
entry_stirfryvegetables.grid(row=2, column=1)
entry_mixdimsims.grid(row=3, column=1)
entry_springrolls.grid(row=4, column=1)
entry_assorteddrinks.grid(row=5, column=1)
entry_hokkiennoodles.grid(row=6, column=1)
entry_soupoftheday.grid(row=7, column=1)

btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Reset",
                   command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Total",
                   command=Total)
btn_total.grid(row=8, column=1)

root.mainloop()
