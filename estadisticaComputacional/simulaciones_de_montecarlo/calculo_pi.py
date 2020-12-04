import random
import math
from estadisticas_simulaciones import media, desviacion_estandar

def aventar_agujas(numero_agujas):
    adentro_del_circulo = 0 

    for _ in range(numero_agujas):
        #El círculo tiene un radio de 1
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        #Teorema de Pitagoras
        distancia_desde_centro = math.sqrt(x ** 2 + y ** 2)

        #Si la distancia desde el centro es menor a 1, la aguja está dentro del circulo
        if distancia_desde_centro <= 1:
            adentro_del_circulo += 1

    return (4 * adentro_del_circulo)  / numero_agujas

def estimacion(numero_agujas, numero_intentos):
    estimados = []
    for _ in range(numero_intentos):
        estimacion_pi = aventar_agujas(numero_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    #Sigma o desviación estandar
    sigma = desviacion_estandar(estimados)

    print(f'Estimación = {round(media_estimados, 5)}, sigma = {round(sigma, 5)}, agujas aventadas = {numero_agujas}')
    return (media_estimados, sigma)

def estimar_pi(precision, numero_intentos):
    numero_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96: #para obtener un 95% de confiabilidad
        media, sigma = estimacion(numero_agujas, numero_intentos)
        numero_agujas *= 2
    return media

if __name__ == '__main__':
    estimar_pi(0.01, 1000)
