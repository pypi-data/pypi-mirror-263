class KomodoContext:
    def __init__(self):
        self.data = []

    def add(self, tag, content):
        self.data.append((tag, content))

    def clear(self):
        self.data = []
