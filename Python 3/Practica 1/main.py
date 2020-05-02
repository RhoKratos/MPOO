def fibonacci(num):
    a = 0
    b = 1
    
    for i in range(num):
        c = b+a
        a = b
        b = c
        
    return a
    
def factorial(num):
    while num != 1:
        return (num * factorial(num-1))
    return 1
    
print('Práctica 1 MPOO.')
print('Sucesiones.')
numero = int(input('Introduce un indice de la sucesión que deseas.'))
print('¿Que sucesion desas realizar?')
print('\t1.-Fibonacci.')
print('\t2.-Factorial.')
opcion = int(input())
if opcion == 1: 
    r = fibonacci(numero)
    print (r)

if opcion == 2: 
    r = factorial(numero)
    print (r)

