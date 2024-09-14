def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad.

    Parámetros:
    temperaturas (list of list of float): Una lista que contiene listas de temperaturas para cada ciudad.

    Retorna:
    dict: Un diccionario donde las claves son los índices de las ciudades y los valores son las temperaturas promedio.
    """
    promedios = {}

    for i, ciudad_temperaturas in enumerate(temperaturas):
        # Calcula el promedio de temperaturas para la ciudad actual
        total_temperaturas = sum(ciudad_temperaturas)
        numero_de_temperaturas = len(ciudad_temperaturas)
        promedio = total_temperaturas / numero_de_temperaturas
        promedios[f'Ciudad_{i + 1}'] = promedio

    return promedios


# Ejemplo de uso
temperaturas = [
    [22.5, 23.0, 21.5, 24.0],  # Temperaturas para la Ciudad 1 durante 4 semanas
    [19.0, 20.5, 18.5, 21.0],  # Temperaturas para la Ciudad 2 durante 4 semanas
    [15.5, 16.0, 14.5, 17.0]  # Temperaturas para la Ciudad 3 durante 4 semanas
]

promedios = calcular_temperatura_promedio(temperaturas)
print(promedios)
