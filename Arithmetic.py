class Arithmetic():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        self.add = self.a + self.b
        return self.add

    def subtraction(self):
        self.sub = self.a - self.b
        return self.sub

    def multiplication(self):
        self.mul = self.a * self.b
        return self.mul

    def division(self):
        try:
            self.div = self.a / self.b
            return self.div
        except ZeroDivisionError:
            pass

if __name__ == '__main__':
    arithmetic = Arithmetic(8,9)