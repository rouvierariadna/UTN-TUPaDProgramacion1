##1_pedir nombre del agente
nombre_agente = input("Nombre del agente: ").strip()
while not nombre_agente.isalpha():
    print("Ingrese solo letras.")
    nombre_agente = input("Nombre del agente: ").strip()

##2_variables iniciales del juego
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

##contador para la regla anti-spam
forzar_seguidas = 0

print(f"¡Bienvenido Agente {nombre_agente}! ")
print(f"Misión: Abrir la bóveda")

##3_bucle principal del juego
##continúa mientras tenga energía, tiempo, falten cerraduras y la alarma no este bloqueada
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"ESTADO ACTUAL")
    print(f"Energía: {energia}")
    print(f" Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma}")
    print("1_Forzar cerradura (costo: -20 energía, -2 tiempo)")
    print("2_Hackear panel (costo: -10 energía, -3 tiempo)")
    print("3_Descansar (costo: +15 energía, -1 tiempo)")

    opcion = input("Elija una acción (1-3): ").strip()
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Seleccione una opción válida (1, 2 o 3).")
        opcion = input("Elija una acción (1-3): ").strip()

    opcion_accion = int(opcion)

    ##OPCIÓN 1:forzar cerradura
    if opcion_accion == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2

        ##regla_anti-spam (3ra vez seguida)
        if forzar_seguidas == 3:
            alarma = True
            print("¡LA CERRADURA SE TRABÓ! La alarma se activó por forzar 3 veces seguidas.")
        else:
            ##riesgo de alarma si energía < 40
            if energia < 40:
                print("¡Atención! Energía baja, hay riesgo de activar la alarma.")
                num_riesgo = input("Elija un número de seguridad (1-3): ").strip()
                while not num_riesgo.isdigit() or int(num_riesgo) < 1 or int(num_riesgo) > 3:
                    print("Error: Elija un número de 1 a 3.")
                    num_riesgo = input("Elija un número de seguridad (1-3): ").strip()

                if int(num_riesgo) == 3:
                    alarma = True
                    print("¡Alarma activada por fallo en la maniobra!")

            ##si no hay alarma, abre cerradura
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura forzada con éxito!")

    #"OPCIÓN 2:hackear panle
    elif opcion_accion == 2:
        forzar_seguidas = 0  ##Corta anti-spam
        energia -= 10
        tiempo -= 3

        print("Iniciando hackeo...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - Progreso de código: {codigo_parcial}")

        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Código completado! Se abrió 1 cerradura automáticamente.")

    ##OPCIÓN 3:descansar
    elif opcion_accion == 3:
        forzar_seguidas = 0  ##corta anti-spam
        tiempo -= 1

        if alarma:
            ##si la alarma está ON, recupera 15 pero pierde 10 extra por el estres de la alarma
            energia += 15 - 10
            print("Descansaste, pero la alarma encendida te costó -10 de energía extra.")
        else:
            energia += 15
            print("Descansaste recuperando energía.")

        ##tope máximo de energía:100
        if energia > 100:
            energia = 100

##4_evaluación del resultado final
print("FIN DEL JUEGO")
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El Agente {nombre_agente} ha logrado abrir la bóveda.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se bloqueó por activación de alarma con poco tiempo.")
else:
    print("DERROTA: Te has quedado sin energía o sin tiempo.")