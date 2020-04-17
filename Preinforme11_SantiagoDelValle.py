import numpy as np

#Tema de ciberseguridad
#Creación de usuario

contraseña=[[0,1,2,3,4,8,9],[10,54,39,74,75,36,14],[1000,3000,3100,5100,4872,4789,36521],[100008,1411515,18556,23864,48562,19845,32389]]

User_Name= input("Por favor digite su nombre de usuario")

n= int(input("Digite un numero entre 1 y 8"))
z= int(input("Digite un numero entre 1 y 8"))
x= int(input("Digite un numero entre 1 y 8"))
k= int(input("Digite un numero entre 1 y 8"))
p= int(input("Digite un numero entre 1 y 8"))
o= int(input("Digite un numero entre 1 y 8"))

if 0<=n<=8 and 0<=z<=8 and 0<=x<=8 and 0<=k<=8 and 0<=p<=8 and 0<=o<=8:

    parte_1= contraseña[n-1][z-1]
    parte_2= contraseña[x-1][k-1]
    parte_3= contraseña[p-1][o-1]

    contraseña_Final= parte_1 * parte_2 * parte_3

    print("Su contraseña es",contraseña_Final)
else:
    print("Por favor haga bien el procedimiento")