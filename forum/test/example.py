class Example():
    def __init__(self):
        self.apples = 5

    def trivial_double_apple(self, apples):
        try:
            return apples * 2
        except:
            raise ValueError