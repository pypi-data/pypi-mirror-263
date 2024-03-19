class KomodoContext:
    def __init__(self):
        self.data = []

    def add(self, tag, content):
        self.data.append((tag, content))

    def extend(self, context):
        self.data.extend(context.data)

    def reset(self):
        self.data = []
