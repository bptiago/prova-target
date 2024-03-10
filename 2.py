def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        sequencia = fibonacci(num - 1)
        next_num = sequencia[-1] + sequencia[-2]
        sequencia.append(next_num)
        return sequencia

def numero_in_fibonnaci(num, sequencia):
    if num in sequencia:
        return print(f'{num} é da sequência de Fibonacci')
    else:
        return print(f'{num} não faz parte da sequência de Fibonacci')

sequencia = fibonacci(20) # Calculando 20 números de Fibonacci
numero_in_fibonnaci(10, sequencia) # Testando número 10 na sequência de Fibonacci