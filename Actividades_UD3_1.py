import math

def ex1():
    print("Buenas tardes")

def ex2():
    lado = 5
    area = lado * lado
    print(f"Lado = {lado}, Área = {area}")

def ex3():
    lado = float(input("Introduce el lado del cuadrado: "))
    area = lado * lado
    print(f"Área = {area}")

def ex4():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print(f"Suma = {a + b}")
    print(f"Resta = {a - b}")
    print(f"Producto = {a * b}")
    if b != 0:
        print(f"División = {a / b}")
    else:
        print("División: error (división por cero)")

def ex5():
    r = float(input("Introduce el radio: "))
    longitud = math.pi * (2 * r)           # pi * diámetro
    area = math.pi * r * r
    volumen = (4.0/3.0) * math.pi * r**3
    print(f"Longitud de la circunferencia = {longitud}")
    print(f"Área del círculo = {area}")
    print(f"Volumen de la esfera = {volumen}")

def ex6():
    precio = float(input("Precio original: "))
    precio_venta = float(input("Precio real de venta: "))
    if precio != 0:
        descuento = (precio - precio_venta) / precio * 100
        print(f"Porcentaje de descuento = {descuento:.2f}%")
    else:
        print("Precio original no puede ser 0")

def ex7():
    millas = float(input("Distancia en millas marinas: "))
    metros = millas * 1852
    print(f"Distancia en metros = {metros}")

def ex8():
    edad = int(input("Edad: "))
    if edad >= 18:
        print("Eres mayor de edad")

def ex9():
    edad = int(input("Edad: "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

def ex10():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print(f"Suma = {a + b}")
    print(f"Resta = {a - b}")
    print(f"Producto = {a * b}")
    if b != 0:
        print(f"División = {a / b}")
    else:
        print("División: error (división por cero)")

def ex11():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    mayor = a if a > b else b
    print(f"El mayor es: {mayor}")

def ex12():
    n = float(input("Número: "))
    if n >= 0:
        print("Positivo")
    else:
        print("Negativo")

def ex13():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    asc = sorted([a, b])
    print("Orden ascendente:", asc[0], asc[1])

def ex14():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    if a > b:
        print("El mayor es:", a)
    elif b > a:
        print("El mayor es:", b)
    else:
        print("Son iguales")

def ex15():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    c = float(input("Número 3: "))
    mayor = max(a, b, c)
    menor = min(a, b, c)
    print(f"Mayor = {mayor}")
    print(f"Menor = {menor}")
    iguales = []
    if a == b == c:
        print("Los tres son iguales")
        return
    if a == b:
        iguales.append("1 y 2")
    if a == c:
        iguales.append("1 y 3")
    if b == c:
        iguales.append("2 y 3")
    if iguales:
        print("Iguales:", ", ".join(iguales))
    else:
        print("No hay números iguales entre sí")

def ex16():
    n = int(input("Introduce un número entre 0 y 99999: "))
    if 0 <= n <= 99999:
        cifras = len(str(abs(n)))
        print(f"Número de cifras = {cifras}")
    else:
        print("Número fuera de rango")

def ex17():
    usuario_correcto = "admin"
    contraseña_correcta = "1234"
    user = input("Usuario: ")
    pwd = input("Contraseña: ")
    if user != usuario_correcto:
        print("nombre de usuario incorrecto")
    elif pwd != contraseña_correcta:
        print("Contraseña incorrecta")
    else:
        print("inicio de sesión correcto")

def ex18():
    n = int(input("Número: "))
    if n % 10 == 0:
        print("Es múltiplo de 10")
    else:
        print("No es múltiplo de 10")

def ex19():
    saldo = 1000.0
    while True:
        print("\nBienvenido a su Cajero Virtual")
        print("1. Ingresar dinero en cuenta")
        print("2. Retirar dinero de la cuenta")
        print("3. Salir")
        opc = input("Elige opción: ")
        if opc == "1":
            cantidad = float(input("Cantidad a ingresar: "))
            if cantidad > 0:
                saldo += cantidad
                print(f"Saldo = {saldo}")
            else:
                print("Cantidad no válida")
        elif opc == "2":
            cantidad = float(input("Cantidad a retirar: "))
            if 0 < cantidad <= saldo:
                saldo -= cantidad
                print(f"Saldo = {saldo}")
            else:
                print("Fondos insuficientes o cantidad no válida")
        elif opc == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

def ex20():
    nota = float(input("Calificación (0-10): "))
    if nota < 0 or nota > 10:
        print("Nota fuera de rango")
        return
    if nota < 3:
        texto = "Muy Deficiente"
    elif nota < 5:
        texto = "Insuficiente"
    elif nota < 6:
        texto = "Suficiente"
    elif nota < 7:
        texto = "Bien"
    elif nota < 9:
        texto = "Notable"
    else:
        texto = "Sobresaliente"
    print(texto)

def ex21():
    nombre = input("Nombre del trabajador: ")
    horas = float(input("Horas trabajadas en la semana: "))
    tarifa = float(input("Tarifa por hora: "))
    if horas <= 35:
        bruto = horas * tarifa
    else:
        bruto = 35 * tarifa + (horas - 35) * tarifa * 1.5
    # Cálculo impuestos
    restante = bruto
    impuesto = 0.0
    # primeros 500 libres
    if restante > 500:
        restante -= 500
    else:
        restante = 0
    # siguientes 400 al 25%
    if bruto > 500:
        tramo = min(bruto - 500, 400)
        impuesto += tramo * 0.25
    # resto al 45%
    if bruto > 900:
        impuesto += (bruto - 900) * 0.45
    neto = bruto - impuesto
    print(f"Trabajador: {nombre}")
    print(f"Salario bruto: {bruto:.2f}€")
    print(f"Impuestos: {impuesto:.2f}€")
    print(f"Salario neto: {neto:.2f}€")

def ex22():
    h = int(input("Horas (0-23): "))
    m = int(input("Minutos (0-59): "))
    s = int(input("Segundos (0-59): "))
    s += 1
    if s >= 60:
        s = 0
        m += 1
    if m >= 60:
        m = 0
        h += 1
    if h >= 24:
        h = 0
    print(f"Tiempo tras un segundo: {h:02d}:{m:02d}:{s:02d}")

def ex23():
    valor = float(input("Valor de compra: "))
    medio = input("Medio de pago ('contado' o 'tarjeta'): ").strip().lower()
    if medio == "contado":
        descuento = valor * 0.05
        total = valor - descuento
        print(f"Descuento = {descuento:.2f}, Total a pagar = {total:.2f}")
    elif medio == "tarjeta":
        recargo = valor * 0.03
        total = valor + recargo
        print(f"Recargo = {recargo:.2f}, Total a pagar = {total:.2f}")
    else:
        print("Medio de pago no reconocido")

def ex24():
    monto = float(input("Monto de compra: "))
    dia = input("Día de la semana: ").strip().lower()
    if dia in ("martes", "jueves"):
        descuento = monto * 0.15
        total = monto - descuento
        print(f"Descuento = {descuento:.2f}, Total a pagar = {total:.2f}")
    else:
        print(f"No hay descuento. Total a pagar = {monto:.2f}")

def ex25():
    """Cálculo de matrícula (antes estaba en el código principal)."""
    nombre = input("Ingrese el nombre del postulante: ")
    facultad = input("Ingrese la facultad que va a estudiar: ")

    importe = 0
    mensualidad = 0

    match facultad:
        case "Ing. de Sistemas":
            importe = 350
            mensualidad = 650
        case "Derecho":
            importe = 300
            mensualidad = 550
        case "Ing. Naviera":
            importe = 300
            mensualidad = 500
        case "Ing. Pesquera":
            importe = 310
            mensualidad = 460
        case "Contabilidad":
            importe = 280
            mensualidad = 490
        case "Administración":
            importe = 360
            mensualidad = 520
        case _:
            print("Facultad no reconocida.")
            return

    subtotal = importe + mensualidad
    igv = round(subtotal * 0.18, 2)
    total = round(subtotal + igv, 2)

    print("\nResumen de matrícula")
    print(f"Postulante: {nombre}")
    print(f"Facultad: {facultad}")
    print(f"Importe de matrícula: S/ {importe}")
    print(f"Mensualidad: S/ {mensualidad}")
    print(f"IGV (18%): S/ {igv}")
    print(f"Monto total a pagar: S/ {total}")

def ex26():
    """Evaluar lanzamiento de tres dados según nº de seises (usa match como 'switch')."""
    try:
        d1 = int(input("Dado 1 (1-6): "))
        d2 = int(input("Dado 2 (1-6): "))
        d3 = int(input("Dado 3 (1-6): "))
    except ValueError:
        print("Entrada no válida. Debes introducir números enteros.")
        return

    for d in (d1, d2, d3):
        if d < 1 or d > 6:
            print("Valor de dado inválido. Debe estar entre 1 y 6.")
            return

    seises = sum(1 for d in (d1, d2, d3) if d == 6)

    match seises:
        case 3:
            msg = "Excelente"
        case 2:
            msg = "Muy bien"
        case 1:
            msg = "Regular"
        case _:
            msg = "Pésimo"

    print(msg)

def menu():
    ejercicios = {
        "1": ex1, "2": ex2, "3": ex3, "4": ex4, "5": ex5, "6": ex6,
        "7": ex7, "8": ex8, "9": ex9, "10": ex10, "11": ex11, "12": ex12,
        "13": ex13, "14": ex14, "15": ex15, "16": ex16, "17": ex17,
        "18": ex18, "19": ex19, "20": ex20, "21": ex21, "22": ex22,
        "23": ex23, "24": ex24, "25": ex25, "26": ex26,
    }
    while True:
        print("\nElige ejercicio (1-26) o 'salir':")
        opc = input("> ").strip()
        if opc.lower() in ("salir", "exit", "q"):
            break
        func = ejercicios.get(opc)
        if func:
            func()
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()