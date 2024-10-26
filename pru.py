import pandas as pd
# def simple_interest(_i, _t, _c):
#
#     return _i * _c * _t
#
# print("Mencione las unidades en meses")
# i = int(input("¿Cuál es la tasa de interés?\n"))
# t = int(input("Cuál es el tiempo\n"))
# c = int(input("Cuál es el capital\n"))

class Simple_interest:
    def __init__(self, rate, capital, time):
        self.rate = rate
        self.capital = capital
        self.time = time

    def interest(self):
        return self.rate * self.capital * self.time

    def amount(self):
        return self.capital * (1 + self.rate * self.time)

