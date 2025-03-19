import random

helados = []

print("*** HeladeriApp ***")
print("1. Agregar Helado")
print("2. Mostrar todos los Helados")
print("3. Modificar Helado")
print("4. Eliminar Helado")
print("5. Salir")


while True:
    opcion = int(input("Digite una opción del menú: "))

    if opcion == 1:
       
        id_helado = random.randint(1000, 9999) 
        nombre = input("Digite el nombre del helado: ")
        descripcion = input("Digite la descripción del helado: ")
        precio = float(input("Digite el precio del helado: "))

        helado = {
            "id": id_helado,
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio
        }
        helados.append(helado)
        print("Helado '" + nombre + "' agregado con éxito.")

    elif opcion == 2:
        if len(helados) > 0:
            print("\nLista de Helados:")
            for helado in helados:
                print("ID: " + str(helado['id']) + " | Nombre: " + helado['nombre'] + " | Descripción: " + helado['descripcion'] + " | Precio: " + str(helado['precio']))
        else:
            print("No hay helados registrados.")

    elif opcion == 3:
        id_helado = int(input("Digite el ID del helado que desea modificar: "))
        encontrado = False
        for helado in helados:
            if helado["id"] == id_helado:
                encontrado = True
                print("Modificando Helado: " + helado['nombre'])
                helado["nombre"] = input("Nuevo nombre del helado: ")
                helado["descripcion"] = input("Nueva descripción: ")
                helado["precio"] = float(input("Nuevo precio: "))
                print("Helado '" + helado['nombre'] + "' modificado con éxito.")
                break
        if not encontrado:
            print("Helado no encontrado con ese ID.")

    elif opcion == 4:
        id_helado = int(input("Digite el ID del helado que desea eliminar: "))
        encontrado = False
        for helado in helados:
            if helado["id"] == id_helado:
                helados.remove(helado)
                print("Helado con ID " + str(id_helado) + " eliminado con éxito.")
                encontrado = True
                break
        if not encontrado:
            print("Helado no encontrado con ese ID.")

    elif opcion == 5:
        print("Saliendo de la aplicación...")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
