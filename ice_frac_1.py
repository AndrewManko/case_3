from turtle import *

def ice_frac(order, size):
    if order == 0:
      forward(size)

    else:
      ice_frac(order-1, size/2)
      left(90)
      ice_frac(order-1, size/3)
      right(180)
      ice_frac(order-1, size/3)
      left(90)
      ice_frac(order-1, size/2)

def main():
  up()
  goto(-100,0)
  down()
  ice_frac((int(input('Глубина рекурсии:'))), (int(input('Длина стороны:'))))
  mainloop()

if __name__ == '__main__':
    main()
