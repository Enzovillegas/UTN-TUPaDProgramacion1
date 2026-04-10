#Simular una compra con validaciones y cálculo de total:
#Pedir nombre del cliente (solo letras, validar con .isalpha() en while):
#pido el nombre del cliente:
nombre=input("Por favor ingrese su nombre: ").strip()
#Valido que el nombre no esté vacío y solo contenga letras:

while nombre==""or not nombre.isalpha():
    print("Error; ingresa un nombre no vacío y sólo con letras")
    nombre=input("Ingrese su nombre nuevamente: ").strip()
print("Nombre válido: ", nombre)
#Pedir cantidad de productos a comprar (número entero positivo, validar con 
#.isdigit() en while):
#str por si escribe "cinco" y strip para que quite espacios adelante y al finalizar:
cantidad=str(input("Por favor ingrese la cantidad de productos: ")).strip()
#Validamos que la cantidad sea un entero positivo:
while not cantidad .isdigit() or int(cantidad)<=0:
    print("Error; ingresa un número entero positivo: ")
    cantidad=str(input("Ingresa la cantidad de productos: ")).strip()
cantidad=int(cantidad)
total_sin_descuento=0
total_con_descuento=0.0
#Creamos un bucle para recorrer todos los productos:
for i in range (1, cantidad +1):
#Pido precio:
    precio=input(f"Producto {i}- ingrese precio: ")
    #Validamos que el precio sea un entero positivo:
    while not precio.isdigit():
        print("Error; el precio debe ser un entero positivo: ")
    precio=input(f"Producto{i}-ingrese precio nuevamente: ")
    precio=int(precio)
#Si tiene descuento:
desc=input("Descuento (S/N): ").lower()
while desc != "s" and desc != "n":
        print("Error; ingrese S o N:")
        desc=input("Descuento S/N:").lower()
total_sin_descuento+=precio
if desc=="s":
     precio=precio*0.9
total_con_descuento += precio     
#Calculos finales:
ahorro=total_sin_descuento-total_con_descuento
promedio=total_con_descuento/cantidad
print("Cliente: ", nombre)
print(f"Total sin descuento: $, {total_sin_descuento}")
print(f"Total con descuento: $, {total_con_descuento:.2f}")
print(f"Ahorro total: $ {ahorro:.2f}")
print(f"Promedio: $ {promedio:.2f}")
#Ejercicio 2
#Definir credenciales fijas en el código: 
usuario_correcto="alumno"
clave_correcta="python123"
#Arranco en cero:
intentos=0
# Defino un while que se repita hasta que intentos sea menor que 3 y defino las variables:
while intentos <3:
    usuario=input("Por favor ingrese el usuario: ")
    clave=input("Por favor ingrese la clave correcta:")
#Si es correcto se corta el ciclo:
    if usuario==usuario_correcto and clave==clave_correcta:
          break
#Suma a intentos 1 (No es ciclo infinito)
    else:
     intentos+=1
     print("Intento",intentos,"/3 fallido")

#Llega a 3 y se bloquea el acceso
    if intentos==3:
        print("Acceso bloqueado")
    opciones=0
    if opcion == 1:
        print("Inscripto")

    elif opcion == 2:
        nueva = input("Nueva clave: ")

        # Validar longitud
        if len(nueva) < 6:
            print("Error: mínimo 6 caracteres.")
            continue

        confirmar = input("Confirmar clave: ")

        if nueva != confirmar:
            print("Error: las claves no coinciden.")
        else:
            clave_correcta = nueva
            print("Clave cambiada con éxito.")

    elif opcion == 3:
        print("¡Seguí adelante, vas muy bien!")

    elif opcion == 4:
        print("Saliendo del sistema...")
        break
#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)” 
lunes=["","",""]
martes=["","","",""]
#Pido nombre:
nombre=input("Por favor ingrese su nombre: ")
#Solo letras:
while not nombre.isalpha():
     print("Error: Sólo letras")
     nombre=input("Por favor ingrese su nombre:")
opcion=""
while opcion !="1":
     print("Menú:")
     print("opción 1=Reservar el turno")
     print("opción 2=Cancelar el turno")
     print("opción 3=Ver agenda del día")
     print("opción 4=Salir")
     opcion=input("Elegí una opción:")
if opcion=="1":
        dia=input("Elegí el día, (1-Lunes, 2-Martes): ")
        paciente=input("Nombre del paciente: ")
while not paciente.isalpha():
            print("Error, ingrese solo letras")
            paciente=input("Por favor ingrese su nombre correctamente: ")
if dia=="1":
                if paciente in lunes:
                         print("Ese paciente ya tiene turno el Lunes")
                else:
                         for i in range (len(lunes)):
                              if lunes[i]=="":
                                   lunes[i]=paciente
                                   print("Turno asignado en Lunes")
                                   break
else:
                                   print("No hay turnos disponibles")
if dia=="2":
                                        if paciente in martes:
                                              print("Ese paciente ya tiene turno el Martes")
                                        else:
                                              for i in range(len(martes)):
                                                                        if martes[i]=="":
                                                                               martes[i]=paciente
                                                                               print("Turno asignado en Martes")
                                                                               break
                                                                        else:
                                                                               print("No hay turnos disponibles el Martes")
elif opcion == "2":
        dia = input("Elegí día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente: ")

        if dia == "1":
            if paciente in lunes:
                pos = lunes.index(paciente)
                lunes[pos] = ""
                print("Turno cancelado")
            else:
                print("No existe ese turno")

        elif dia == "2":
            if paciente in martes:
                pos = martes.index(paciente)
                martes[pos] = ""
                print("Turno cancelado")
            else:
                print("No existe ese turno")
# Ver agenda:
elif opcion == "3":
        dia = input("Elegí día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("\nAgenda Lunes:")
            for turno in lunes:
                if turno == "":
                    print("Libre")
                else:
                    print(turno)

        elif dia == "2":
            print("\nAgenda Martes:")
            for turno in martes:
                if turno == "":
                    print("Libre")
                else:
                    print(turno)

# Salir
elif opcion == "4":
        print("Saliendo...")

else:
        print("Opción inválida")

#Resumen:
ocupados_lunes = len(lunes) - lunes.count("")
ocupados_martes = len(martes) - martes.count("")

print("\n--- RESUMEN ---")
print("Lunes ocupados:", ocupados_lunes, "libres:", lunes.count(""))
print("Martes ocupados:", ocupados_martes, "libres:", martes.count(""))

if ocupados_lunes > ocupados_martes:
    print("Día con más turnos: Lunes")
elif ocupados_martes > ocupados_lunes:
    print("Día con más turnos: Martes")
else:
    print("Empate de turnos")
#Ejercicio 4  — “Escape Room: La Bóveda”
# Variables
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

# Nombre:
nombre = input("Nombre del agente: ")
#Validamos que sea solo letras:
while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("Nombre del agente: ")
#Menu que se repita:
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
#Bloqueo:
    if alarma and tiempo <= 3:
        print("La bóveda se bloqueó por la alarma")
        break
    print("Estado")
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)
    print("Código:", codigo_parcial)
    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Elegí opción: ")

    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        print("Opción inválida")
        opcion = input("Elegí opción: ")

    # Opción 1
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            print("Forzaste 3 veces seguidas. Se activó la alarma")
            alarma = True
        else:
            
            if energia < 40:
                num = input("Elegí número (1-3): ")
                while not num.isdigit() or num not in ("1", "2", "3"):
                    num = input("Elegí número válido (1-3): ")

                if num == "3":
                    print("Activaste la alarma")
                    alarma = True

            if not alarma:
                cerraduras_abiertas += 1
                print(" Abriste una cerradura")

# Opcion 2
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("Hackeando...")
        for i in range(4):
            print("Paso", i + 1)
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Código completo → cerradura abierta")

 # Opcion 3
    elif opcion == "3":
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        racha_forzar = 0

        if alarma:
            energia -= 10
            print("Descansar con alarma activa consume energía extra")

print("\nRESULTADO")

if cerraduras_abiertas == 3:
    print("Ganaste, abriste la bóveda")
elif energia <= 0 or tiempo <= 0:
    print("Perdiste por falta de recursos")
# Ejercicio 5:
#“Escape Room:"La Arena del Gladiador"  
print("Bienvenido a la Arena")

# Nombre:

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")

# Variables:
vida_jugador = 100        
vida_enemigo = 100        
pociones = 3              
danio_jugador = 15        
danio_enemigo = 12        
turno_jugador = True      

print("\nInicio")
#

while vida_jugador > 0 and vida_enemigo > 0:

    print("\nNuevo turno")
    print(nombre, "(HP:", vida_jugador, ") vs Enemigo (HP:", vida_enemigo, ") | Pociones:", pociones)

#Turno del jugador:

    if turno_jugador:

        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

# Validamos:
        while not opcion.isdigit() or opcion not in ("1", "2", "3"):
            print("Error: Ingrese un número válido")
            opcion = input("Opción: ")

#Accion A:
        if opcion == "1":
            if vida_enemigo < 20:
                danio = danio_jugador * 1.5   
                print(" ¡Golpe crítico!")
            else:
                danio = danio_jugador

            vida_enemigo -= danio
            print("¡Atacaste al enemigo por", danio, "de daño!")

# Ráfaga veloz
        elif opcion == "2":
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

#Curar
        elif opcion == "3":
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Recuperaste 30 de vida")
            else:
                print("¡No quedan pociones!")

#Turno del enemigo:
        if vida_enemigo > 0:
            vida_jugador -= danio_enemigo
            print(" ¡El enemigo te atacó por 12 puntos de daño!")

# Resultado:
print("\n=== FIN ===")

if vida_jugador > 0:
    print(" ¡Ganaste!", nombre, "ha ganado la batalla.")
else:
    print("Perdiste. Has caído en combate.")




         

    

          

     
          


 
     
     














