
from superheroes_list import superheroes
from list_ import List
from cola import Queue

superheroes_list = List(superheroes) 

# criterios de ordenamiento
superheroes_list.add_criterion("nombre", lambda p: p["name"])
superheroes_list.add_criterion("nombre_real", lambda p: p["real_name"])
superheroes_list.add_criterion("aparicion", lambda p: p["first_appearance"])

# 1. Ordenar por nombre
print("1. Personajes ordenados por nombre:")
superheroes_list.sort_by_criterion("nombre")
superheroes_list.show()

# 2. Buscar posiciones
print("\n2. Posiciones de personajes:")
superheroes_list.sort_by_criterion("nombre")
pos_thing = superheroes_list.search("The Thing", "name")
pos_rocket = superheroes_list.search("Rocket Raccoon", "name")
print(f"- The Thing está en la posición: {pos_thing}")
print(f"- Rocket Raccoon está en la posición: {pos_rocket}")

# 3. Villanos
print("\n3. Lista de villanos:")
lista_villanos = List([p for p in superheroes_list if p["is_villain"]])
lista_villanos.sort_by_criterion("nombre")
lista_villanos.show()

# 4. Villanos antes de 1980 en una cola
print("\n4. Villanos que aparecieron antes de 1980:")
cola_villanos = Queue()
for villano in lista_villanos:
    cola_villanos.arrive(villano)

villanos_antes_1980 = List()
while cola_villanos.size() > 0:
    villano = cola_villanos.attention()
    if villano["first_appearance"] < 1980:
        villanos_antes_1980.append(villano)

villanos_antes_1980.sort_by_criterion("nombre")
villanos_antes_1980.show()

# 5. Superhéroes con ciertos prefijos
print("\n5. Superhéroes que empiezan con Bl, G, My o W:")
prefijos = ["Bl", "G", "My", "W"]
heroes_filtrados = List()

for personaje in superheroes_list:
    if not personaje["is_villain"]:
        if any(personaje["name"].startswith(pref) for pref in prefijos):
            heroes_filtrados.append(personaje)

heroes_filtrados.sort_by_criterion("nombre")
heroes_filtrados.show()

# 6. Ordenar por nombre real
print("\n6. Personajes ordenados por nombre real:")
superheroes_list.sort_by_criterion("nombre_real")
superheroes_list.show()

# 7. Superhéroes ordenados por fecha de aparición
print("\n7. Superhéroes ordenados por año de aparición:")
solo_heroes = List([p for p in superheroes_list if not p["is_villain"]])
solo_heroes.sort_by_criterion("aparicion")
solo_heroes.show()

# 8. Cambiar nombre real de Ant Man
print("\n8. Cambiando el nombre real de Ant Man:")
for personaje in superheroes_list:
    if personaje["name"] == "Ant Man":
        personaje["real_name"] = "Scott Lang"
        print("Nombre real actualizado a:", personaje["real_name"])
        break

# 9. Filtrar por biografía
print("\n9. Personajes con 'time-traveling' o 'suit' en la biografía:")
palabras_clave = ["time-traveling", "suit"]
bio_filtrados = List()

for personaje in superheroes_list:
    bio = personaje["short_bio"].lower()
    if any(palabra in bio for palabra in palabras_clave):
        bio_filtrados.append(personaje)

bio_filtrados.sort_by_criterion("nombre")
bio_filtrados.show()

# 10. Eliminar personajes específicos
print("\n10. Eliminando personajes (Electro y Baron Zemo):")

eliminado_electro = superheroes_list.delete_value("Electro", "name")
if eliminado_electro:
    print("Electro fue eliminado:")
    print(eliminado_electro)
else:
    print("Electro no estaba en la lista.")

eliminado_zemo = superheroes_list.delete_value("Baron Zemo", "name")
if eliminado_zemo:
    print("Baron Zemo fue eliminado:")
    print(eliminado_zemo)
else:
    print("Baron Zemo no estaba en la lista.")
