# A simple script to do MAthematical calaculation
from pywebio.input import *
from pywebio.output import *
def mathemticaloperation():
    a = input("Enter the first number：", type=FLOAT)
    b = input("Enter the second number：", type=FLOAT)
    c=0
    operation = radio("Choose one operation", options=['+', '*', '/', '%'])
    operation_name=""
    match operation:
        case "+":
            operation_name="Addition"
            c=a+b
        case "*":
            operation_name="Multiplication"
            c=a*b
        case "/":
            operation_name="Division"
            c=a/b
        case "%":
            operation_name="Modulus"
            c=a%b
        
    put_text('The operation selected is: %s. and the output is: %.1f' % (operation_name, c))
    
if __name__ == '__main__':
    mathemticaloperation()