import random
import math


#logaritmo natural = math.log()

t_entre_llegada = int(raw_input("INGRESA TIEMPO ENTRE LLEGADA:    "))
t_minimo = int(raw_input("TIEMPO MINIMO EN CORTE:    "))
t_maximo = int(raw_input("TIEMPO MAXIMO EN CORTE:    "))
total_de_clientes = int(raw_input("TOTAL DE CLIENTES:     "))

t_llegada_total = 0
t_salida_anterior = 0
espera_total_1 = 0
t_corte_1 = 0

tiempo_llegada = []
tiempo_corte = []
cli = []
sali = []
espe = []

for i in range(total_de_clientes):
	R = random.random()
	t_llegada = abs((((-1)*(t_entre_llegada))*((math.log(R)))))#tiempo de llegada de un solo cliente
	t_llegada_total = t_llegada + t_llegada_total # tiempo de llegada sumado
	tiempo_llegada.append(t_llegada_total) #agregar el tiempo de llegada a la lista
	t_corte = ((t_minimo + ((t_maximo - t_minimo) * (R)))) #tiempo de corte
	tiempo_corte.append(t_corte)
	cli.append(i) #numrto de cliente agregado a la lista
	t_salida = t_llegada_total + t_corte # tiempo de salida 
	sali.append(t_salida)
	print "CLIENTE    " + str(i)
	print "TIEMPO DE LLEGADA DEL CLIENTE   " + str(t_llegada)
	print "TIEMPO DE LLEGADA   " + str(t_llegada_total)
	print "TIEMPO DE CORTE   " + str(t_corte)
	print "TIEMPO DE SALIDA   " + str(t_salida)
	
	
	espera_total = (t_salida_anterior - t_llegada_total)

	if espera_total < 0:
		espera_total = 0		
	
	print "TIEMPO DE ESPERA    " + str(espera_total)
	espe.append(espera_total)

	t_salida_anterior = t_salida
	
	espera_total_1 = espera_total + espera_total_1
	t_corte_1 = (t_corte) + (t_corte_1)


long_de_fila = (espera_total_1) / (t_salida_anterior) 
t_espera_promedio = (espera_total_1) / (total_de_clientes)
uso_instalacion = (t_corte_1) / (t_salida_anterior) 

print ("LONGITUD PROMEDIO DE FILA   %.2f" %(long_de_fila))
print ("TIEMPO DE ESPERA PROMEDIO     %.2f" %(t_espera_promedio))
print ("USO PROMEDIO DE LA INSTALACION      %.2f" %(uso_instalacion))



sep = '|{}|{}|{}|{}|{}|'.format('-'*10, '-'*16, '-'*10, '-'*16, '-'*16)
print('{0}\n| CLIENTE  |    LLEGADA     |  CORTE   |     SALIDA     |     ESPERA     |\n{0}'.format(sep))
for cliente,llegada,corte,salida,espera in zip(cli,tiempo_llegada, tiempo_corte,sali,espe):
	#print ('tiempo de llegada:{0:.2f},  tiempo de corte: {0:.2f}'.format(llegada,corte))
	print('| {:>8.2f} | {:>14.2f} | {:>8.2f} | {:>14.2f} | {:>14.2f} |\n{}'.format(cliente,llegada,corte,salida,espera,sep))

	

