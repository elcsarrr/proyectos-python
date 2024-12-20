import mysql.connector
import tkinter as tk
from tkinter import ttk,messagebox
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width =300, height = 300) # width para ancho y height para altura

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)#La opción tearoff se establece en 0, lo que significa que no se permitirá arrancar ("tear off") submenús en este menú.
    barra_menu.add_cascade(label="inicio", menu = menu_inicio)


    menu_inicio.add_command(label="crear registro en BD")
    menu_inicio.add_command(label="eliminar registro en BD")
    menu_inicio.add_command(label="salir", command = root.destroy)

    barra_menu.add_cascade(label="consultas")
    barra_menu.add_cascade(label="configuracion")
    barra_menu.add_cascade(label="ayuda")
class Frame(tk.Frame):#clase
    def __init__(self, root = None):
        #se hace la conexion a la base de datos
        self.conexion = mysql.connector.connect(
            user='root',
            password='',
            host='127.0.0.1',
            database='peliculas'
        )
        self.cursor = self.conexion.cursor() # el término "cursor" se refiere a un objeto que permite a un programa de aplicación interactuar con una base de datos 
        #                                      y recorrer filas de datos de manera secuencial o mediante operaciones específicas.
        super().__init__(root ,width=850, height=600) # super() en Python se utiliza para llamar a métodos de la clase base (clase padre) en una clase hija que hereda de la clase base.
        self.root = root
        self.pack() # esto lo organiza todo para que quede como pegado
        self.id_pelicula = None #  self.id_pelicula se utiliza para realizar operaciones de edición o guardado basadas en la película seleccionada en la interfaz gráfica. 
        #                          Si es None, se trata de una nueva película; de lo contrario, ya existe y se debe editar.
        #self.config(bg="green")
        self.campos_pelicula()
        self.desabilitar_campo()
        self.diseñar_tabla()

    def campos_pelicula(self):
        #---------------------------------------------------- LABELS
        

        self.label_nombre = tk.Label(self, text = "Nombre: ") # ese self es el frame
        self.label_nombre.config(font= ("Arial",12, "bold"))# el 12 indica el tamaño de la fuente,el bold es la negrita
        self.label_nombre.place(x=10, y=20)

        self.label_duracion = tk.Label(self, text = "duracion: ")
        self.label_duracion.config(font= ("Arial",12, "bold"))
        self.label_duracion.place(x=10, y=50)
        
        self.label_genero = tk.Label(self, text = "genero: ")
        self.label_genero.config(font= ("Arial",12, "bold"))
        self.label_genero.place(x=10, y=80)

        #-------------------------------------------------- ENTRYS
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width= 50, font=("Arial",12))
        self.entry_nombre.place(x=110, y=20)

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self,textvariable=self.mi_duracion)
        self.entry_duracion.config(width= 50, font=("Arial",12))
        self.entry_duracion.place(x=110, y=50)
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self,textvariable=self.mi_genero)
        self.entry_genero.config(width= 50,  font=("Arial",12))
        self.entry_genero.place(x=110, y=80)

        #------------------------------------------------------ BOTONES
        self.boton_nuevo = tk.Button (self, text="Nuevo",command=self.habilitar_campo)
        self.boton_nuevo.config(width=15, font=("Arial",12,"bold") ,fg="white", bg="green",cursor = "hand2",activebackground="spring green")
        self.boton_nuevo.place(x=10, y=130)

        self.boton_guardar = tk.Button (self, text="Guardar",command=self.guardar_datos)
        self.boton_guardar.config(width=15, font=("Arial",12,"bold") ,fg="white", bg="orange",cursor = "hand2",activebackground="orange3")
        self.boton_guardar.place(x=200, y=130)
        
    
        self.boton_cancelar = tk.Button (self, text="Cancelar",command=self.desabilitar_campo)
        self.boton_cancelar.config(width=15, font=("Arial",12,"bold") ,fg="white", bg="red",cursor = "hand2",activebackground="red4")
        self.boton_cancelar.place(x=400, y=130)
        
    
    def habilitar_campo(self):
        self.mi_nombre.set("")#el set envia y va a poner los campos en blando
        self.mi_duracion.set("")
        self.mi_genero.set("")
        self.entry_nombre.config(state="normal") # el state normal permite que se pueda editar y este habilitado el entry
        self.entry_duracion.config(state="normal")
        self.entry_genero.config(state="normal")
        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")
    
    def desabilitar_campo(self):
        self.id_pelicula = None # 
        self.mi_nombre.set("")#el set envia
        self.mi_duracion.set("")
        self.mi_genero.set("")

        self.entry_nombre.config(state="disabled")# el state disabled permite que no se pueda editar y este deshabilitado el entry
        self.entry_duracion.config(state="disabled")
        self.entry_genero.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")
    def guardar_datos(self):
        if self.id_pelicula == None: # aca la condicion es para que se guarde normal cuando es la primera vez, si no es none se esta editando
            self.guardarT()
        else:
            self.editar(self.id_pelicula, self.mi_nombre.get(), self.mi_duracion.get(), self.mi_genero.get())# esto llama a una funcion que actualiza 
        self.desabilitar_campo()# no funciona nada
        self.diseñar_tabla()# se crea toda la tabla


    def diseñar_tabla(self):
        self.lista_peliculas = [] # se declara como una lista vacia
        sql = "SELECT * FROM pelicula"# se realiza una consulta SQL a una base de datos para obtener información sobre las películas. El resultado de esa consulta se almacena en self.lista_peliculas.
        self.cursor.execute(sql)# execute  se utiliza para ejecutar una consulta SQL en la base de datos asociada al cursor. para recuperar,insertar,actualizar y eliminar la base de datos
        self.lista_peliculas = self.cursor.fetchall() #recupera la informacion
        self.lista_peliculas.reverse() # invierte los elementos para que muestre de inicio a fin
        self.tabla = ttk.Treeview(self, columns= ("nombre", "Duracion", "Genero"))# muestra datos en forma de arbol
        self.tabla.place(x=10, y= 180, width=780, height=355)# width para ancho y height para altura
        # Calcula la altura de la barra de desplazamiento en función de la altura de la tabla
        scroll_height = int(355 * 0.75)  # 75% de la altura de la tabla para la barra, los 355 es la altura de la tabla
    

        self.scroll = ttk.Scrollbar(self, orient= "vertical", command = self.tabla.yview)
        self.scroll.place(x=790,y=200, height=scroll_height)
        self.tabla.configure(yscrollcommand = self.scroll.set)# a la tabla le envia la configuraciones del scroll

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="NOMBRE")
        self.tabla.heading("#2", text="DURACION")
        self.tabla.heading("#3", text="GENERO")

        for i in self.lista_peliculas:
            self.tabla.insert('',0, text=i[0], # '' representa el padre del elemento que se está insertando. En este caso, se está insertando en el nivel superior (raíz) de la tabla. y el 0 indica que inserte desde la posicion 1
            values= (i[1], i[2], i[3]))
    #botones editar
        self.boton_editar = tk.Button (self, text="Editar", command = self.editar_datos)
        self.boton_editar.config(width=15, font=("Arial",12,"bold") ,fg="white", bg="green",cursor = "hand2",activebackground="spring green")
        self.boton_editar.place(x=10, y=550)

    #botones eliminar
        self.boton_eliminar = tk.Button (self, text="Eliminar", command= self.eliminar_datos)
        self.boton_eliminar.config(width=15, font=("Arial",12,"bold") ,fg="white", bg="red",cursor = "hand2",activebackground="red4")
        self.boton_eliminar.place(x=180, y=550)

    def guardarT(self):

        generoo = self.mi_genero.get() # 
        nombree = self.mi_nombre.get()#self.mi_nombre = tk.StringVar() 
        duracioon = self.mi_duracion.get()
        self.cursor.execute("INSERT INTO pelicula (nombre,duracion,genero) VALUES ('{0}', '{1}', '{2}')".format(nombree,duracioon,generoo)) #el execute envia y recibe de la base de datos
        self.conexion.commit()#  se utiliza para confirmar (commit) las transacciones realizadas en la base de datos.
    def editar(self,id_pelicula, nombre, duracion, genero):
        sql = f"""UPDATE pelicula
        SET nombre  = '{nombre}', duracion = '{duracion}',
        genero ='{genero}'
        WHERE id_pelicula = {id_pelicula} """#actualiza
        self.cursor.execute(sql)
        self.conexion.commit()
    def editar_datos(self):
        try: # botar un error si el usuario hace algo que no debe hacer
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']# self.tabla.selection() devuelve la fila seleccionada y self.tabla.item() devuelve un diccionario con información sobre esa fila.
            #basicamente cuando uno preciona editar hace que aparezca lo antes escrito
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][3]
            self.habilitar_campo()
            self.entry_nombre.insert(0,self.nombre_pelicula)# el 0 indica desde que posicion se insertara los datos
            self.entry_duracion.insert(0,self.duracion_pelicula)
            self.entry_genero.insert(0,self.genero_pelicula)
        except:
            titulo = "Edicion de datos"
            mensaje = "no ha seleccionado ningun registro"
            messagebox.showerror(titulo,mensaje)
    def eliminar (self,id_pelicula):
        sql = f"DELETE FROM pelicula WHERE id_pelicula = {id_pelicula} "
        self.cursor.execute(sql)
        self.conexion.commit()
    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text'] #recupera el id de pelicula y es para selecionar
            self.eliminar(self.id_pelicula)# ejecuta el eliminar

            self.diseñar_tabla()
            self.id_pelicula = None
        except:
            titulo = "Edicion de datos"
            mensaje = "no ha seleccionado ningun registro"
            messagebox.showerror(titulo,mensaje)# para que salga una ventana con un error
"""
selecE=IntVar()
selecS=IntVar()
rdbDBM = Radiobutton(root,text="DBM",value=1,variable=selecE,bg="pink").place(x=75,y=320)
rdbWATTS = Radiobutton(root,text="WATTS",value=2,variable=selecE,bg="pink").place(x=75,y=340)


"""
