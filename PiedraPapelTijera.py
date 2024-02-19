import random

opciones = ["piedra", "papel", "tijera"]
seleccion_maquina = random.choice(opciones)

def proceso(opcion_usuario, seleccion_maquina):
    if opcion_usuario == seleccion_maquina:
        print("Empate")
    elif (opcion_usuario == "piedra" and seleccion_maquina == "tijera") or \
         (opcion_usuario == "papel" and seleccion_maquina == "roca") or \
         (opcion_usuario == "tijera" and seleccion_maquina == "papel"):
        print("¡Ganaste!")
    else:
        print("¡La máquina gana!")

print("Opciones disponibles: piedra, papel, tijera")
opcion_usuario = input("Elige tu opción: ").lower()

if opcion_usuario in opciones:
    print(f"La máquina eligió: {seleccion_maquina}")
    print(f"Tú elegiste: {opcion_usuario}")
    proceso(opcion_usuario, seleccion_maquina)
else:
    print("Opción no válida. Por favor, elige entre piedra, papel o tijera.")
