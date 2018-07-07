from adventure.dice_roll import roll
import collections
import socket


class TextGame:
    # Constants:
    class Stats:
        NAMES = ("pow", "brn", "soc", "agi")

        def __init__(self, pow=10):
            pass

    #####
    def __init__(self, char_name):
        self.character = char_name
        self.stats = self.Stats()


def sockets(host_tup=None):
    if not host_tup:
        host_tup = ("127.0.0.1", 5000)
    with socket.socket() as sock:
        sock.connect(host_tup)
        sock.send(b"my data")
