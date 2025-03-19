frutas = []


for i in range(10):
    nombre = input("Ingresa el nombre de la fruta: ")
    precio = float(input("Ingresa el precio de la fruta: "))
    frutas.append({"Nombre": nombre, "Precio": precio})


for i in range(len(frutas) - 1):
    for a in range(len(frutas) - 1 - i):
        if frutas[a]["Precio"] > frutas[a + 1]["Precio"]:
            frutas[a], frutas[a + 1] = frutas[a + 1], frutas[a]


print("Lista de frutas: ")
for fruta in frutas:
    print(f"{fruta['Nombre']} - {fruta['Precio']}")