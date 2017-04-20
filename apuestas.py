#!/usr/bin/python
# coding: utf8

from random import randint
import os

Salir_menu = False
Salir_apuesta = False
Salir_juego = False
saldo = 100 
apuesta = 0


while Salir_menu == False:
	
	os.system('clear')
	print "1 = Jugar" 
	print "-1 = Salir" 
	opcion=input("Que decea hacer? ")
	
	if (opcion == 1):
		
		while Salir_apuesta == False:
			
			Salir_apuesta = False
				
			print "Saldo disponible ", saldo , " €"
			apuesta=input("Quanto quiere apostar? ")
			
			if(apuesta >= 10 and apuesta <= saldo):
				while (Salir_juego == False):	
					
					Salir_juego = False
					Salir_carta = False
					J1palo = randint(1,4) 
					J2palo = randint(1,4)

					if (J1palo == 1):
						palo1 = "Picas"
					if (J1palo == 2):
						palo1 = "Corazones"
					if (J1palo == 3):
						palo1 = "Diamantes"
					if (J1palo == 4):
						palo1 = "Treboles"

					jugador1 = randint(2,14)
					jugador2 = randint(2,14)

					numero1 = jugador1
					if (jugador1 == 11):
						numero1 = "J"
					if (jugador1 == 12):
						numero1 = "Q"
					if (jugador1 == 13):
						numero1 = "K"
					if (jugador1 == 14):
						numero1 = "As"

					print "J1Saca ", numero1 , " de", palo1

					while (Salir_carta == False):
						
						if (jugador1 == jugador2 and J1palo == J2palo):
							jugador2 = randint(2,14)
							J2palo = randint(1,4)
							
						if not(jugador1 == jugador2 and J1palo == J2palo):
							Salir_carta = True

					if (J2palo == 1):
						palo2 = "Picas"
					if (J2palo == 2):
						palo2 = "Corazones"
					if (J2palo == 3):
						palo2 = "Diamantes"
					if (J2palo == 4):
						palo2 = "Treboles"
								
					numero2 = jugador2
					if (jugador2 == 11):
						numero2 = "J"
					if (jugador2 == 12):
						numero2 = "Q"
					if (jugador2 == 13):
						numero2 = "K"
					if (jugador2 == 14):
						numero2 = "As"
							
					print "J2 Saca ", numero2 , " de", palo2 

					if (jugador1 == jugador2):
						print "Empate"
						saldo = saldo - apuesta
					else:
						if ( jugador1 > jugador2):
							print "Gana J1"
							saldo = (saldo - apuesta) + (apuesta * 2)		
						else:
							print "Vaya malisimo, J2 Gana"
							saldo = saldo - apuesta
							
					print "Saldo disponible ", saldo , " €"
					tecla=raw_input("Introduzca tecla para continuar ")
					Salir_juego = True
					Salir_apuesta = True
			else: 
				print "Imposible apostar menos de 10 euros " 
	
	if (opcion == -1 or saldo < 10):
		print "Quedas fuera no tenes suficiente saldo para apostar"
		print "Quedas fuera de combate "
Salir_menu = True
