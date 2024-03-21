from math import sqrt as sqrt

class Calculator:
    def __init__(self):
        self.mem = 0

    def add(self, number):
        self.mem += number

    def substract(self, number):
        self.mem -= number

    def multiply(self, number):
        self.mem *= number

    def devide(self, number):
        if number != 0:
            self.mem /= number
        else:
            print ('Devision by zero is an error')

    def root(self, number):
        self.mem = sqrt(number)

    def reset(self):
        self.mem = 0