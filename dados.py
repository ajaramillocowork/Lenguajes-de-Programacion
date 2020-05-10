import random

def lanzarDados(dado1, dado2):
    return dado1 + dado2

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
print("Dado 1:", dado1)
print("Dado 2;", dado2)
print("Obtuviste un", lanzarDados(dado1, dado2))
