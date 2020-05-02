from matplotlib.pylab import *
import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *
from sympy.plotting import *
from time import *
from scipy import *
asctime()
clock()
#introducimos los datos
while True:
    try:
        B=float(input("introduzca el ángulo en grados β = "))
        except ValueError:
        print ()
        print("Cantidad Incorrecta")
        print ()
        continue
    break
while True:
    try:
        vi=float(input("introduzca la velocidad inicial en (m/s) vi = "))

    except ValueError:
        print ()
        print("Cantidad Incorrecta")
        print ()
        continue
    break
print ()
θ=((B*pi)/180)
print ("θ=",θ)
g=9.81 # m/s**2
print ()
a=tan(θ)
b=((g)/((2*vi**2)*cos(θ)**2))
print ()
ymax=(vi**2)*(np.sin(θ)*sin(θ))/(2*g)
xmax=(vi**2)*(np.sin(2*θ))/(g)
print ("................................................................................")
print ("................................................................................")
tmax=(vi*sin(θ))/(g)
tv=2*(tmax)
# Salidas de los datos calculados
print (str("La altura máxima  alcanzada por el proyectil es: Ymax")+" = "+str(ymax)+" m")
print (str("El alcance máximo horizontal  del proyectil es: Xmax")+" = "+str(xmax)+" m")
print ("................................................................................")
print ("................................................................................")
print ("La altura máxima (m) alcanzada por el proyectil es: Ymax =",format(ymax,".2f"))
print ("El alcance máximo horizontal(m) del proyectil es: Xmax =",format(xmax," .2f"))
print ("................................................................................")
print ("................................................................................")
print ("El tiempo máximo t1max (s) que alcanza el proyectil para el ángulo β es: t1max =",format(tmax,".2f"))
print ("El tiempo de vuelo t1v(s) que alcanza el proyectil para el angulo β es: t1v =",format(tv,".2f"))
print ("................................................................................")
print ("................................................................................")

# Definimos la ecuación de la trayectoria
def f(x):
    return(a*x-b*x**2)
x=np.linspace(0,xmax,500)
#creamos la figura
plt.figure("FISICA APLICADA",figsize=(10,8),dpi=80,facecolor="y",edgecolor="c")   
plt.axes(axisbg="orange")
# añadimos el titulo
title("LANZAMIENTO DE PROYECTILES", 
fontsize=15,color="blue",verticalalignment="baseline",horizontalalignment = "center")  
# añadimos el subtitulo
plt.suptitle("CINEMATICA",fontsize=20,color="red")

#añadimos las etiquetas de los ejes
xlabel("xmax",fontsize=20,color="red")                                      
ylabel("ymax",fontsize=20,color="blue")
#añadimos texto
plt.text(((np.argmax(f(x)))/2),np.max(f(x))+1,"vi=",fontsize=10)
plt.text(((np.argmax(f(x)))/2)+11,np.max(f(x))+1,(str(vi)+"m/s"),fontsize=10)
#mostrar la fecha y la hora actual formateadas :",asctime()
#mostrar el tiempo real de ejecucion de este proceso :",clock()
plt.text(2,np.max(f(x))+1,("fecha/hora:"+str(asctime())),fontsize=10,color="green")
plt.text(2,np.max(f(x))-1,("tiempo(s):"+str(clock())),fontsize=10,color="blue")

# Añadimos la rejilla en la gráfica
plt.grid(True)                                                              
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
# Añadimos los ejes 
# plt.axis("tight")                                     
                 
# dibujamos y ponemos etiquetas a la gráfica
plt.text(3,1,B,fontsize=10)
plt.plot(x, f(x), "red", linewidth = 2, label = (str(B)+"º"))   
# añadimos la leyenda
plt.legend(loc = 4,fontsize=10)                                                         
#anotaciones en el gráfico
plt.annotate('Altura Máxima',
xy = (xmax/2, ymax),
xycoords = 'data',
xytext = (-70, -50),
textcoords = 'offset points',
arrowprops = dict(arrowstyle = "->",
connectionstyle = "arc, angleA = 0,armA = 30,rad = 50"),
# dibujar tabla dentro del gráfico
valores = [[format(np.max(xmax),".2f"),format(np.min(ymax),".2f")]]
etiquetas_col = ["xmax (m)", "ymax (m)"]
plt.table(cellText=valores, colLabels = etiquetas_col, colWidths = [0.15]*len(f(x)),loc='upper right')
# guarda la gráfica con 300dpi (puntos por pulgada)en python34-ejemplos curso python
#plt.savefig("figura_Lanzamiento Proyectiles_1.pdf", dpi = 300)            
# mostramos en pantalla la gráfica
plt.show()
