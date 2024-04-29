x=float(input('enter first number: '))
y=float(input('enter second number: '))
output=0
operation= input('enter operation: add, subtract, multiplication, divide, power, ceilling')

if operation=='add':
    output=x+y
    print('product:',output)
elif operation=='subtract':
    output=x-y
    print('product:',output)
elif operation=='multiplication':
    output=x*y
    print('product:',output)
elif operation=='divide':
    output=x/y
    print('product:',output)
elif operation=='power':
    output=x**y
    print('product:',output)
elif operation=='ceilling':
    output=x//y
    print('product:',output)
else:
    print('invalid operation')

