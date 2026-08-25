##nombre del jugador

nombre_gladiador=input("Nombre del gladiador: ").strip()
while not nombre_gladiador.isalpha():
        print("Error: solo se permiten letras")
        nombre_gladiador=input("Nombre del gladiador: ").strip()

##variable iniciales
vida_del_gladiador= 100
vida_del_enemigo= 100
pociones_de_vida= 3
dano_base_ataque_pesado= 15
dano_base_del_enemigo= 12
turno_gladiador= True

while vida_del_gladiador > 0 and vida_del_enemigo > 0:
        print(f"NUEVO TURNO")
        print(f"{nombre_gladiador} tu vida es: {vida_del_gladiador} vs Vida del enemigo: {vida_del_enemigo}   Pociones: {pociones_de_vida}")
        print("Elige accion: ")
        print("1_Ataque pesado")
        print("2_Ráfaga veloz")
        print("3_Curar")

        opcion= input("Opcion elegida: ").strip()

        ##valido que la opcion ingresada debe ser dentro del rango dde las opciones dadas
        while not opcion.isdigit () or int(opcion) < 1 or int(opcion) > 3:
                print("Error: seleccione una opcion válida (1-3)")
                opcion=input("Opcion elegida: ").strip()

        opcion_juego= int(opcion)
        
##opcion1_ataque pesado
        if opcion == "1":
            if vida_del_enemigo < 20:
                dano_final= dano_base_ataque_pesado * 1.5
                print("¡GOLPE CRITICO!")
            else:
                dano_final= dano_base_ataque_pesado

            vida_del_enemigo-= dano_final
            print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

##opcion2_rafaga veloz
        elif opcion == "2":
            print("¡Iniciaste una ráfaga de golpes!")
            for i in range(3):
                vida_del_enemigo -= 5
                print(">Golpe conectado por 5 de daño")


##opcion3_curar
        elif opcion == "3":
            if pociones_de_vida > 0:
                pociones_de_vida -= 1
                vida_del_gladiador+= 30
                print(f"¡Te has curado 30 vidas! Te quedan {pociones_de_vida} pociones ")
            else:
                print("¡No te quedan pociones!")
        if vida_del_enemigo > 0:
                vida_del_gladiador -= dano_base_del_enemigo
                print(f"¡El enemigo te atacó por {dano_base_del_enemigo} puntos de daño!")

##fin del juego
print("FIN DE LA BATALLA")
if vida_del_gladiador > 0:
    print(f"VICTORIA! {nombre_gladiador} ha ganado la batalla")
else:
    print("¡DERROTA!. Has caído en combate")