# -*- coding: utf-8 -*-

def conversor(tipo_moneda, valor_yen):
    moneda = input("¿Cuántos " + tipo_moneda + " tienes?: ")
    moneda = float(moneda)
    yen = moneda / valor_yen
    yen = round(yen, 3)
    yen = str(yen)
    print("Tienes 円" + yen + " yenes")

menu = """
Bienvenido al conversor de monedas 💰 de Mar 🐼, ingrese la cantidad de dinero, por favor:
1 - Pesos mexicanos
2 - Dólares
3 - Euros
4 - Yuanes
5 - Wones surcoreanos
Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Pesos mexicanos", 0.18)
elif opcion == 2:
    conversor("Dólares", 0.0087)
elif opcion == 3:
    conversor("Euros", 0.0077)
elif opcion == 4:
    conversor("Yuanes", 0.056)
elif opcion == 5:
    conversor("Wondes surcoreanos", 10.37)
    print("Tienes ¥" + yen + " yenes")
else:
    print('ingresa una opción correcta, por favor')
