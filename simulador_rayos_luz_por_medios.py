import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox, StringVar, ttk

class SnellSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Rayo de Luz")
        
        # Variables
        self.indices_refraccion = []
        self.espesores = []
        self.angulo_incidencia = 0
        self.angulos_refraccion = []
        
        # Interfaz gráfica
        self.setup_ui()
        
    def setup_ui(self):
        # Estilo ttk
        self.style = ttk.Style()
        self.style.configure("TLabel", padding=5)
        self.style.configure("TEntry", padding=5)
        self.style.configure("TButton", padding=5)
        
        # Frame superior para la configuración
        top_frame = ttk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        ttk.Label(top_frame, text="Índices de refracción (separados por comas):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_indices_refraccion = ttk.Entry(top_frame)
        self.entry_indices_refraccion.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(top_frame, text="Espesores (separados por comas):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_espesores = ttk.Entry(top_frame)
        self.entry_espesores.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(top_frame, text="Ángulo de incidencia (grados):").grid(row=2, column=0, padx=5, pady=5)
        self.entry_angulo_incidencia = ttk.Entry(top_frame)
        self.entry_angulo_incidencia.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(top_frame, text="Calcular y Graficar", command=self.simular).grid(row=3, columnspan=2, pady=10)
        
        # Frame para el gráfico
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Frame para resultados
        result_frame = ttk.Frame(self.root)
        result_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        ttk.Label(result_frame, text="Resultados:").pack(anchor='w')
        self.text_resultado = tk.Text(result_frame, height=4, state='disabled')
        self.text_resultado.pack(fill=tk.X)

    def snell_law(self, n1, n2, theta1):
        theta1_rad = np.radians(theta1)
        sin_theta2 = (n1 / n2) * np.sin(theta1_rad)
        
        if sin_theta2 < -1 or sin_theta2 > 1:
            raise ValueError("Hay reflexión total del rayo de luz")
        
        theta2_rad = np.arcsin(sin_theta2)
        return np.degrees(theta2_rad)
    
    def calcular_trayectoria(self):
        angulos_refraccion = [self.angulo_incidencia]
        distancias = [0]
        
        x_actual = 0
        angulo_actual = self.angulo_incidencia

        for i in range(len(self.indices_refraccion) - 1):
            n1 = self.indices_refraccion[i]
            n2 = self.indices_refraccion[i + 1]
            espesor = self.espesores[i]

            angulo_refraccion = self.snell_law(n1, n2, angulo_actual)
            angulos_refraccion.append(angulo_refraccion)

            distancia = espesor / np.cos(np.radians(angulo_refraccion))
            x_actual += distancia
            distancias.append(x_actual)
            
            angulo_actual = angulo_refraccion
            
        return distancias, angulos_refraccion
    
    def graficar_trayectoria(self, distancias, angulos_refraccion):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Convertir ángulos a radianes
        angulos_refraccion_rad = np.radians(angulos_refraccion)
        
        # Convertir ángulos y magnitudes a coordenadas cartesianas
        x = distancias * np.cos(angulos_refraccion_rad)
        y = distancias * np.sin(angulos_refraccion_rad)

        colores = plt.cm.viridis(np.linspace(0, 1, len(x)))

        for i in range(1, len(x)):
            ax.axvline(x=x[i], color='gray', linestyle='--')
            
        for i in range(len(x) - 1):
            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], '-o', color=colores[i], label=f'Trayectoria en medio {i+1}')
        
        # Líneas de referencia en x y y
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Trayectoria del rayo de luz en diferentes medios')
        ax.grid(True)
        ax.legend()
        
        self.canvas.draw()

    def mostrar_resultados(self, angulos_refraccion, distancias):
        self.text_resultado.config(state='normal')
        self.text_resultado.delete(1.0, tk.END)
        self.text_resultado.insert(tk.END, f"Ángulos de refracción: {angulos_refraccion}\n")
        self.text_resultado.insert(tk.END, f"Distancias: {distancias}")
        self.text_resultado.config(state='disabled')
    
    def simular(self):
        try:
            self.indices_refraccion = list(map(float, self.entry_indices_refraccion.get().split(',')))
            self.espesores = list(map(float, self.entry_espesores.get().split(',')))
            self.angulo_incidencia = float(self.entry_angulo_incidencia.get())
            
            if len(self.indices_refraccion) != len(self.espesores) + 1:
                messagebox.showerror("Error", "La cantidad de índices de refracción debe ser igual a la cantidad de espesores + 1.")
                return
            
            distancias, angulos_refraccion = self.calcular_trayectoria()
            
            self.graficar_trayectoria(distancias, angulos_refraccion)
            
            self.mostrar_resultados(angulos_refraccion, distancias)
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

root = tk.Tk()
app = SnellSimulator(root)
root.mainloop()
