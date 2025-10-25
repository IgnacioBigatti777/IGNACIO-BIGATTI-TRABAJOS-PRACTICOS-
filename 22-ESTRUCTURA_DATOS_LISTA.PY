# ==============================================================================
# 1. ESTRUCTURA DE DATOS: Lista de Jedis (EJEMPLO)
# ==============================================================================

jedis = [
    {
        "nombre": "Yoda",
        "maestros": [],
        "sables_luz": ["verde"],
        "especie": "Yoda's Species"
    },
    {
        "nombre": "Luke Skywalker",
        "maestros": ["Obi-Wan Kenobi", "Yoda"],
        "sables_luz": ["azul", "verde"],
        "especie": "humana"
    },
    {
        "nombre": "Ahsoka Tano",
        "maestros": ["Anakin Skywalker"],
        "sables_luz": ["verde", "amarillo", "blanco"],
        "especie": "togruta"
    },
    {
        "nombre": "Mace Windu",
        "maestros": ["Yoda", "Cossam Mas"],
        "sables_luz": ["violeta"],
        "especie": "humana"
    },
    {
        "nombre": "Kit Fisto",
        "maestros": ["Yoda"],
        "sables_luz": ["verde"],
        "especie": "nautolano"
    },
    {
        "nombre": "Plo Koon",
        "maestros": ["Yoda", "Tyvokka"],
        "sables_luz": ["naranja"],
        "especie": "kel dor"
    },
    {
        "nombre": "Aayla Secura",
        "maestros": ["Quinlan Vos"],
        "sables_luz": ["azul", "verde"],
        "especie": "twi'lek"
    },
    {
        "nombre": "Ki-Adi-Mundi",
        "maestros": ["Yoda", "Sharad Hett"],
        "sables_luz": ["azul"],
        "especie": "cereano"
    },
    {
        "nombre": "Qui-Gon Jinn",
        "maestros": ["Conde Dooku"],
        "sables_luz": ["verde"],
        "especie": "humana"
    },
]

# ==============================================================================
# 2. FUNCIONES PARA RESOLVER LAS ACTIVIDADES
# ==============================================================================

# a. listado ordenado por nombre y por especie
def listar_jedis_ordenados(lista_jedis):
    """Ordena y lista los Jedis primero por nombre y luego por especie."""
    
    # Ordenar por Nombre
    jedis_por_nombre = sorted(lista_jedis, key=lambda j: j['nombre'])
    print("\n--- a. Listado Ordenado por Nombre ---")
    for j in jedis_por_nombre:
        print(f"- {j['nombre']} (Especie: {j['especie']})")
        
    # Ordenar por Especie
    jedis_por_especie = sorted(lista_jedis, key=lambda j: j['especie'])
    print("\n--- a. Listado Ordenado por Especie ---")
    for j in jedis_por_especie:
        print(f"- {j['especie']} (Nombre: {j['nombre']})")


# b. mostrar toda la información de Ahsoka Tano y Kit Fisto
def mostrar_informacion_por_nombres(lista_jedis, nombres):
    """Muestra la información completa de los Jedis cuyos nombres se encuentran en la lista 'nombres'."""
    print(f"\n--- b. Información Detallada de {', '.join(nombres)} ---")
    for nombre_buscado in nombres:
        jedi = next((j for j in lista_jedis if j['nombre'] == nombre_buscado), None)
        if jedi:
            print(f"\nJedi: {jedi['nombre']}")
            print(f"  Maestros: {', '.join(jedi['maestros']) if jedi['maestros'] else 'Ninguno conocido'}")
            print(f"  Sables de Luz: {', '.join(jedi['sables_luz'])}")
            print(f"  Especie: {jedi['especie']}")
        else:
            print(f"\n¡Advertencia! No se encontró a {nombre_buscado}.")


# c. y h. (Función reutilizable) mostrar todos los padawan de Yoda, Luke Skywalker, Qui-Gon Jinn y Mace Windu
def mostrar_padawans_de_maestros(lista_jedis, maestros_buscados, actividad_letra):
    """Muestra los aprendices (padawans) de los maestros especificados."""
    padawans = {}
    for maestro in maestros_buscados:
        # Busca Jedis donde el maestro esté en su lista de 'maestros'
        aprendices = [jedi['nombre'] for jedi in lista_jedis if maestro in jedi['maestros']]
        padawans[maestro] = aprendices

    print(f"\n--- {actividad_letra}. Padawans (Aprendices) de Maestros ---")
    for maestro, aprendices in padawans.items():
        if aprendices:
            print(f"- **{maestro}** entrenó a: {', '.join(aprendices)}")
        else:
            print(f"- **{maestro}**: No se encontraron padawans en esta lista.")


# d. mostrar los Jedi de especie humana y twi'lek
def mostrar_jedis_por_especie(lista_jedis, especies_buscadas):
    """Lista los Jedis que pertenecen a las especies especificadas."""
    especies_bajas = [e.lower() for e in especies_buscadas]
    jedis_encontrados = [
        jedi['nombre'] for jedi in lista_jedis 
        if jedi['especie'].lower() in especies_bajas
    ]

    print(f"\n--- d. Jedis de especie {', '.join(especies_buscadas).title()} ---")
    if jedis_encontrados:
        print(f"Jedis: {', '.join(jedis_encontrados)}")
    else:
        print("No se encontraron Jedis de esas especies en la lista.")


# e. listar todos los Jedi que comienzan con A
def listar_jedis_que_comienzan_con(lista_jedis, letra):
    """Lista los Jedis cuyo nombre comienza con la letra especificada."""
    letra_mayus = letra.strip()[0].upper()
    jedis_filtrados = [
        jedi['nombre'] for jedi in lista_jedis
        if jedi['nombre'].startswith(letra_mayus)
    ]
    
    print(f"\n--- e. Jedis que comienzan con '{letra_mayus}' ---")
    if jedis_filtrados:
        print(f"Jedis: {', '.join(jedis_filtrados)}")
    else:
        print(f"No se encontraron Jedis que comiencen con '{letra_mayus}'.")


# f. mostrar a los Jedi que usaron sable de luz de más de un color
def mostrar_jedis_multi_sable(lista_jedis):
    """Muestra los Jedis que han usado sables de luz de más de un color (más de 1)."""
    jedis_multi = [
        jedi['nombre'] for jedi in lista_jedis
        if len(jedi['sables_luz']) > 1
    ]
    
    print("\n--- f. Jedis que usaron sable de más de un color ---")
    if jedis_multi:
        print(f"Jedis: {', '.join(jedis_multi)}")
    else:
        print("Todos los Jedis de la lista usaron un solo color de sable.")


# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta
def mostrar_jedis_por_color_sable(lista_jedis, colores_buscados):
    """Muestra los Jedis que usaron alguno de los colores de sable de luz especificados."""
    colores_bajos = [c.lower() for c in colores_buscados]
    jedis_por_color = set()
    
    for jedi in lista_jedis:
        # Verifica si algún sable del Jedi está en la lista de colores buscados
        if any(sable.lower() in colores_bajos for sable in jedi['sables_luz']):
            jedis_por_color.add(jedi['nombre'])

    print(f"\n--- g. Jedis que usaron sable {', '.join(colores_buscados)} ---")
    if jedis_por_color:
        # Muestra los nombres ordenados para mejor lectura
        print(f"Jedis: {', '.join(sorted(list(jedis_por_color)))}")
    else:
        print(f"No se encontraron Jedis con sables {', '.join(colores_buscados)}.")


# ==============================================================================
# 3. EJECUCIÓN DE LAS ACTIVIDADES
# ==============================================================================

if __name__ == '__main__':
    
    print("==============================================")
    print("  EJECUCIÓN DE ACTIVIDADES SOBRE LA LISTA JEDI  ")
    print("==============================================")

    # a. listado ordenado por nombre y por especie
    listar_jedis_ordenados(jedis)

    # b. mostrar toda la información de Ahsoka Tano y Kit Fisto
    mostrar_informacion_por_nombres(jedis, ["Ahsoka Tano", "Kit Fisto"])

    # c. mostrar todos los padawan de Yoda y Luke Skywalker
    mostrar_padawans_de_maestros(jedis, ["Yoda", "Luke Skywalker"], "c")

    # d. mostrar los Jedi de especie humana y twi'lek
    mostrar_jedis_por_especie(jedis, ["humana", "twi'lek"])

    # e. listar todos los Jedi que comienzan con A
    listar_jedis_que_comienzan_con(jedis, "A")

    # f. mostrar a los Jedi que usaron sable de luz de más de un color
    mostrar_jedis_multi_sable(jedis)

    # g. indicar los Jedi que utilizaron sable de luz amarillo o violeta
    mostrar_jedis_por_color_sable(jedis, ["amarillo", "violeta"])

    # h. indicar los nombres de los padawans de Qui-Gon Jin y Mace Windu
    mostrar_padawans_de_maestros(jedis, ["Qui-Gon Jinn", "Mace Windu"], "h")

    print("\n==============================================")