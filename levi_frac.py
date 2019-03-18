from turtle import *


def levi_frac(order, size):
    if order == 0:
        forward(size)

    else:
        levi_frac(order - 1, size / 3)
        right(90)
        levi_frac(order - 1, size / 3)
        left(90)


def main():
    up()
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    levi_frac(n, a)
    mainloop()


if __name__ == '__main__':
    main()
