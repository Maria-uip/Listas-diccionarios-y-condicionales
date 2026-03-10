 # Lista de nombres
nombres = ["Gian", "Adriana", "David", "Jerry", "Said", "Maria", "Carlos", "Karen", "Sara", "Sofia", "Moises" ]# Diccionario de edades# Estructura: "Nombre": Edad (entero)
registro_edades = {
    "Gian": 30,
    "Adriana": 26,
    "David": 25,
    "Jerry": 22,
    "Said": 35,
    "Maria": 27,
    "Carlos" : 33,
    "Karen" : 19,
    "Sara" : 16,
    "Sofia" : 24,
    "Moises" : 23
} 

print("Personas registradas:")
for nombre in nombres:
    print("-", nombre)

    
nombre_buscado = input("Escribe  un nombre: ").capitalize()

if nombre_buscado in registro_edades:
    edad = registro_edades[nombre_buscado]
    print(f"{nombre_buscado} tiene {edad} años.")

else:
    print("La persona no fue encontrada.")

op = input("¿Deseas cambiar la edad? (si/no): ").lower()

if op == "si":
        entrada = input("Nueva edad: ")
        if entrada.isdigit():
            nueva = int(entrada)
            registro_edades[nombre_buscado] = nueva
            print(f"Edad de {nombre_buscado} actualizada a {nueva}.")
        else:
            print("Error: Debes ingresar un número válido.")
else:
    print("La persona no fue encontrada.")

print(f"\nHay {len(nombres)} personas en el registro.")