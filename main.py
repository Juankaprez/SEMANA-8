import os
import subprocess

# Mostrar el contenido de un archivo
def mostrar_codigo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            print("\n--- CÓDIGO ---\n")
            print(f.read())
    except:
        print("No se pudo leer el archivo.")

# Ejecutar un script
def ejecutar_codigo(ruta):
    subprocess.run(["python", ruta])

# Mostrar opciones en lista
def mostrar_lista(lista):
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")
    print("0. Volver")

# Menú principal
def menu_principal():
    ruta_base = os.path.dirname(__file__)
    unidades = ["Unidad 1", "Unidad 2"]

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        mostrar_lista(unidades)
        opcion = input("Seleccione una unidad: ")

        if opcion == "0":
            break

        if opcion.isdigit():
            i = int(opcion) - 1
            if 0 <= i < len(unidades):
                menu_unidad(os.path.join(ruta_base, unidades[i]))

# Menú de subcarpetas
def menu_unidad(ruta):
    carpetas = [c.name for c in os.scandir(ruta) if c.is_dir()]

    while True:
        print("\n=== SUBCARPETAS ===")
        mostrar_lista(carpetas)
        opcion = input("Seleccione una carpeta: ")

        if opcion == "0":
            break

        if opcion.isdigit():
            i = int(opcion) - 1
            if 0 <= i < len(carpetas):
                menu_scripts(os.path.join(ruta, carpetas[i]))

# Menú de scripts
def menu_scripts(ruta):
    scripts = [s.name for s in os.scandir(ruta) if s.name.endswith(".py")]

    while True:
        print("\n=== SCRIPTS ===")
        mostrar_lista(scripts)
        opcion = input("Seleccione un script: ")

        if opcion == "0":
            break

        if opcion.isdigit():
            i = int(opcion) - 1
            if 0 <= i < len(scripts):
                ruta_script = os.path.join(ruta, scripts[i])
                mostrar_codigo(ruta_script)

                ejecutar = input("¿Ejecutar? (s/n): ")
                if ejecutar.lower() == "s":
                    ejecutar_codigo(ruta_script)

# Ejecutar programa
menu_principal()
