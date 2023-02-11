# def sum(a,b):
#     total=a+b
#     return total
# x=int(input())
# y=int(input())
# n= sum(x,y)
# print(n)
import calendar
x=int(input("Enter year:"))
y=int(input("Enter month:"))

cal = calendar.month(x,y)
print(cal)
