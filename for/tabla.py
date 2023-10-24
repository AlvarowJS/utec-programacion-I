def tabla(num):
    body = "  "
    if num > 0 and num < 11:

        for i in range(1, 11):
            body += "  "+"{:3d}".format(i)

        for y in range(1, num+1):
            
            body += '\n' + "{:2d}".format(y) + "  "
            for x in range(1,11):
                body += "{:3d}".format(x * y) + "  "
        
        print(body)
    
    else:
        print('ingrese un valor dentro del rango del 1 al 10')
# tabla(4)
# tabla(7)
tabla(12)
