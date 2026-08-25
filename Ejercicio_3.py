lunes1= ""
lunes2= ""
lunes3= ""
lunes4=""

martes1= ""
martes2= ""
martes3= ""
##Pedir nombre del operador, bucle hasta que ingrese con letras
operador= input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Solo se permiten ingresar letras")
    operador=input("Nombre del operador: ").strip()

#turnos
lunes1, lunes2, lunes3, lunes4 = "", "", "", ""
martes1, martes2, martes3 = "", "", ""

sistema_activo= True

##Menú
while sistema_activo:
    print("AGENDA DE TURNOS")
    print("1_Reservar turno")
    print("2_Cancelar turno (por nombre)")
    print("3_Ver agenda del dia")
    print("4_Ver resumen general") 
    print("5_Cerrar sistema") 

    opcion= input("Opcion requerida: ").strip() 

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error, seleccione una opcion correcta")
        opcion=input("Seleccione una opcion (1,2,3,4,5): ").strip()

    opcion_establecida= int(opcion)

    ##opcion 1 
    if opcion_establecida == 1:
        dia= input("Elegir turno (1=Lunes, 2=Martes): ").strip()
        while dia != "1" and dia != "2":
            print("El dato ingresado es incorrecto, elija 1 o 2: ")
            dia= input("Elegir turno (1=Lunes, 2=Martes): ").strip()
        dia= int(dia)

        paciente= input("Nombre del paciente: ").strip()
        while not paciente.isalpha():
            print("Ingrese solo letras")
            paciente=input("Nombre del paciente: ")

    ##reserva lunes
        if dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Ya tiene un turno reservado")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado para el lunes (Turno 1)")    
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado para el lunes (Turno 2).")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado para el lunes (Turno 3).")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado para el lunes (Turno 4).")
            else:
                print("No hay turnos disponibles para el Lunes")

        ##reserva martes
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Ya tiene un turno reservado")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado para el martes (Turno 1).")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado para el martes (Turno 2).")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado para el martes (Turno 3).")
            else:
                print("No hay turnos disponibles para el Martes")

##cancelar turno
    elif opcion_establecida == 2:
        dia = input("Elegir día (1=Lunes, 2=Martes): ").strip()
        while dia != "1" and dia != "2":
            print("El dato ingresado es incorrecto, elija 1 o 2:")
            dia = input("Elegir turno (1=Lunes, 2=Martes): ").strip()

        paciente = input("Nombre del paciente a cancelar: ").strip()
        while not paciente.isalpha():
            print("Error: Ingrese solo letras.")
            paciente = input("Nombre del paciente a cancelar: ").strip()

        cancelado = False
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""; cancelado = True
            elif lunes2 == paciente: lunes2 = ""; cancelado = True
            elif lunes3 == paciente: lunes3 = ""; cancelado = True
            elif lunes4 == paciente: lunes4 = ""; cancelado = True
        else:
            if martes1 == paciente: martes1 = ""; cancelado = True
            elif martes2 == paciente: martes2 = ""; cancelado = True
            elif martes3 == paciente: martes3 = ""; cancelado = True

        if cancelado:
            print("Turno cancelado exitosamente")
        else:
            print("No se encontró ningún turno registrado de ese paciente en el dia seleccionado")

   ##ver agenda del dia
    elif opcion_establecida == 3:
        dia = input("Elegir día a consultar (1=Lunes, 2=Martes): ").strip()
        while dia != "1" and dia != "2":
            print("El dato ingresado es incorrecto, elija 1 o 2:")
            dia = input("Elegir día a consultar (1=Lunes, 2=Martes): ").strip()

        if dia == "1":
            print("AGENDA LUNES")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("AGENDA MARTES")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    ##resumen general
    elif opcion_establecida == 4:
        ## turnos dados el dia lunes
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        ##turbis dados el dia martes
        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print("RESUMEN GENERAL")
        print(f"Lunes  -> Ocupados: {ocupados_lunes} | Disponibles: {libres_lunes}")
        print(f"Martes -> Ocupados: {ocupados_martes} | Disponibles: {libres_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: LUNES")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: MARTES")
        else:
            print("Día con más turnos ocupados: EMPATE (ambos días tienen la misma cantidad)")

    ## cerra sistema
    elif opcion_establecida == 5:
        print(f"Gracias por utilizar el sistema, {operador}. ¡Hasta luego!")
        sistema_activo = False