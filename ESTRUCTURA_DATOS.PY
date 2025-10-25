# ==============================================================================
# 1. ESTRUCTURA DE DATOS: Lista de Superhéroes
# ==============================================================================

superheroes = [
    {
        "nombre": "Spider-Man",
        "año_aparicion": 1962,
        "casa": "Marvel",
        "biografia": "Peter Parker, mordido por una araña radiactiva, lucha contra el crimen en Nueva York."
    },
    {
        "nombre": "Superman",
        "año_aparicion": 1938,
        "casa": "DC",
        "biografia": "Kryptoniano enviado a la Tierra, Kal-El usa sus poderes para proteger a la humanidad."
    },
    {
        "nombre": "Wonder Woman",
        "año_aparicion": 1941,
        "casa": "DC",
        "biografia": "Princesa amazona Diana de Themyscira, defensora de la verdad y la vida."
    },
    {
        "nombre": "Iron Man",
        "año_aparicion": 1963,
        "casa": "Marvel",
        "biografia": "Tony Stark, genio, multimillonario, playboy, filántropo, que usa una armadura de alta tecnología."
    },
    {
        "nombre": "Batman",
        "año_aparicion": 1939,
        "casa": "DC",
        "biografia": "Bruce Wayne, utiliza inteligencia y tecnología para combatir el crimen."
    }
    # Puedes añadir más superhéroes aquí
]

# ==============================================================================
# 2. FUNCIONES DE GESTIÓN BÁSICA
# ==============================================================================

def agregar_superheroe(lista, nombre, año, casa, biografia):
    """
    Agrega un nuevo superhéroe a la lista.
    """
    nuevo_heroe = {
        "nombre": nombre,
        "año_aparicion": año,
        "casa": casa,
        "biografia": biografia
    }
    lista.append(nuevo_heroe)
    print(f"'{nombre}' agregado a la lista.")


def mostrar_todos_los_superheroes(lista):
    """
    Muestra la información básica de todos los superhéroes en la lista.
    """
    if not lista:
        print("La lista de superhéroes está vacía.")
        return
        
    print("\n--- Lista Completa de Superhéroes ---")
    for heroe in lista:
        print(f"  Nombre: {heroe['nombre']}")
        print(f"  Casa: {heroe['casa']}")
        print(f"  Año Aparición: {heroe['año_aparicion']}")
        print("--------------------------------------")


def buscar_superheroe_por_nombre(lista, nombre):
    """
    Busca y devuelve el diccionario del superhéroe por nombre.
    Retorna None si no lo encuentra.
    """
    nombre_busqueda = nombre.strip().lower()
    for heroe in lista:
        if heroe['nombre'].lower() == nombre_busqueda:
            return heroe
    return None

# ==============================================================================
# 3. EJEMPLO DE USO (OPCIONAL)
# ==============================================================================

if __name__ == '__main__':
    
    # Mostrar la lista inicial
    mostrar_todos_los_superheroes(superheroes)
    
    # Agregar un nuevo superhéroe
    agregar_superheroe(superheroes, "Capitán América", 1941, "Marvel", "Soldado de la Segunda Guerra Mundial mejorado con un suero.")
    
    # Buscar un superhéroe
    heroe_encontrado = buscar_superheroe_por_nombre(superheroes, "Batman")
    if heroe_encontrado:
        print(f"\n¡Encontrado! La biografía de {heroe_encontrado['nombre']} es: {heroe_encontrado['biografia'][:50]}...")
    else:
        print("\nSuperhéroe no encontrado.")
        
    # Mostrar la lista actualizada
    mostrar_todos_los_superheroes(superheroes)