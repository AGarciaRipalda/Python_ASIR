"""Cada ejercicio está en una función ejN(). Ejecuta desde main() seleccionando el número"""
import math

def ej1():
    print("Buenas Tardes")

def ej2():
    lado = 5
    print("Área:", lado * lado)

def ej3():
    lado = float(input("Introduce el lado del cuadrado: "))
    print("Área:", lado * lado)

def ej4():
    a = float(input("a: "))
    b = float(input("b: "))
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Producto:", a * b)
    if b == 0:
        print("División: Error: división por cero")
    else:
        print("División:", a / b)

def ej5():
    r = float(input("Introduce el radio: "))
    d = 2 * r
    longitud = math.pi * d
    area = math.pi * r * r
    volumen = 4/3 * math.pi * r**3
    print(f"Longitud de la circunferencia: {longitud}")
    print(f"Área del círculo: {area}")
    print(f"Volumen de la esfera: {volumen}")

def ej6():
    precio_original = float(input("Precio original: "))
    precio_venta = float(input("Precio de venta real: "))
    if precio_original == 0:
        print("Error: precio original es 0")
        return
    descuento = (precio_original - precio_venta) / precio_original * 100
    print(f"Porcentaje de descuento: {descuento:.2f}%")

def ej7():
    millas = float(input("Distancia en millas marinas: "))
    metros = millas * 1852
    print(f"Distancia en metros: {metros}")

def ej8():
    edad = int(input("Edad: "))
    if edad >= 18:
        print("Eres mayor de edad")

def ej9():
    edad = int(input("Edad: "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

def ej10():
    for i in range(1, 21):
        print(i)

def ej11():
    # contador sumando de 2 en 2
    n = 2
    while n <= 200:
        print(n)
        n += 2

def ej12():
    # contador sumando de 1 en 1 y filtrando pares
    for n in range(1, 201):
        if n % 2 == 0:
            print(n)

def ej13():
    N = int(input("Introduce N: "))
    for i in range(1, N + 1):
        print(i)

def ej14():
    a = float(input("a: "))
    b = float(input("b: "))
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Producto:", a * b)
    if b == 0:
        print("División: Error: división por cero")
    else:
        print("División:", a / b)

def ej15():
    a = float(input("a: "))
    b = float(input("b: "))
    if a > b:
        print("El mayor es:", a)
    elif b > a:
        print("El mayor es:", b)
    else:
        print("Son iguales:", a)

def ej16():
    n = float(input("Número: "))
    if n >= 0:
        print("Positivo")
    else:
        print("Negativo")

def ej17():
    a = float(input("a: "))
    b = float(input("b: "))
    if a <= b:
        print(a, b)
    else:
        print(b, a)

def ej18():
    a = float(input("a: "))
    b = float(input("b: "))
    if a > b:
        print("a es mayor")
    elif b > a:
        print("b es mayor")
    else:
        print("Son iguales")

def ej19():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    mayor = max(a, b, c)
    menor = min(a, b, c)
    iguales = []
    if a == b == c:
        iguales = [("a","b","c")]
    else:
        if a == b:
            iguales.append(("a","b"))
        if a == c:
            iguales.append(("a","c"))
        if b == c:
            iguales.append(("b","c"))
    print("Mayor:", mayor)
    print("Menor:", menor)
    if iguales:
        print("Iguales:", iguales)
    else:
        print("No hay iguales")

def ej20():
    N = int(input("Introduce N (>=0): "))
    if N < 0:
        print("Error: N negativo")
        return
    fact = 1
    for i in range(2, N + 1):
        fact *= i
    print(f"{N}! = {fact}")

def ej21():
    hubo_negativo = False
    count = 0
    while count < 100:
        x = float(input(f"Introduce número no nulo ({count+1}/100): "))
        if x == 0:
            print("No se permiten ceros, introduce otro número.")
            continue
        if x < 0:
            hubo_negativo = True
        count += 1
    print("Se leyó algún número negativo:" , "Sí" if hubo_negativo else "No")

def ej22():
    positivos = 0
    negativos = 0
    count = 0
    while count < 100:
        x = float(input(f"Introduce número no nulo ({count+1}/100): "))
        if x == 0:
            print("No se permiten ceros, introduce otro número.")
            continue
        if x > 0:
            positivos += 1
        else:
            negativos += 1
        count += 1
    print("Positivos:", positivos)
    print("Negativos:", negativos)

def ej23():
    positivos = 0
    negativos = 0
    hubo_negativo = False
    while True:
        x = float(input("Introduce número no nulo (0 para terminar): "))
        if x == 0:
            break
        if x > 0:
            positivos += 1
        else:
            negativos += 1
            hubo_negativo = True
    print("Hubo algún negativo:", "Sí" if hubo_negativo else "No")
    print("Positivos:", positivos)
    print("Negativos:", negativos)

def ej24():
    suma = sum(range(1, 11))
    producto = 1
    for i in range(1, 11):
        producto *= i
    print("Suma 1..10:", suma)
    print("Producto 1..10:", producto)

def ej25():
    nota = float(input("Calificación (0-10): "))
    if nota < 0 or nota > 10:
        print("Nota fuera de rango")
        return
    if 0 <= nota < 3:
        letra = "Muy Deficiente"
    elif 3 <= nota < 5:
        letra = "Insuficiente"
    elif 5 <= nota < 6:
        letra = "Suficiente"
    elif 6 <= nota < 7:
        letra = "Bien"
    elif 7 <= nota < 9:
        letra = "Notable"
    else:
        letra = "Sobresaliente"
    print("Calificación alfabética:", letra)

def ej26():
    nombre = input("Nombre del trabajador: ")
    horas = float(input("Horas trabajadas: "))
    tarifa = float(input("Tarifa por hora (€): "))
    if horas <= 35:
        bruto = horas * tarifa
    else:
        bruto = 35 * tarifa + (horas - 35) * tarifa * 1.5
    # calcular impuestos
    renta_exenta = 500
    tramo1 = 400
    imponible = max(0, bruto - renta_exenta)
    impuesto = 0
    impuesto += min(tramo1, imponible) * 0.25
    if imponible > tramo1:
        impuesto += (imponible - tramo1) * 0.45
    neto = bruto - impuesto
    print("Nombre:", nombre)
    print(f"Salario bruto: {bruto:.2f}€")
    print(f"Impuestos: {impuesto:.2f}€")
    print(f"Salario neto: {neto:.2f}€")

def ej27():
    hubo_10 = False
    while True:
        nota = float(input("Introduce nota (0-10), -1 para terminar: "))
        if nota == -1:
            break
        if nota == 10:
            hubo_10 = True
    print("Hubo alguna nota 10:", "Sí" if hubo_10 else "No")

def ej28():
    suma_pares = 0
    suma_impares = 0
    for n in range(100, 201):
        if n % 2 == 0:
            suma_pares += n
        else:
            suma_impares += n
    print("Suma pares (100..200):", suma_pares)
    print("Suma impares (100..200):", suma_impares)

def ej29():
    print("Piensa un número entre 1 y 100. Responde 'mayor' si tu número es mayor que la propuesta, 'menor' si es menor, 'igual' si acierto.")
    low = 1
    high = 100
    while low <= high:
        guess = (low + high) // 2
        resp = input(f"¿Tu número es {guess}? (mayor/menor/igual): ").strip().lower()
        if resp == "igual":
            print("¡Adiviné!")
            return
        elif resp == "mayor":
            low = guess + 1
        elif resp == "menor":
            high = guess - 1
        else:
            print("Respuesta no válida, usa mayor/menor/igual.")
    print("No se pudo adivinar (inconsistencia en las respuestas).")

def ej30():
    euros = int(input("Introduce cantidad en euros (múltiplo de 5): "))
    if euros % 5 != 0 or euros < 0:
        print("Cantidad no válida")
        return
    billetes = [500, 200, 100, 50, 20, 10, 5]
    resultado = {}
    restante = euros
    for b in billetes:
        cuenta = restante // b
        resultado[b] = cuenta
        restante -= cuenta * b
    print("Billetes necesarios:")
    for b in billetes:
        if resultado[b]:
            print(f"{b}€: {resultado[b]}")

def main():
    print("Selecciona ejercicio (1-30) o 0 para salir")
    while True:
        try:
            n = int(input("Ejercicio: "))
        except ValueError:
            continue
        if n == 0:
            break
        fn = globals().get(f"ej{n}")
        if callable(fn):
            fn()
        else:
            print("Ejercicio no implementado")

if __name__ == "__main__":
    main()