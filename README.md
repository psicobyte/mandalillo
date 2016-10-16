# mandalillo

(esta es la versión para Python 3)

Pequeño módulo que genera una imagen basándose en una cadena conteniendo una sucesión arbitraria de cuarenta unos y ceros. Cada cadena concreta tiene su propia imagen.

(en la rama mandalillo25 de este proyecto hay una versión que usa una sucesión de 25 unos y ceros)

## Requisitos:

mandalillo usa los siguientes módulos:

* copy
* math
* re
* sys
* Pillow

## Uso:

mandalillo.pl está ideado para ser usado como módulo en otros programas de este modo:

    import mandalillo

    cadena = "0000100110011101011101000010010010110100"

    imagen = mandalillo.Mandalillo(cadena)
    salida = imagen.dibuja()
    salida.save("salida.png")


El método `dibuja` del objeto `Mandalillo` retorna unu objeto `Image` de `PIL`

Mandalillo también puede ser usado independientemente, del modo

    mandalillo.py STRING

por ejemplo:

mandalillo.py 0000100110011101011101000010010010110100

## Archivos en este repo:

archivo | Descripción
-------|--------
mandalillo.py | El módulo en sí.
ejemplo_random.py | Script de ejemplo que usa el módulo mandfalillo.pl para generar una imagen aleatoria
img | Directorio conteniendo los iconos, colores, etc que se usan para componer la imagen final
ejemplos | Directorio con algunos ejemplos aleatorios generados con mandalillo.pl
fuentes_de_las_imagenes | Archivos XCF usador para crear las imágense del directorio img
LICENSE | Licencia (GPL3)
README.MD | Este documento
