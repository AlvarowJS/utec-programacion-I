import math

pi = math.pi

def area_circulo(r):
    area = pi * r**2
    return area

def area_cuadrado(l):
    area = l**2
    return area

def area_triangulo(base=2, altura=1):
    area = (base * altura)/2
    return area
