#!/usr/bin/python
#coding: utf-8

#       CopyRight 2016 Allan Psicobyte (psicobyte@gmail.com)
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.


import random
import mandalillo

aleatoria = "".join([random.choice("01") for b in range(1,41)])

nombre_archivo = aleatoria + ".png"

imagen = mandalillo.Mandalillo(aleatoria)
salida = imagen.dibuja()

salida.save(nombre_archivo)
