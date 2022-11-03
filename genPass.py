#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  genPass.py
#  
#  Copyright 2022 Arthur Maia <suporte@ex2.com.br>
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
#  

import PySimpleGUI as sg
import random

def criar_senha():
	sg.theme('DarkAmber')
	layout = [
		[sg.Text('Qtd Caracteres:', size=(16,0)), sg.Input(size=(30,5), key='qtd', do_not_clear=False)],
		[sg.Button('Gerar Senha'), sg.Button('Nova Senha')],
		[sg.Output(size=(45,2))],
		[sg.Text('\nDev By Arthur', size=(45,2), justification='center')]
	]
	return sg.Window('GenPass', layout=layout, finalize=True)

# Criar a Janela
janela = criar_senha()

while True:
	event, values = janela.read()
	if event == sg.WIN_CLOSED:
		break
	
	elif event == 'Gerar Senha':
		lowEnter = "abcdefghijklmnopqrstuvxz"
		upEnter = lowEnter.upper()
		numEnter = "1234567890"
		symEnter = "@#$%&*?!"

		allEnter = lowEnter + upEnter + numEnter + symEnter
		length = int(values['qtd'])

		passgen="".join(random.sample(allEnter, length))
		print(passgen)
		
	elif event == 'Nova Senha':
		janela.close()
		janela = criar_senha()

