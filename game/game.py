from tkinter import *


def game_loop():
    help_str = "Do a thing!"

    running = True
    while running:
        print(help_str)


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        for i in range(5):
            self.btn_ok = Button(self, text="OK!" + str(i), command=cmd(print, "Yes!", i))
            self.btn_ok.grid()


def cmd(func, *args, **kwargs):
    def wrapper():
        func(*args, **kwargs)

    return wrapper


def run_app():
    app = Application()
    app.master.title("OK!")
    app.master.config(width=1000, height=1000)
    app.mainloop()


if __name__ == '__main__':
    print("Ran Game.py")
    run_app()
