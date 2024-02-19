# El bucle for recorre los números del 1 al 100 (incluyendo el 1 pero excluyendo el 101 por que si no lo contaria xD).
for numero in range(1, 101):
    # Verifica si el número es divisible por 3 y 5.
    if numero % 3 == 0 and numero % 5 == 0:
        # Si es divisible por 3 y 5, muestra "FizzBuzz".
        print("FizzBuzz")
    # Si no es divisible por 3 y 5, verifica si es divisible solo por 3.
    elif numero % 3 == 0:
        # Si es divisible solo por 3, muestra "Fizz".
        print("Fizz")
    # Si no es divisible por 3, verifica si es divisible solo por 5.
    elif numero % 5 == 0:
        # Si es divisible solo por 5, muestra "Buzz".
        print("Buzz")
    # Si no es divisible por 3 ni por 5, muestra el número.
    else:
        print(numero)
