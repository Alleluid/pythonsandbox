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
        self.create_widgets(master)


    def create_widgets(self, master):
        for i in range(5):
            btn_ok = Button(self, text="OK!" + str(i), command=cmd(print, "Yes!", i))
            btn_ok.grid()

        menubar = Menu(self)

        app_menu = Menu(menubar)
        app_menu.add_command(label="Quit", command=self.quit)

        menubar.add_cascade(label="App", menu=app_menu)
        self.config(menu=menubar)



def cmd(func, *args, **kwargs):
    def wrapper():
        func(*args, **kwargs)

    return wrapper


def run_app():
    app = Application()
    app.master.title("OK!")
    app.master.geometry("1200x720")
    app.master.config(width=1000, height=1000)
    app.mainloop()


if __name__ == '__main__':
    print("Ran Game.py")
    run_app()
