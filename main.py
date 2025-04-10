

print("¡Bienvenido al Gestor de Tareas!")

tarea = input("Escribe una nueva tarea: ")
with open("tareas.txt", "a") as archivo:
    archivo.write(tarea + "\n")
print("Tarea guardada.")

print("\nTus tareas:")
with open("tareas.txt", "r") as archivo:
    print(archivo.read())
