##nombre del cliente
nombre=input("Nombre del cliente: ").strip ()

while not nombre.isalpha():
    print("Ingrese solo letras (sin espacios)")
    nombre=input("Nombre del cliente: ").strip()


##cantidad de productos
cantidad=input("Cantidad de productos: ").strip()

while not cantidad.isdigit() or int(cantidad) == 0:
    print("Solo numeros enteros positivos mayores a 0")
    cantidad=input("Cantidad de productos: ").strip()
cantidad=int(cantidad)


##precios
total_con_descuento= 0
total_sin_descuento= 0

ahorro= 0
promedio= 0

for i in range(cantidad):

    ##pedir precio
    precio=input("Precio del producto: ").strip()
    
    while not precio.isdigit():
        print("Números enteros")
        precio=input("Precio del producto: ").strip()
    precio=int(precio)


    ##pedir descuento
    descuento=input("Tiene descuento(SI/NO)?: ")

    while  descuento.lower().strip() != "s" and descuento.lower().strip() !="n" :
        print("Ingrese S/N")
        descuento=input("Tiene descuento?: ").strip().lower()

    #aplicar descuento si corresponde
    if descuento =="s":
            precio_final= precio - (precio * 0.10)
    else: 
            precio_final= precio

    total_sin_descuento += precio
    total_con_descuento +=precio_final

ahorro= total_sin_descuento - total_con_descuento
promedio= total_con_descuento / cantidad

print(f"Cliente: {nombre}")
print(f"Cantidad de productos comprados: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuento:.2f}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")