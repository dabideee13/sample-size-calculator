from typing import Any

from tkinter import Tk, Label, Button, Entry, StringVar


class Field:

    def __init__(self, app: Tk) -> None:
        self.app = app

    @property
    def total_population(self) -> None:
        return _entry(x=210, y=20)

    @property
    def confidence_level(self) -> None:
        return _entry(x=210, y=90)

    @property
    def margin_of_error(self) -> None:
        return _entry(x=210, y=160)

    @property
    def target_proportion(self) -> None:
        return _entry(x=210, y=230)

    @property
    def add_name(text: str) -> None:
        return Label(self.app, text=text)

    def _entry(self, text: str):
        return Entry(self.app, textvariable=StringVar()).place(x=x, y=y)


class App:

    def __init__(self, app: Tk, sample_size: int, **kwargs: Any) -> None:
        self.app = app()
        self.sample_size = sample_size
        self.kwargs = kwargs

    def entry_total_population(self) -> None:
        self.entry = Entry(self.app)
        self.entry.pack()

    def label_calculate(self, *args: Any) -> None:
        self.label = Label(self.app, text=f'Total sample size: {self.entry.get()}')
        self.label.pack()

    def button_calculate(self) -> None:
        self.button = Button(self.app, text="Calculate", command=self.label_calculate)
        self.button.pack()

    def run(self) -> None:
        self.setup()
        self.entry_total_population()
        self.button_calculate()
        self.app.bind('<Return>', self.label_calculate)
        self.app.mainloop()

    def setup(self) -> None:
        if 'title' in list(self.kwargs.keys()):
            self.app.title(self.kwargs['title'])
        self.app.geometry('500x300')
        self.app.resizable(False, False)

    # TODO: Handle string inputs here when user mistakenly inputs alphabets and special characters
    # TODO: Add output for inputs
    # TODO: Add logger


def main():
    app = App(Tk, 383, title="Sample Size Calculator")
    app.run()


if __name__ == '__main__':
    main()
