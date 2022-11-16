#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pyflag.py
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

from PIL import Image
import os
 
INPUT_FOLDER="input"
OUTPUT_FOLDER="output"
 
def in_path(filename):
	 return os.path.join(INPUT_FOLDER,filename)
	 

def triangle(size):
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)  
	image = Image.new("RGB", (size, size), WHITE)
	
	for x in range(size):
		for y in range(size):
			if x < y:
				image.putpixel((x, y), BLACK)
	return image
		
def bandeira_france(height):
	Width = 3*height//2
	BLUE = (0, 85, 164)
	WHITE = (255,255,255)
	RED = (239,64,53) 
	image = Image.new("RGB", (Width, height), WHITE)
	
	offset =Width//3
	for x in range (offset):
		for y in range(height):
			image.putpixel((x, y), BLUE)
			image.putpixel((x + 2*offset, y), RED)
	return image
	
if __name__ == "__main__":
	bandeira = bandeira_france(700)
	bandeira.show()
