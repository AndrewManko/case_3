from turtle import *

def m(order, size):
    if order == 0:
      forward(size)
      
    else:
      m(order-1, size/3) 
      left(90)
      m(order-1, size/3)
      right(90)
      m(order-1, size/3)
      right(90)
      m(order-1, size/3*2)
      left(90)
      m(order-1, size/3)
      left(90)
      m(order-1, size/3)
      right(90)
      m(order-1, size/3)
      
def main():
  up()
  goto(-100,0)
  down()
  
  n = int(input('Глубина рекурсии:'))
  a = int(input('Длина стороны:'))
  m(n, a)

if __name__ == '__main__':
    main()
