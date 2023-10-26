import imageio.v2 as imageio
import numpy as np

# UTILIZAR ESTAS FUNCIONES PARA COMPROBAR SI SU SOLUCIÓN ES CORRECTA.
# NO LO VAYAN A INCLUIR CUANDO SUBAN SU SOLUCIÓN A GRADESCOPE



def leer_imagen(ruta):
    """
    La función leer_imagen recibe un string con la ruta
    de una imagen en formato BMP y retorna una lista de
    tres dimensiones con el mapa de bits de la imagen.
    Asimismo, convertimos la lista de numpy a una lista
    común y corriente.
    """
    np_array = np.array(imageio.imread(ruta), dtype='int')
    # noinspection PyTypeChecker
    lista_3d = np_array.tolist()
    return lista_3d

def guardar_imagen(ruta, lista_3d):
    """
    La función guardar_imagen recibe una lista de 3
    dimensiones con el mapa de bits de la imagen
    y retorna la imagen en formato bmp.
    """
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))






# NO UTILICEN INPUTS NI PRINTS EN LA ENTREGA FINAL EN GRADESCOPE




class Solution:

    def pregunta_1(self, imagen, radius, center): 
        new_imagen = imagen.copy()
        c0 = center[0]
        c1 = center[1]
        r = radius    
      
        matriz = np.array(new_imagen)
        y = matriz.shape[0]
        x = matriz.shape[1]


        i, j = np.ogrid[0:y, 0:x]
       

        result = (j - c0)**2 + (i - c1)**2 > r**2
        matriz[result,:]=0
        new_imagen = matriz
        return new_imagen 

    
    def pregunta_2(self, imagen, M):
        new_imagen = imagen.copy()
        kernel = [[1/(M*M) for x in range(M)] for _ in range(M)]
        off_set = len(kernel) // 2


        

        return new_imagen



    def pregunta_3(self, imagen, color, factor): 
        
        new_imagen = imagen.copy()
        

        return new_imagen
    

solucion = Solution()
imagen_original = leer_imagen('ruta.bmp')
nueva_imagen = solucion.pregunta_1(imagen_original, 250, (309,340))
guardar_imagen('jojo-circle.bmp', nueva_imagen)

