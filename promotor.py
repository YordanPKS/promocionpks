
import os 
import time 
import platform 

# Cambia esto por el número de intentos deseados 
crash = 1  

def open_link(link): 
    if platform.system() == "Windows": 
        os.startfile(link) 
    elif platform.system() == "Darwin":  # macOS 
        os.system(f"open {link}") 
    else:  # Asumimos que es Linux u otro 
        os.system(f"xdg-open {link}") 

def main(): 
    # Abrimos el archivo y leemos los números
    with open("numeros.txt", "r") as file:
        numeros = file.readlines()

    for combnum in numeros:
        combnum = combnum.strip()  # Eliminamos espacios en blanco y saltos de línea
        link = f"https://wa.me/{combnum}/?text=agg" 
        
        for i in range(crash): 
            open_link(link) 
            time.sleep(20)  # Espera 40 segundos entre intentos 

def run_tool(): 
    print("Gracias por utilizar la herramienta...\n") 
    time.sleep(4) 
    print("Inicializando herramienta...") 
    time.sleep(4) 
    print("\n\n") 
    main() 

# Ejecutamos directamente la función sin pedir datos al usuario. 
run_tool()