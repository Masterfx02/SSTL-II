#ACTIVIDAD 2: Validación de expresiones regulares
#YESHUA NEFTALI ESPINOZA GONZÁLEZ
#SEMINARIO DE SOLUCIÓN DE TRADUCTORES DE LENGUAJE II

import tkinter as tk
import re

def validar_telefono():
    telefono = entry_telefono.get()
    if re.fullmatch(r'\d{10}', telefono):
        label_result_telefono.config(text="Teléfono válido.", fg="green")
    else:
        label_result_telefono.config(text="Teléfono inválido.", fg="red")

def validar_correo():
    correo = entry_correo.get()
    if re.fullmatch(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', correo):
        label_result_correo.config(text="Correo válido.", fg="green")
    else:
        label_result_correo.config(text="Correo inválido.", fg="red")

def validar_curp():
    curp = entry_curp.get()
    if re.fullmatch(r'[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]\d', curp):
        label_result_curp.config(text="CURP válido.", fg="green")
    else:
        label_result_curp.config(text="CURP inválido.", fg="red")

def validar_rfc():
    rfc = entry_rfc.get()
    if re.fullmatch(r'[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}', rfc):
        label_result_rfc.config(text="RFC válido.", fg="green")
    else:
        label_result_rfc.config(text="RFC inválido.", fg="red")

def validar_ipv4():
    ipv4 = entry_ipv4.get()
    if re.fullmatch(r'(\d{1,3}\.){3}\d{1,3}', ipv4) and all(0 <= int(num) <= 255 for num in ipv4.split('.')):
        label_result_ipv4.config(text="IP válida.", fg="green")
    else:
        label_result_ipv4.config(text="IP inválida.", fg="red")

def validar_fecha():
    fecha = entry_fecha.get()
    if re.fullmatch(r'([0-2]\d|3[01])/(0\d|1[0-2])/\d{2}', fecha):
        label_result_fecha.config(text="Fecha válida.", fg="green")
    else:
        label_result_fecha.config(text="Fecha inválida.", fg="red")

# Configuración de la interfaz
root = tk.Tk()
root.title("Validador de Cadenas")
root.geometry("600x250")

# Entradas y botones para cada tipo de validación
tk.Label(root, text="Teléfono (10 dígitos):").grid(row=0, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Validar Teléfono", command=validar_telefono).grid(row=0, column=2, padx=10, pady=5)
label_result_telefono = tk.Label(root, text="")
label_result_telefono.grid(row=0, column=3, padx=10, pady=5)

tk.Label(root, text="Correo Electrónico:").grid(row=1, column=0, padx=10, pady=5)
entry_correo = tk.Entry(root)
entry_correo.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Validar Correo", command=validar_correo).grid(row=1, column=2, padx=10, pady=5)
label_result_correo = tk.Label(root, text="")
label_result_correo.grid(row=1, column=3, padx=10, pady=5)

tk.Label(root, text="CURP:").grid(row=2, column=0, padx=10, pady=5)
entry_curp = tk.Entry(root)
entry_curp.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Validar CURP", command=validar_curp).grid(row=2, column=2, padx=10, pady=5)
label_result_curp = tk.Label(root, text="")
label_result_curp.grid(row=2, column=3, padx=10, pady=5)

tk.Label(root, text="RFC:").grid(row=3, column=0, padx=10, pady=5)
entry_rfc = tk.Entry(root)
entry_rfc.grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Validar RFC", command=validar_rfc).grid(row=3, column=2, padx=10, pady=5)
label_result_rfc = tk.Label(root, text="")
label_result_rfc.grid(row=3, column=3, padx=10, pady=5)

tk.Label(root, text="Dirección IP v4:").grid(row=4, column=0, padx=10, pady=5)
entry_ipv4 = tk.Entry(root)
entry_ipv4.grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Validar IP", command=validar_ipv4).grid(row=4, column=2, padx=10, pady=5)
label_result_ipv4 = tk.Label(root, text="")
label_result_ipv4.grid(row=4, column=3, padx=10, pady=5)

tk.Label(root, text="Fecha de Cumpleaños (DD/MM/AA):").grid(row=5, column=0, padx=10, pady=5)
entry_fecha = tk.Entry(root)
entry_fecha.grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Validar Fecha", command=validar_fecha).grid(row=5, column=2, padx=10, pady=5)
label_result_fecha = tk.Label(root, text="")
label_result_fecha.grid(row=5, column=3, padx=10, pady=5)

root.mainloop()
