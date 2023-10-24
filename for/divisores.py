def divisores(num):
    divisores = []
    for i in range(1, num+1):
        if num % i == 0:
            divisores.append(i)
    return divisores

def secuencia(first, last, jumps):
    secuencia = []
    for i in range(last, first-1, -jumps):
        secuencia.append(i)    
    return secuencia



print(divisores(6))
print(secuencia(-7,23,2))
print(secuencia(25,90,5))