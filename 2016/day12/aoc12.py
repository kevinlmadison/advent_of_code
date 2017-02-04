import re

# part 1


class Registry:
    def __init__(self):
        self.regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

    def copy(self, val, reg):
        self.regs[reg] = val
