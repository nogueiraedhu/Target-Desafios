def Fibonacci(numero):
    num1 = 0
    num2 = 1
    num3 = 0

    while (numero > num3):
        num3 = num1 + num2
        num1 = num2
        num2 = num3

    if (numero == num3 ):
        print('O número pertence a sequência de Fibonacci.')
    else:
        print('O número não pertence a sequência de Fibonacci.')


numero = float(input('Digite um número:'))
Fibonacci(numero)