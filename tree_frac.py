from turtle import *

def tree_frac(d, n):
    if n == 0:
        return
        
    forward(d)
    right(30)
    tree_frac(d / 2, n - 1)
    left(60)
    tree_frac(d / 2, n - 1)
    right(30)
    backward(d)

def main():
    left(90)
    
    d = int(input('Длина стороны'))
    n = int(input('Длина рекурсии'))
    tree_frac(d,n)

if __name__ == '__main__':
    main()
