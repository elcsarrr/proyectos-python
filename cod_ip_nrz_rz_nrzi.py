from PIL import Image, ImageTk
from tkinter import *
from matplotlib.backends.backend_tkagg import*
from matplotlib.figure import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import ttk,messagebox

root = Tk()

root.title("laboratorio 1 teleco 2")
root.geometry("900x450")
root.resizable(0, 0)

# Cargar y redimensionar la imagen usando tkinter
raw_image = PhotoImage(file="sen4.png")
resized_image = raw_image.subsample(4)  # Ajusta este valor según sea necesario

label_imagen = Label(root, image=resized_image, borderwidth=0)
label_imagen.place(x=500, y=70)

""""

raw_image2 = PhotoImage(file="flecha3.png")
resized_image2 = raw_image2.subsample(2)  # Ajusta este valor según sea necesario

label_imagen2 = Label(root, image=resized_image2, borderwidth=0)
label_imagen2.place(x=700, y=50)
"""


def diseño():
#--------------------------------LABELS---------------------------------------------------------------------
    root.resultado_binario = StringVar()
    
    root.label_titulo = Label(root, text = "CODIFICACION DE DIRECCIONES IP") # ese self es el frame
    root.label_titulo.config(font= ("Arial",30, "bold"))# el 12 indica el tamaño de la fuente,el bold es la negrita
    root.label_titulo.place(x=100, y=20)
    
    root.label_secOC = Label(root, text="SELECIONE UN OCTETO:")
    root.label_secOC.config(font=("Arial",12,"bold"))
    root.label_secOC.place(x=50, y=180)

    root.label_ip = Label(root, text="INGRESE UNA IP:")
    root.label_ip.config(font=("Arial",12,"bold"))
    root.label_ip.place(x=112, y=140)

    root.label_tipC = Label (root, text="ELIJA UN TIPO DE CODIFICACION:")
    root.label_tipC.config(font=("Arial",12,"bold"))
    root.label_tipC.place(x=120, y=270)

    root.label_resultadoBina =Label (root,text="SU NUMERO EN BINARIO ES:")
    root.label_resultadoBina.config(font=("Arial",12,"bold"))
    root.label_resultadoBina.place(x=50, y=220)

    root.label_resultadoBin = Label(root, textvariable=root.resultado_binario)
    root.label_resultadoBin.config(font=("Arial", 12, "bold"))
    root.label_resultadoBin.place(x=280, y=220)

    root.label_version = Label(root, text = "version 1.0.1") # ese self es el frame
    root.label_version.config(font= ("Arial",7, "bold"))# el 12 indica el tamaño de la fuente,el bold es la negrita
    root.label_version.place(x=830, y=430)

    root.label_contacto = Label(root, text = "CESAR SAAVEDRA, JEISON ¿AMADO?, NICOLAS GUEVARA,TEL: 3222215814") # ese self es el frame
    root.label_contacto.config(font= ("Arial",9, "bold"))# el 12 indica el tamaño de la fuente,el bold es la negrita
    root.label_contacto.place(x=30, y=430)

#------------------ ENTRYS--------------------------------------------------
    root.la_ip = StringVar()
    root.entry_ip = Entry(root,textvariable=root.la_ip)
    root.entry_ip.config(width= 3, font=("Arial",12))
    root.entry_ip.place(x=260, y=140)

    root.la_ip_dos = StringVar()
    root.entry_ip_dos = Entry(root,textvariable=root.la_ip_dos)
    root.entry_ip_dos.config(width= 3, font=("Arial",12))
    root.entry_ip_dos.place(x=310, y=140)

    root.la_ip_tres = StringVar()
    root.entry_ip_tres = Entry(root,textvariable=root.la_ip_tres)
    root.entry_ip_tres.config(width= 3, font=("Arial",12))
    root.entry_ip_tres.place(x=360, y=140)

    root.la_ip_cuatro = StringVar()
    root.entry_ip_cuatro = Entry(root,textvariable=root.la_ip_cuatro)
    root.entry_ip_cuatro.config(width= 3, font=("Arial",12))
    root.entry_ip_cuatro.place(x=410, y=140)

#--------------------Radio button---------------------------------------------------------
    root.opcion = IntVar()
    root.radio_button1 = Radiobutton(root, variable=root.opcion, value=1)
    root.radio_button1.config(cursor = "hand2")
    root.radio_button1.place(x=260, y=180)

    root.radio_button2 = Radiobutton(root, variable=root.opcion, value=2)
    root.radio_button2.config(cursor = "hand2")
    root.radio_button2.place(x=310, y=180)

    root.radio_button3 = Radiobutton(root, variable=root.opcion, value=3)
    root.radio_button3.config(cursor = "hand2")
    root.radio_button3.place(x=360, y=180)

    root.radio_button4 = Radiobutton(root, variable=root.opcion, value=4)
    root.radio_button4.config(cursor = "hand2")
    root.radio_button4.place(x=410, y=180)


    root.opcionCO = IntVar()
    root.radio_buttonCO1 = Radiobutton(root,text="NRZ", variable=root.opcionCO, value=1)
    root.radio_buttonCO1.config(cursor = "hand2")
    root.radio_buttonCO1.place(x=40, y=300)

    root.radio_buttonCO2 = Radiobutton(root,text="RZ", variable=root.opcionCO, value=2)
    root.radio_buttonCO2.config(cursor = "hand2")
    root.radio_buttonCO2.place(x=200, y=300)

    root.radio_buttonCO3 = Radiobutton(root,text="NRZI", variable=root.opcionCO, value=3)
    root.radio_buttonCO3.config(cursor = "hand2")
    root.radio_buttonCO3.place(x=330, y=300)


#----------------BOTONES-----------------------------------------------------------

    root.boton_nuevo = Button (root, text="NUEVO",command=habilitar_campo)
    root.boton_nuevo.config(width=15, font=("Arial",12,"bold") ,fg="white", bg="green",cursor = "hand2",activebackground="spring green")
    root.boton_nuevo.place(x=50, y=350)

    root.boton_calcular = Button (root, text="CALCULAR", command=calcular)
    root.boton_calcular.config(width=15, font=("Arial",12,"bold") ,fg="white", bg="orange",cursor = "hand2",activebackground="orange3")
    root.boton_calcular.place(x=300, y=350)
        
    
    root.boton_cancelar = Button (root, text="CANCELAR",command=desahibilitar_campo)
    root.boton_cancelar.config(width=15, font=("Arial",12,"bold") ,fg="white", bg="red",cursor = "hand2",activebackground="red4")
    root.boton_cancelar.place(x=550, y=350)

    root.mostrar =  Label(root, text = "CODIFICACION TELEFONIA 4G")

#---------------------------------------------------------------------------------------------

def habilitar_campo():
        root.la_ip.set("")#el set envia y va a poner los campos en blando
        root.la_ip_dos.set("")
        root.la_ip_tres.set("")
        root.la_ip_cuatro.set("")
        root.opcion.set("")
        root.opcionCO.set("")
        root.radio_button1.config(state="normal")
        root.radio_button2.config(state="normal") 
        root.radio_button3.config(state="normal")
        root.radio_button4.config(state="normal")  
        root.radio_buttonCO1.config(state="normal")
        root.radio_buttonCO2.config(state="normal") 
        root.radio_buttonCO3.config(state="normal")
        root.entry_ip.config(state="normal") # el state normal permite que se pueda editar y este habilitado el entry
        root.entry_ip_dos.config(state="normal")
        root.entry_ip_tres.config(state="normal")
        root.entry_ip_cuatro.config(state="normal")
        root.boton_calcular.config(state="normal")
        root.boton_cancelar.config(state="normal")

def desahibilitar_campo():
        root.la_ip.set("")#el set envia y va a poner los campos en blando
        root.la_ip_dos.set("")
        root.la_ip_tres.set("")
        root.la_ip_cuatro.set("")
        root.opcion.set("")
        root.opcionCO.set("")
        root.entry_ip.config(state="disabled") # el state normal permite que se pueda editar y este habilitado el entry
        root.entry_ip_dos.config(state="disabled")
        root.entry_ip_tres.config(state="disabled")
        root.entry_ip_cuatro.config(state="disabled")
        root.radio_button1.config(state="disabled")
        root.radio_button2.config(state="disabled") 
        root.radio_button3.config(state="disabled")
        root.radio_button4.config(state="disabled") 
        root.radio_buttonCO1.config(state="disabled")
        root.radio_buttonCO2.config(state="disabled") 
        root.radio_buttonCO3.config(state="disabled")
        root.boton_calcular.config(state="disabled")
        root.boton_cancelar.config(state="disabled")
   

def elegir():
    root.opcion_seleccionada = root.opcion.get()
    if root.opcion_seleccionada == 1:
        root.valor_ip = root.entry_ip.get()  # Corrected from entry_la_ip
    elif root.opcion_seleccionada == 2:
        root.valor_ip = root.entry_ip_dos.get()
    elif root.opcion_seleccionada == 3:
        root.valor_ip = root.entry_ip_tres.get()
    elif root.opcion_seleccionada == 4:
        root.valor_ip = root.entry_ip_cuatro.get()


    
def calcular():
    
    entero_a_bin()

    # Nuevo código para graficar la señal NRZ
    resultado_binario = root.resultado_binario.get()
    elegir_dos()
 
    # Convierte el resultado_binario a una lista de enteros
    


def entero_a_bin():
    elegir()
    # Asegúrate de definir root.resultado_binario antes de usarlo
    numero_decimal = int(root.valor_ip)  # Convierte a entero
    numero_binario = bin(numero_decimal)[2:]  # Convierte a binario y elimina el prefijo '0b'
    root.entry_ip_tres = Entry(root,textvariable=root.la_ip_tres)

def grafica_nrz(señal_binaria):
    tiempo = np.arange(0, len(señal_binaria), 1)
    señal = np.where(np.array(señal_binaria) == 0, -1, 1)

    # Ajusta el tamaño de la figura
    plt.figure(figsize=(len(señal_binaria), 4))

    # Personaliza las etiquetas del eje y
    y_labels = ['-v', '0', '+v']
    y_values = [-1, 0, 1]
    plt.yticks(y_values, y_labels)

    plt.step(tiempo, señal, where='post', color='b', linestyle='--', marker='o')
    plt.title('NRZ')
    plt.xlabel('Tiempo')
    plt.ylabel('Nivel de la Señal')

    plt.grid(True)
    plt.show()

def grafica_rz(señal_binaria_dos):
    time = np.arange(0, len(señal_binaria_dos) * 2, 1)
    signal = []

    for bit in señal_binaria_dos:
        if bit == 0:
            signal.extend([-1, 0])
        else:
            signal.extend([1, 0])

    # Ajusta el tamaño de la figura
    plt.figure(figsize=(len(señal_binaria_dos) * 2, 4))

    # Personaliza las etiquetas del eje y
    y_labels = ['-v', '0', '+v']
    y_values = [-1, 0, 1]
    plt.yticks(y_values, y_labels)

    plt.step(time, signal, where='post', color='b', linestyle='--', marker='o')
    plt.title('RZ')
    plt.xlabel('Tiempo')
    plt.ylabel('Nivel de la Señal')

    plt.grid(True)
    plt.show()

def señal_nrzi(señal_binaria_tres):
    time = np.arange(0, len(señal_binaria_tres) * 2, 1)
    signal = []
    

    polaridad = 1  
    
    for bit in señal_binaria_tres:
        # Agrega el nivel actual de polaridad al señal
        signal.append(polaridad)
        
        if bit == 0:
            # Cambia la polaridad instantáneamente en caso de un bit 0
            polaridad = -polaridad
        
    # Agrega el nivel de polaridad después del último cambio
    signal.append(polaridad)

    # Ajusta el tamaño de la figura
    plt.figure(figsize=(len(señal_binaria_tres) * 2, 4))

    # Personaliza las etiquetas del eje y para NRZI
    y_labels = ['-1', '0', '+1']  # ajustado para reflejar la nueva polaridad
    y_values = [-1, 0, 1]
    plt.yticks(y_values, y_labels)

    # Ajusta el tiempo para evitar el error
    time = np.arange(0, len(signal), 1)
    
    plt.step(time, signal, where='post', color='b', linestyle='--', marker='o')
    plt.title('NRZI')
    plt.xlabel('Tiempo')
    plt.ylabel('Nivel de la Señal')

    plt.grid(True)
    plt.show()


"""

def validar_entradas():
    try:
        ip1 = int(root.entry_ip.get())
        ip2 = int(root.entry_ip_dos.get())
        ip3 = int(root.entry_ip_tres.get())
        ip4 = int(root.entry_ip_cuatro.get())
    except ValueError:
        return False

    # Verifica que todas las entradas estén en el rango válido (0-255)
    if 0 <= ip1 <= 255 and 0 <= ip2 <= 255 and 0 <= ip3 <= 255 and 0 <= ip4 <= 255:
        return True
    else:
        return False
"""
def elegir_dos():
    resultado_binarioo = root.resultado_binario.get()
    root.opcion_dos = root.opcionCO.get()
    if root.opcion_dos == 1:
        señal_binaria = [int(bit) for bit in resultado_binarioo]
        grafica_nrz(señal_binaria)
    elif root.opcion_dos == 2:
        señal_binaria_dos = [int(bit) for bit in resultado_binarioo]
        grafica_rz(señal_binaria_dos)
    elif root.opcion_dos == 3:
        señal_binaria_tres = [int(bit) for bit in resultado_binarioo]
        señal_nrzi(señal_binaria_tres)




diseño()
desahibilitar_campo()



root.mainloop()