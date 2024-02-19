
def es_anagrama(TRUE1, FALCE2):
    # Convierte palabras a minúsculas y ordena sus letras utilizando el comando "sorted" :b
    TRUE1 = sorted(TRUE1.lower())
    FALCE2 = sorted(FALCE2.lower())
    # compara palabras de forma ordenada :D
    return TRUE1 == FALCE2
# Los usos de cada palabra
print(es_anagrama("Roma", "Mora"))       # Debe MOSTRAR True
print(es_anagrama("Lacteo", "Coleta"))   # Debe MOSTRAR True
print(es_anagrama("Cara", "Arca"))       # Debe MOSTRAR True
print(es_anagrama("Comota", "muchaco"))  # Debe MOSTRAR False
