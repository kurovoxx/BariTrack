from Clases.Implementar_Grafico import Implementar_Grafico
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from util.colores import *

class Grafico_Calorias(Implementar_Grafico):
    def obtener_datos(self, usuario):
        query = """SELECT SUM(total_cal), fecha FROM consumo_diario GROUP BY fecha ORDER BY strftime('%Y-%m-%d', substr(fecha, 7, 4) || '-' || substr(fecha, 4, 2) || '-' || substr(fecha, 1, 2))"""
        resultados = self._ejecutar_consulta(usuario, query)
        cantidad = [fila[0] for fila in resultados]
        fecha = [fila[1] for fila in resultados]
        return fecha, cantidad
    
    def crear_grafico(self, frame, datos):
        fecha, cantidad = datos
        fig = Figure(figsize=(8, 5), dpi=100, facecolor=gris)
        ax = fig.add_subplot(111)
        self._configurar_ejes(ax, 'Calorías vs Tiempo', 'Calorías')
        
        if len(cantidad) > 0:
            bars = ax.bar(fecha, cantidad, color=verde_alegre, edgecolor='black', linewidth=1.5)
            for bar in bars:
                bar.set_linewidth(1.5)
                bar.set_edgecolor('white')
                bar.set_linestyle((0, (5, 1)))
            ax.set_yticks(ax.get_yticks())
        else:
            self._mostrar_sin_datos(ax)
        
        self._configurar_ticks(ax, fecha)
        self._mostrar_canvas(fig, frame)

    def _configurar_ejes(self, ax, titulo, ylabel):
        """Configuración común de ejes"""
        ax.set_facecolor("gray")
        ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.6, color='gray')
        ax.set_title(titulo, color='white', fontsize=12)
        ax.set_ylabel(ylabel, color='white', fontsize=10)
        ax.set_xlabel('Fecha', color='white', fontsize=10)

    def _mostrar_sin_datos(self, ax):
        """Muestra mensaje cuando no hay datos"""
        ax.text(0.5, 0.5, 'No hay datos disponibles', 
                horizontalalignment='center',
                verticalalignment='center', 
                transform=ax.transAxes, 
                color='white', fontsize=12)
        ax.set_yticks([])

    def _configurar_ticks(self, ax, fechas):
        """Configuración común de ticks"""
        ax.set_xticks(range(len(fechas)))
        ax.set_xticklabels(fechas, rotation=45, ha='right', fontsize=8, color='white')

    def _mostrar_canvas(self, fig, frame):
        """Muestra el canvas común"""
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.pack(fill='both', expand=True)