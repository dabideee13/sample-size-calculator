from typing import Any

from tkinter import Tk, Label, Button, Entry, StringVar

from core import SampleSizeCalculator, SampleSizeParameter

app = Tk()
app.title("Sample Size Calculator")
app.geometry('500x300')
app.resizable(False, False)

total_population_label = Label(app, text="Total population: ")
total_population_label.place(x=10, y=20)
total_population_label.pack()

total_population_entry = Entry(app, textvariable=StringVar())
total_population_entry.place(x=210, y=20)
total_population_entry.pack()

confidence_level_label = Label(app, text="Confidence level: ")
confidence_level_label.place(x=10, y=90)
confidence_level_label.pack()

confidence_level_entry = Entry(app, textvariable=StringVar())
confidence_level_entry.place(x=210, y=90)
confidence_level_entry.pack()

margin_of_error_label = Label(app, text="Margin of error: ")
margin_of_error_label.place(x=10, y=160)
margin_of_error_label.pack()

margin_of_error_entry = Entry(app, textvariable=StringVar())
margin_of_error_entry.place(x=210, y=160)
margin_of_error_entry.pack()

target_proportion_label = Label(app, text="Target proportion: ")
target_proportion_label.place(x=10, y=230)
target_proportion_label.pack()

target_proportion_entry = Entry(app, textvariable=StringVar())
target_proportion_entry.place(x=210, y=230)
target_proportion_entry.pack()

calculator = SampleSizeCalculator()


def calculate(*args: Any) -> None:
    calculation_label = Label(
        app,
        text=(
            "Total sample size: "
            f"{calculator.calculate(int(total_population_entry.get()), float(confidence_level_entry.get()), float(margin_of_error_entry.get()), float(target_proportion_entry.get()))}"
        )
    )
    calculation_label.place(x=10, y=320)
    calculation_label.pack()


def button() -> None:
    calculation_button = Button(app, text="Calculate", command=calculate)
    calculation_button.place(x=10, y=300)
    calculation_button.pack()


button()
app.bind('<Return>', calculate)
app.mainloop()
