import random
import math
import time 

#logaritmo natural = math.log()

t_entre_llegada = int(raw_input("INGRESA TIEMPO ENTRE LLEGADA:    "))
t_minimo = int(raw_input("TIEMPO MINIMO EN CORTE:    "))
t_maximo = int(raw_input("TIEMPO MAXIMO EN CORTE:    "))
can_barberos = int(raw_input("CANTIDAD DE BARBEROS:     "))
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
tiempo_llegada_entero = []
sali_entero = []
barbero = []

barberos_ocupados = 1

arreglo_barberos = []

for i in range(can_barberos):
	arreglo_barberos.append([0,0,i])

for i in range(total_de_clientes):
	R = random.random()
	t_llegada = abs((((-1)*(t_entre_llegada))*((math.log(R)))))#tiempo de llegada de un solo cliente
	t_llegada_total = t_llegada + t_llegada_total # tiempo de llegada sumado
	tiempo_llegada.append(t_llegada_total) #agregar el tiempo de llegada a la lista
	tiempo_llegada_entero.append(int(t_llegada_total))
	t_corte = ((t_minimo + ((t_maximo - t_minimo) * (R)))) #tiempo de corte
	tiempo_corte.append(t_corte)
	cli.append(i) #numrto de cliente agregado a la lista

	espera_total = (t_salida_anterior - t_llegada_total)

	for b in arreglo_barberos:
		if b[0] == 0:
			espera_total = 0
			b[0] = 1
			b[1] = t_llegada_total + t_corte
			barbero.append(b[2])

		elif b[1] < t_llegada_total:
			espera_total = 0
			b[1] = t_llegada_total + t_corte
			barbero.append(b[2])

			
		
	print "TIEMPO DE ESPERA    " + str(espera_total)
	espe.append(espera_total)

	t_salida = t_llegada_total + t_corte + espera_total # tiempo de salida 
	sali.append(t_salida)
	sali_entero.append(int(t_salida))
	
	t_salida_anterior = t_salida
	espera_total_1 = espera_total + espera_total_1#_________________________________
	t_corte_1 = (t_corte) + (t_corte_1)
	



long_de_fila = (espera_total_1) / (t_salida_anterior) 
t_espera_promedio = (espera_total_1) / (total_de_clientes)
uso_instalacion = (t_corte_1) / (t_salida_anterior) 

print ("LONGITUD PROMEDIO DE FILA   %.2f" %(long_de_fila))
print ("TIEMPO DE ESPERA PROMEDIO     %.2f" %(t_espera_promedio))
print ("USO PROMEDIO DE LA INSTALACION      %.2f" %(uso_instalacion))
print "\n\n"


sep = '|{}|{}|{}|{}|{}|{}|'.format('-'*10, '-'*16, '-'*10, '-'*16, '-'*16, '-'*16)
print('{0}\n| CLIENTE  |    LLEGADA     |  CORTE   |     SALIDA     |     ESPERA     |     BARBERO    |\n{0}'.format(sep))
for cliente,llegada,corte,salida,espera,barb in zip(cli,tiempo_llegada, tiempo_corte,sali,espe,barbero):
	#print ('tiempo de llegada:{0:.2f},  tiempo de corte: {0:.2f}'.format(llegada,corte))
	print('| {:>8.2f} | {:>14.2f} | {:>8.2f} | {:>14.2f} | {:>14.2f} | {:>14.2f} |\n{}'.format(cliente,llegada,corte,salida,espera,barb,sep))


raw_input("")

clientese = 1
clientess = 1

for t in range(1, int(t_salida_anterior)+1):
	time.sleep(1)
	print t
	if t in tiempo_llegada_entero:
		print ("llego cliente %s" %(clientese))
		clientese += 1
	if t in sali_entero:
		print ("salio cliente %s" %(clientess))
		clientess += 1


	


