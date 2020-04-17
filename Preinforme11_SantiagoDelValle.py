import numpy as np

#Tema de ciberseguridad

print("""Bienvenido a la base de datos
Pd: esta es una versión alpha""")

x=int(input("""Por favor digite su contraseña para acceder,sir Carlos
:"""))

contraseña=[[0,1,2,3,4,8,9],[10,54,39,74,75,36,14],[1000,3000,3100,5100,4872,4789,36521],[100008,1411515,18556,23864,48562,19845,32389]]

contraseña_1= contraseña [0][5]
contraseña_2= contraseña [2][6]
contraseña_3= contraseña [3][6]
contraseña_4= contraseña [1][0]

contraseña_usuario= contraseña_1 + contraseña_2 + contraseña_3 + contraseña_4

if x==contraseña_usuario:
    print("Puede acceder")
else:
    print("Intentelo otra vez")
            
        
    
        

