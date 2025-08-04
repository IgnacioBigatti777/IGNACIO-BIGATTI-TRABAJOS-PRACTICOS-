# Lista de 15 superhéroes
lista_superheroes = [
    "Iron Man", "Spider-Man", "Hulk", "Thor", "Viuda Negra",
    "Ojo de Halcón", "Pantera Negra", "Doctor Strange", "Bruja Escarlata",
    "Ant-Man", "Wasp", "Falcon", "Capitán América", "Winter Soldier", "Vision"
]

# Función recursiva que devuelve "Sí" o "No"
def contiene_capitan(lista, posicion=0):
    if posicion == len(lista):
        return "No"
    if lista[posicion] == "Capitán América":
        return "Sí"
    return contiene_capitan(lista, posicion + 1)

# Función recursiva para mostrar los superhéroes
def mostrar_superheroes(lista, pos=0):
    if pos < len(lista):
        print(lista[pos])
        mostrar_superheroes(lista, pos + 1)

# Verificación
respuesta = contiene_capitan(lista_superheroes)
print("¿Capitán América está en la lista?", respuesta)

# Listado
print("Superhéroes en la lista:")
mostrar_superheroes(lista_superheroes)
