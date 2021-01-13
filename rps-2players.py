#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rps.py
#  
#  Copyright 2021 Arthur Maia <arthur@ex2.com.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import random
#game_list = ['Pedra', 'Papel', 'Tesoura']
player1 = input("Player 1, digite seu nome: ")
player2 = input("Player 2, digite seu nome: ")

p1 = 0
p2 = 0

print("Score: "+ player1 +": " + str(p1) + "\n"+ player2 +": " + str(p2))
# The Loop
run = True
while run:
	p1_choice = input("P1: Pedra, Papel, Tesoura ou Sair: ")
	p2_choice = input("P2: Pedra, Papel, Tesoura ou Sair: ")
	if p1_choice == p2_choice:
		print("Empate")
	elif p2_choice == 'Pedra':
		if p1_choice == 'Tesoura':
			print(player2 + "Venceu!")
			p2 +=1
		else:
			print(player1 + "Venceu!")
			p1 +=1
	elif p2_choice == 'Papel':
		if p1_choice == 'Pedra':
			print(player2 + "Venceu!")
			p2 +=1
		else:
			print(player1 + "Venceu!")
			p1 +=1
	elif p2_choice == 'Tesoura':
		if p1_choice == 'Papel':
			print(player2 + "Venceu!")
			p2 +=1
		else:
			print(player1 + "Venceu!")
			p1 +=1
	elif p1_choice == 'Sair':
		break
	else:
		print("Comando Invalido")
		
	print("Player 2: " + p2_choice)
	print("Player 1: " + p1_choice)
	print("")
	print ("Score: "+ player1 +": " + str(p1) + "\n"+ player2 +": " + str(p2))
	print("")
