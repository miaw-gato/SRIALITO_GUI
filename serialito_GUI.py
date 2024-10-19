import tkinter as GUI
import serial
import time

ventana = GUI.Tk()

PUERTO = "COM3"
arduino = None

def CONECTAR():
    global arduino, PUERTO
    PUERTO = EntryCOM.get()
    try:
        arduino = serial.Serial(port=PUERTO, baudrate=115200, timeout=.1)
        print(f"Conectado a {PUERTO}")
    except serial.SerialException:
        print(f"No se pudo conectar al puerto {PUERTO}")

def SEND():
    if arduino and arduino.is_open:
        print("función ENVÍO DE DATOS")
        x = SpinDATA.get()
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        data = arduino.readline().decode('utf-8').strip()  # Corregido
        LabelRECIVE.config(text=f"Dato recibido: {data}")
    else:
        print("El puerto no está conectado")

def CERRAR():
    if arduino and arduino.is_open:
        print("Cerrando puerto...")
        arduino.close()
    ventana.destroy()

# Instancia de los objetos
LabelCOM_NAME = GUI.Label(ventana, text="Escribe el nombre del puerto; ejem: COM2")
EntryCOM = GUI.Entry(ventana)
BotonCONECT = GUI.Button(ventana, text="CONECTAR", command=CONECTAR)
SpinDATA = GUI.Spinbox(ventana, from_=0, to=500)
BotonSEND = GUI.Button(ventana, text="ENVIAR", command=SEND)
LabelRECIVE = GUI.Label(ventana, text="Dato recibido =")
BotonCerrar = GUI.Button(ventana, text="SALIR", command=CERRAR)

# Incrustación en VENTANA
LabelCOM_NAME.pack(padx=1, pady=2)
EntryCOM.pack(padx=1, pady=2)
BotonCONECT.pack(padx=1, pady=2)
SpinDATA.pack(padx=1, pady=2)
BotonSEND.pack(padx=1, pady=2)
LabelRECIVE.pack(padx=1, pady=2)
BotonCerrar.pack(padx=1, pady=2)

ventana.mainloop()
