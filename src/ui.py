from tkinter import Tk, Label, StringVar, Entry, Button
from main import main


def Calculate():
    def calculate_n0(z_score: float, target_proportion: float, margin_of_error: float) -> float:
        return (z_score ** 2) * target_proportion * (1 - target_proportion) / (margin_of_error ** 2)


    def calculate_n(n0: float, total_population) -> float:
        return n0 / (1 + (n0 - 1) / total_population)


    def calculate_sample_size(total_population: int, confidence_level: float, margin_of_error: float, target_proportion: float) -> int:
        z_score = calculate_z_score(confidence_level)
        n0 = calculate_n0(z_score, target_proportion, margin_of_error)
        return ceil(calculate_n(n0, total_population))


    def main():
        total_population = int(total_population_entry.get())
        confidence_level = float(confidence_level_entry.get())
        margin_of_error = float(margin_of_error_entry.get())
        target_proportion = float(target_proportion_entry.get())
        Label(text=f'{calculate_sample_size(total_population, confidence_level, margin_of_error, target_proportion)}', font="arial 20 bold").place(x=350, y=160)

    if __name__ == '__main__':
        main()


app = Tk()
app.title("Sample Size Calculator")
app.geometry("500x300")
app.resizable(False, False)
app.configure(background='light blue')

total_population = Label(app, text="Total population: ", font="arial 15", width=15)
confidence_level = Label(app, text="Confidence level: ", font="arial 15", width=15)
margin_of_error = Label(app, text="Margin of error: ", font="arial 15", width=15)
target_proportion = Label(app, text="Target proportion: ", font="arial 15", width=15)

total_population.place(x=10, y=20)
confidence_level.place(x=10, y=90)
margin_of_error.place(x=10, y=160)
target_proportion.place(x=10, y=230)

total_population_value = StringVar()
confidence_level_value = StringVar()
margin_of_error_value = StringVar()
target_proportion_value = StringVar()

total_population_entry = Entry(app, textvariable=total_population_value, font="arial 18", width=8).place(x=210, y=20)
confidence_level_entry = Entry(app, textvariable=confidence_level_value, font="arial 18", width=8).place(x=210, y=90)
margin_of_error_entry = Entry(app, textvariable=margin_of_error_value, font="arial 18", width=8).place(x=210, y=160)
target_proportion_entry = Entry(app, textvariable=target_proportion_value, font="arial 18", width=8).place(x=210, y=230)

Button(text="Calculate", font="arial 15", command=Calculate).place(x=350, y=20)
Button(app, text="Exit", command=lambda:exit(), font="arial 15", width=8).place(x=350, y=90)

app.mainloop()
