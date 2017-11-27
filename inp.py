from select import select


class character_io:
    """Gets a single character from standard input.  Does not echo to the
screen."""

    def __init__(self):
        self.impl = _gtyu()

    def getch(self): return self.impl()


class _gtyu:
    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            [i, o, e] = select([sys.stdin.fileno()], [], [], 0.5)
            if i:
                ch = sys.stdin.read(1)
            else:
                ch = None

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


char = character_io()
