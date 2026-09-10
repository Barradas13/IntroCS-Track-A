#Q1

import math

pi = math.pi
r = 7.5
area = round(pi * r ** 2, 2)
cir = round(pi * 2 * r, 2)

print(area)
print(cir)


#Q2

def CalculateFinalAmount(P, r, n, t):
    return P * (1 + r/n)**(n*t)

P = float(input("Give the principal amount: "))
r = float(input("Give the annual interest rate (give your answer in decimal, like if it is 100% give 1.0) "))
n = float(input("What is the number of times interest is compunded per year: "))
t = float(input("Give the number of years: "))

print(CalculateFinalAmount(P, r, n, t))


