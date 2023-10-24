def countsticks(num):
    sticks = ""
    if num >0 and num < 101:
        for i in range(num):
            if i % 5 == 0:
                sticks += " |"
            else:
                sticks += "|"
        return print(sticks)
    
    else:
        print("Ingrese un numero dentro de 0 a 100")

countsticks(33)