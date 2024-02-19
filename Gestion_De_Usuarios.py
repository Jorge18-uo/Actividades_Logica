def generar_correo_electronico(nombre, apellido, fecha_nacimiento, gmail='gmail.com'):
    # Obtener las primeras dos letras del nombre
    start_nombre = nombre[:2].lower()

    # Obtener las últimas dos letras del apellido
    end_apellido = apellido[-2:].lower()

    # Obtener el día de nacimiento
    dia_nacimiento = fecha_nacimiento.split('/')[0]

    # Generar el correo electrónico
    correo= f"{start_nombre}{end_apellido}{dia_nacimiento}@{gmail}"

    return correo

# Ejemplo de uso
nombre = "Jorge"
apellido = "Alberto"
fecha_nacimiento = "18/02/04"

correo = generar_correo_electronico(nombre, apellido, fecha_nacimiento)
print("este es tu corre: ",correo)
