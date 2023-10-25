matrice = [[[7, 17, 27], 
           [8, 18, 28], 
           [9, 19, 29]],

        [[4, 14, 24], 
         [5, 15, 25], 
         [6, 16, 26]],

        [[1, 11, 21], 
         [2, 12, 22], 
         [3, 13, 23]]]


def suma(matriz):
    total = 0
    for axis2 in matriz:
        for axis1 in axis2:
            for axis0 in axis1:
                total += axis0
    return total

def contar(matriz):
    count = 0
    for axis2 in matriz:
        for axis1 in axis2:
            for axis0 in axis1:
                count += 1
    return count

def maximo(matriz):
    max_element = matriz[0][0][0]
    for axis2 in matriz:
        for axis1 in axis2:
            for axis0 in axis1:
                if max_element < axis0:
                    max_element = axis0 
    return max_element

def minimo(matriz):
    max_element = matriz[0][0][0]
    for axis2 in matriz:
        for axis1 in axis2:
            for axis0 in axis1:
                if max_element > axis0:
                    max_element = axis0 
    return max_element

def pixel_mas_rojo(matriz):
    maximo_rojo = matriz[0][0][0]
    maximo_pixel = matriz[0][0]

    for axis2 in matriz:
        for axis1 in axis2:
            if axis1[0] > maximo_rojo:
                maximo_rojo = axis1[0]
                maximo_pixel = axis1


    return maximo_pixel    

def pixel_mas_verde(matriz):
    maximo_verde = matriz[0][0][1]
    maximo_pixel = matriz[0][0]

    for axis2 in matriz:
        for axis1 in axis2:
            if axis1[1] > maximo_verde:
                maximo_verde = axis1[1]
                maximo_pixel = axis1


    return maximo_pixel    

def pixel_mas_azul(matriz):
    maximo_azul = matriz[0][0][2]
    maximo_pixel = matriz[0][0]

    for axis2 in matriz:
        for axis1 in axis2:
            if axis1[2] > maximo_azul:
                maximo_azul = axis1[2]
                maximo_pixel = axis1


    return maximo_pixel   

def grises(matriz):
    axis2_gris = []
    for axis2 in matriz:
        axis1_gris = []
        for axis1 in axis2:
            # luminancia = int(0.21 * axis1[0] + 0.71 * axis1[1] + 0.07 * axis1[2])
            average = int(axis1[0] + axis1[1] + axis1[2])/3

            axis1_gris.append((average, average, average))
        axis2_gris.append(axis1_gris)
    return axis2_gris




print(suma(matrice))
print(contar(matrice))
print(maximo(matrice))
print(minimo(matrice))
print(pixel_mas_rojo(matrice))
print(pixel_mas_verde(matrice))
print(pixel_mas_azul(matrice))
print(grises(matrice))

