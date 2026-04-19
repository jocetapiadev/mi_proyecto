# 1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambios solicitados:
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

# 2. Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:
        # Usamos un list comprehension para el formato tipo BONUS
        output = ", ".join([f"{key} - {val}" for key, val in diccionario.items()])
        print(output)

# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# 4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for llave, lista in diccionario.items():
        print(f"\n{len(lista)} {llave.upper()}")
        for item in lista:
            print(item)

# --- PRUEBAS PARA VERIFICAR ---
print("--- Ejercicio 2 ---")
cantantes_ejercicio = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
iterarDiccionario(cantantes_ejercicio)

print("\n--- Ejercicio 3 (Nombres) ---")
iterarDiccionario2("nombre", cantantes_ejercicio)

print("\n--- Ejercicio 4 ---")
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
imprimirInformacion(costa_rica)
