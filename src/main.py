from tkinter import Tk, Label, StringVar, Entry, Button, Frame
from typing import Any
from core import SampleSizeCalculator, SampleSizeParameter

app = Tk()
app.title("Sample Size Calculator")
app.geometry("600x300")
app.resizable(False, False)
# app.configure(background='light blue')

total_population = Label(app, text="Total population: ", font="arial 15", width=15)
confidence_level = Label(app, text="Confidence level: ", font="arial 15", width=15)
margin_of_error = Label(app, text="Margin of error: ", font="arial 15", width=15)
target_proportion = Label(app, text="Target proportion: ", font="arial 15", width=15)
result_lbl = Label(app, text="Result", font="arial 15", width=15)

total_population.place(x=10, y=20)
confidence_level.place(x=10, y=50)
margin_of_error.place(x=10, y=80)
target_proportion.place(x=10, y=110)
result_lbl.place(x=380, y= 20)

total_population_input = StringVar()
confidence_level_input = StringVar()
margin_of_error_input = StringVar()
target_proportion_input = StringVar()
result_input = StringVar()

total_population_entry = Entry(app, textvariable=total_population_input, font="arial 16", width=12).place(x=180, y=20)
confidence_level_entry = Entry(app, textvariable=confidence_level_input, font="arial 16", width=12).place(x=180, y=50)
margin_of_error_entry = Entry(app, textvariable=margin_of_error_input, font="arial 16", width=12).place(x=180, y=80)
target_proportion_entry = Entry(app, textvariable=target_proportion_input, font="arial 16", width=12).place(x=180, y=110)
result_entry = Entry(app, textvariable=result_input, font="arial 20", width=11).place(x=380, y=50, height=90)

calculator = SampleSizeCalculator()


def calculate(*args: Any) -> None:
    x = int(total_population_input.get())
    y= float(confidence_level_input.get())
    z = float(margin_of_error_input.get())
    b = float(target_proportion_input.get())

    output = calculator.calculate(x,y,z,b)
    result_input.set(output)


def reset():
    total_population_input.set("")
    confidence_level_input.set("")
    margin_of_error_input.set("")
    target_proportion_input.set("")
    result_input.set("")


def exit():
    app.destroy()


def button() -> None:
	calculation_button = Button( text='Calculate', font=('arial', 12, 'bold'), command=calculate, bd=8, pady=10, padx=10, width=6).place(x = 20, y=160)
	reset_button = Button(text='Reset', font=('arial', 12, 'bold'), command=reset, bd=8, pady=10, padx=10, width=6).place(x=120, y=160)
	exit_button = Button(text='Quit', font=('arial', 12, 'bold'),command=exit, bd=8, pady=10, padx=10, width=6).place(x=220, y=160)


button()
app.bind('<Return>', calculate)
app.mainloop()
