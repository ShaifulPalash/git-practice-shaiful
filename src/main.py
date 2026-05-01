from datetime import date 
from utils import add, subtract, multiply, divide   

print('My Name: Shaiful Islam')
print("Today's Date:", date.today().strftime('%d-%m-%Y'))

print('Addition:', add(30, 10))
print('Subtraction:', subtract(30, 10))

print('Multiplication:', multiply(30, 10))

print('Division:', divide(30, 10))