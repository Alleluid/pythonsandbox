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
    root = Tk()
    root.config()
    root.title("Game Alt")

    for i in range(5):
        btn_ok = Button(root, text="OK!" + str(i), command=cmd(print, "Yes!", i))
        btn_ok.grid()

    root.mainloop()


if __name__ == '__main__':
    main()
