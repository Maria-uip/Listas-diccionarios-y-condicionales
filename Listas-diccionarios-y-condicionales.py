 # Lista de nombres
nombres = ["Gian", "Adriana", "David", "Jerry", "Said", "Maria"]# Diccionario de edades# Estructura: "Nombre": Edad (entero)
registro_edades = {
    "Gian": 30,
    "Adriana": 26,
    "David": 25,
    "Jerry": 22,
    "Said": 35,
    "Maria": 27
} 

nombre_buscado = input("Escribe  un nombre: ")

if nombre_buscado in registro_edades:
    edad = registro_edades[nombre_buscado]
    print(f"{nombre_buscado} tiene {edad} años.")

else:
    print("La persona no fue encontrada.")

