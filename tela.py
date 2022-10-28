#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tela.py
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

class TelaPython:
	def __init__(self):
		layout = [
			[sg.Text('Nome', size=(5,0)), sg.Input(size=(30,0),key='nome')],
			[sg.Text('Idade', size=(5,0)), sg.Input(size=(30,0),key='idade')],
			[sg.Text('Qual provedor de e-mail?')],
			[sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Oulook', key='outlook')],
			[sg.Button('Enviar Dados')],
			[sg.Output(size=(30,20))]
		]
		self.janela = sg.Window("Dados do Usuario").layout(layout)
		
	
	def Iniciar(self):
		while True:
			self.button, self.values = self.janela.Read()
			
			# Lista todos os valores recebidos
			#print(self.values)
			
			# Separando os valores por varivaveis
			nome = self.values['nome']
			idade = self.values['idade']
			provedorGmail = self.values['gmail']
			provedorOutlook = self.values['outlook']
			
			print(f'Nome: {nome}')
			print(f'Idade: {idade}')
			print(f'Aceita Gmail: {provedorGmail}')
			print(f'Aceita Outlook: {provedorOutlook}')

tela = TelaPython()
tela.Iniciar()
