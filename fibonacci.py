# Función para generar los primeros n numeros de la sucesión de Fibonacci
def i(n):
    fib = [0, 1]  # Inicializamos con los dos primeros numeros de la secuencia

    while len(fib) < n:
        sig_number = fib[-1] + fib[-2]
        fib.append(sig_number)

    return fib[:n]

# Imprime los primeros 50 numeros de la sucesión de Fibonacci
n = 50
fibonacci_secuencia = i(n)

print("Los primeros 50 numeros de la sucesión de Fibonacci son:")
print(fibonacci_secuencia)