import numpy as np

#Tema de ciberseguridad
#Creación de usuario

contraseña=[[0,1,2,3,4,8,9],[10,54,39,74,75,36,14],[1000,3000,3100,5100,4872,4789,36521],[100008,1411515,18556,23864,48562,19845,32389]]

y=int(input("Digite el codigo de su key card"))

parte_1= contraseña[3][4]
parte_2= contraseña[2][2]
parte_3= contraseña[1][5]

contraseña_Final= parte_1 * parte_2 * parte_3

Key_Card= 369857100

if y==Key_Card:
    x=int(input("Digite su contraseña"))
    if x==contraseña_Final:
        print("Puede acceder")
    else:
        print("Su contraseña esta mal, intente denuvo")
else:
    print("El codigo de la key card es incorrecto , intente denuevo") 