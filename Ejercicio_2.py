usuario_correcto= "alumno"
clave_correcta= "python123"

intentos= 0
max_intentos= 3
acceso_concedido= 0

while intentos< max_intentos and not acceso_concedido:
    intentos += 1
##ingreso de datos, mostrando los intentos realizados por el usuario
    usuario=input(f"Nombre de usuario (intento {intentos}/{max_intentos}): ")
    clave=input("Clave: ").strip()

    if usuario == usuario_correcto and clave== clave_correcta:
        print("Acceso concedido")
        acceso_concedido= True
    else: 
        print("Error: datos ingresados incorrectos")

##si supera los 3 intentos
if not acceso_concedido:
    print("Cuenta Bloqueada")

##si accede correctamente
while acceso_concedido:
    print("1) Estado")
    print("2) Cambiar clave")
    print("3) Mensaje motivacional")
    print("4) Salir")
    opcion= input("Opción: ").strip()

    ##corregir la informacion que seleccione
    if not opcion.isdigit():
        print("Error, seleccione un número válido")
    else:
        opcion_numeros=int(opcion)

##numero ingresados debe estar entre 1 y 4
        if opcion_numeros < 1 or opcion_numeros > 4:
            print("Numero seleccionado fuera del rango")
        elif opcion_numeros == 1:
            print("Inscripto")
        elif opcion_numeros == 2:
            nueva_clave= input("Nueva clave: ").strip()

    ## validacion de clave (minimo 6 caracteres)
            if len(nueva_clave)< 6:
                print("Error, 6 caracteres minimo")
            else: 
                confirmacion= input("Confirmar clave: ").strip()
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave modificada con exito")
                else:
                    print("Clave ingresada incorrecta")
        elif opcion_numeros == 3:
            print("No importa que tengas que empezar todo de nuevo, lo importante es no perder las ganas de volver a INTENTAR!")
        elif opcion_numeros == 4:
            acceso_concedido= False
