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
game_list = ['Pedra', 'Papel', 'Tesoura']
computer = c = 0
command = p = 0
print("Score: Computer: " + str(c) + "\nPlayer: " + str(p))
# The Loop
run = True
while run:
	computer_choice = random.choice(game_list)
	command = input("Pedra, Papel, Tesoura ou Sair: ")
	if command == computer_choice:
		print("Tie")
	elif command == 'Pedra':
		if computer_choice == 'Tesoura':
			print("Jogador Venceu!")
			p +=1
		else:
			print("Computador Venceu!")
			c +=1
	elif command == 'Papel':
		if computer_choice == 'Pedra':
			print("Jogador Venceu!")
			p +=1
		else:
			print("Computador Venceu!")
			c +=1
	elif command == 'Tesoura':
		if computer_choice == 'Papel':
			print("Jogador Venceu!")
			p +=1
		else:
			print("Computador Venceu!")
			c +=1
	elif command == 'Sair':
		break
	else:
		print("Comando Invalido")
		
	print("Player: " + command)
	print("Computer: " + computer_choice)
	print("")
	print ("Score: Computer: " + str(c) + "\nPlayer: " + str(p))
	print("")
