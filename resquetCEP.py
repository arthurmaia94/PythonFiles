#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  resquetCEP.py
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
import requests

class BuscaCEP:
	def __init__(self):
		sg.theme('DarkAmber') 
		layout = [
			[sg.Text('CEP', size=(5,0)), sg.Input(size=(30,0),key='cep', do_not_clear=False)],
			[sg.Button('Consultar')],
			[sg.Output(size=(30,20))]
		]
		self.janela = sg.Window("Buscar CEP").layout(layout)
		
	
	def Iniciar(self):
		while True:
			self.button, self.values = self.janela.Read()
			
			cep = self.values['cep']
			cep = cep.replace("-", "").replace(".", "")
			
			if len(cep) == 8:
				link = f'https://viacep.com.br/ws/{cep}/json/'
				cep_request = requests.get(link)
				
				dic_cep = cep_request.json()
				#print(f'{dic_cep}\n--------')
				
				cep = dic_cep['cep']
				rua = dic_cep['logradouro']
				uf = dic_cep['uf']
				cidade = dic_cep['localidade']
				bairro = dic_cep['bairro']
				print(f'CEP: {cep}\nRua: {rua}\nEstado: {uf}\nCidade: {cidade}\nBairro: {bairro}\n---------')
			else:
				print("Cep Invalido")

tela = BuscaCEP()
tela.Iniciar()
