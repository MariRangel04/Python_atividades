import math

a = int(input('digite o valor de a:'))
b = int(input('digite o valor de b:'))
c  = int(input('digite o valor de c:'))

potencia = pow(b,2)
delta = potencia - 4*a*(c)
raiz = math.sqrt(delta)

x1 = -b + raiz/2*a
x2 = -b -raiz/2*a

print('x1:',x1)
print('x2:', x2)

