#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  todo.py
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

def criar_tarefa():
	sg.theme('DarkAmber')
	linha = [
		[sg.Checkbox(''),sg.Input('')]
	]
	layout = [
		[sg.Frame('Tarefas', layout=linha, key='container')],
		[sg.Button('Nova Tarefa'), sg.Button('Resetar')],
		[sg.Text('\nDesenvolvido por: Arthur Maia', justification='center', size=(50,2))]
	]
	return sg.Window('Lista de Tarefas', layout=layout, finalize=True)

# Criar a Janela
janela = criar_tarefa()

# Criar regras
while True:
	event, values = janela.read()
	if event == sg.WIN_CLOSED:
		break
		
	elif event == 'Nova Tarefa':
		janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
	elif event == 'Resetar':
		janela.close()
		janela = criar_tarefa()
	
