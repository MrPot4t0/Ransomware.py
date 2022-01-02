# Make you Cry ransomware(makeUcry)
Este es un proyecto final de  la materia IDS340(Desarrollo de software 1), el objetivo es crear un malware que encrypte los archivos de la victima, para enciptar los archivos el se genera una llave  que envia por telegram utilizando la API de telegram para controlar bots. Utiliza un generador que busca los archivos a encriptar basandose en las extenciones de archivos asignadas(.txt, .zip, .sh y otras.) y lo pasa a una funcion que lee su contenido, lo encripta y reescribe el archivo con el contenido encriptado.

se pueden agregar extenciones de archivos que suelen ser importantes dentro del sistema operativo editando la variable `extenciones`
![image](https://user-images.githubusercontent.com/90008286/147864733-92e86068-d2ce-4e65-815f-244ddbe234c5.png)
Cuidado! dependiendo de lo que encriptas puedes dañar el sistema operativo

# Como correrlo
instalar todas las librerias utilizadas
lista de las librerias utilizadas
  -pycryptodome (Fernet)
  -tkitner
  -Platform
  -Requests
  -tkinter
 
forma de instalarlo --> pip install + libreria
ejemplo ---> ```pip install pycryptodome``` ya sea en powershell o linux

configurar el directorio objetivo cambiando las variables linux dir y windows dir por string que contengan la direccion que quieras encriptar
![image](https://user-images.githubusercontent.com/90008286/147864611-4b7d39a0-a512-43b5-b4b8-9b47ff6fb4bc.png)

# Como recibir la clave utilizando el bot de telegram
Para ello hay que crear un bot de telegram y obtener el id del chat al que quieras enviar el mensaje
![image](https://user-images.githubusercontent.com/90008286/147864664-8b18a0b2-1b50-4ec8-bf54-e53a3aed9d3b.png)

Malware hecho con popositos educativos, utilizar este codigo con responsabilidad



