# Make you Cry ransomware(makeUcry)
Este es un proyecto final de  la materia IDS340(Desarrollo de software 1), el objetivo es crear un malware que encrypte los archivos de la victima, para enciptar los archivos el se genera una llave  que envia por telegram utilizando la API de telegram para controlar bots. Utiliza un generador que busca los archivos a encriptar basandose en las extenciones de archivos asignadas(.txt, .zip, .sh...) y lo pasa a una funcion que lee su contenido, lo encripta y reescribe el archivo con el contenido encriptado.

#Como correrlo
debes instalar las librerias utilizadas. ```pip install pycryptodome```

