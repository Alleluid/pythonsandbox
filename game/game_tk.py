from tkinter import *


def cmd(func, *args, **kwargs):
    """
    Creates reference to function with specified params.
    :param func:
    :param args:
    :param kwargs:
    :return:
    """

    def wrapper():
        func(*args, **kwargs)

    return wrapper


def main():
    app = Tk()
    app.title("Game Alt")
    app.grid()
    root = Frame(app, size=1)
    root.grid()

    for i in range(5):
        btn_ok = Button(root, text="OK!" + str(i), command=cmd(print, "Yes!", i))
        btn_ok.grid()

    menubar = Menu(root)

    app_menu = Menu(menubar)
    app_menu.add_command(label="Save", command=cmd(print, "Tried to Save."))
    app_menu.add_command(label="Load", command=cmd(print, "Tried to Load"))
    app_menu.add_separator()
    app_menu.add_command(label="Quit", command=root.quit)

    menubar.add_cascade(label="App", menu=app_menu)

    app.config(menu=menubar)
    app.mainloop()


if __name__ == '__main__':
    main()
