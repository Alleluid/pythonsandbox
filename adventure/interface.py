from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Layout, Button


def demo(screen: Screen):
    def draw_points(tup_list, thin=False):
        last_x, last_y = -1, -1
        for x, y in tup_list:
            if last_x == last_y == -1:
                last_x = x
                last_y = y
                continue
            else:
                screen.move(last_x, last_y)
                screen.draw(x, y, thin=thin)
                last_x = x
                last_y = y

    while True:
        screen.print_at('hello, world', screen.width // 2 - 5, screen.height // 2)
        screen.print_at(f'{screen.width}, {screen.height}', screen.width // 2 - 5, screen.height // 2 - 3)
        screen.move(screen.width // 2, 0)
        screen.draw(0, screen.height // 2)
        screen.draw(screen.width // 2, screen.height)
        screen.draw(screen.width, screen.height // 2)
        screen.draw(screen.width // 2, 0)
        ev = screen.get_key()
        if ev == ord('q'):
            return 1
        if ev == ord('l'):
            draw_points([(5, 5), (10, 5), (10, 10), (10, 20), (20, 20), (30, 30)])
        # if screen.has_resized():
        #     return -1
        screen.refresh()


class UserInterface:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.setup()

    def setup(self):
        frame = Frame(self.screen, 120, 240, has_border=True)
        layout = Layout([1, 1, 1, 1])
        frame.add_layout(layout)

        layout.add_widget(Button("OK", print), 0)
        layout.add_widget(Button("Cancel", print), 3)




Screen.wrapper(UserInterface)
