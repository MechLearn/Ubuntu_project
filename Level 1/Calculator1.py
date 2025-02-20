import math
import cmath
import matplotlib.pyplot as plt


def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b != 0:
        return a/b
    else:
        print("No se puedo dividir por zero")
def exponencial(a,b):
    return math.pow(a,b)
def raiz_cuadrada (a):
    return math.sqrt(a)
def factorial(a):
    return math.factorial(a)
def logaritmo(a):
    return math.log(a)


while True:
    print("\n--- Calculadora Mejorada ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Exponencial")
    print("6. Raiz Cuadrada")
    print("7. Factorial")
    print("8. Logaritmo")
    print("9. Salir")
    #En este punto se crea una variable que me permita almacenar la opcion ingresada por el usuario

    try:
        opcion = int(input("Ingresa una de las opciones"))
    except ValueError:
        print("Por favor ingrese una opcion valida")
        continue


    if opcion == 1:
        print("Has seleccionado la suma")
        a = float(input("Ingresa el primer numero que deseas sumar"))
        b = float(input("Ingresa el segundo numero que deseas sumar"))
        print("El resultado de la suma es", suma(a, b))
    elif opcion == 2:
        print("Has seleccionado la resta")
        a = float(input("Ingresa el primer numero que deseas restar"))
        b = float(input("Ingresa el segundo numero que deseas restar"))
        print("El resultado de la resta es", resta(a, b))
    elif opcion == 3:
        print("Has seleccionado la multiplicacion")
        a = float(input("Ingresa el primer numero a multiplicar"))
        b = float(input("Ingresa el segundo numero a multiplicar"))
        print("El resultado de la multiplicacion es", multiplicacion(a, b))
    elif opcion == 4:
        print("Has seleccionado la division")
        a = float(input("Ingresa el primer numero a division"))
        b = float(input("Ingresa el segundo numero a division"))
        print("El resultado de la division es", division(a, b))
    elif opcion == 5:
        print("Has seleccionado la potenciacion")
        a = float(input("Ingresa el numero a potenciar"))
        b = float(input("Ingresa la potencia"))
        print("El resultado de la potenciacion es", exponencial(a,b))
    elif opcion == 6:
        print("Has seleccionado la logaritmo")
        a = float(input("Ingrese el numero al cual desea sacarle el logaritmo"))
        print(f"El logaritmo del numero {a} es" , logaritmo(a))
    elif opcion == 7:
        print("Has seleccionado la raiz cuadrada")
        a = float(input("Ingresa el numero al cual desea sacar la raiz cuadrada"))
        print(f"la raiz cuadrada del numero {a}", raiz_cuadrada(a))
    elif opcion == 8:
        print("Has seleccionado la factorial")
        a = float(input("Ingresa el numero que desea sacarle el factorial"))
        print(f"la factorial del numero {a}", factorial(a))
    elif opcion == 9:
        print("Seguro que quieres irte?")
    else:
        print("Ha seleccionado una opcion invalida")

    continuar = input("Desea volver a usar la calculadora? S/N")
    if continuar.lower() != 's':
        print("Gracias por usar la calculadora mejorada")
        break
