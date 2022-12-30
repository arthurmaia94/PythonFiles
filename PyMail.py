#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  notify.py
#  
#  Copyright 2022 Arthur Maia <contato.94tech@gmail.com>
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

import requests
import smtplib
import email.message

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)

def enviar_email(cotacao):
    #valor_notificacao = 6.00
    corpo_email = f"<p>Dólar está abaixo de R$6.00.<br />Cotação atual: R$<strong>{cotacao}</strong></p>"
    
    msg=email.message.Message()
    msg['Subject'] = "Cotação do Dólar"
    msg['From'] = 'enviar@email.com'
    msg['To'] = 'receber@gmail.com'
    password = 'senha-enviar'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']],  msg.as_string().encode('utf-8') )
    print('Email Enviado')

if cotacao < 6.00:
    enviar_email(cotacao)
else:
    print("E-mail não Enviado")
