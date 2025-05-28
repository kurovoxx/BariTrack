from Clases.Implementar_Grafico import Implementar_Grafico
from Sub.Grafico_Calorias import Grafico_Calorias
from util.colores import *
from matplotlib.figure import Figure


class Grafico_Peso(Grafico_Calorias):
    def obtener_datos(self, usuario):
        query = """SELECT fecha, peso FROM peso GROUP BY fecha ORDER BY strftime('%Y-%m-%d', substr(fecha, 7, 4) || '-' || substr(fecha, 4, 2) || '-' || substr(fecha, 1, 2))"""
        resultados = self._ejecutar_consulta(usuario, query)
        fecha = [fila[0] for fila in resultados]
        peso = [fila[1] for fila in resultados]
        return fecha, peso
    
    def crear_grafico(self, frame, datos):
        fecha, peso = datos
        fig = Figure(figsize=(8, 5), dpi=100, facecolor=gris)
        ax = fig.add_subplot(111)
        self._configurar_ejes(ax, 'Peso vs Tiempo', 'Peso')
        
        if len(peso) > 0:
            bars = ax.bar(fecha, peso, color=verde_alegre, edgecolor='black', linewidth=1.5)
            for bar in bars:
                bar.set_linewidth(1.5)
                bar.set_edgecolor('white')
                bar.set_linestyle((0, (5, 1)))
            ax.set_yticks(ax.get_yticks())
        else:
            self._mostrar_sin_datos(ax)
        
        self._configurar_ticks(ax, fecha)
        self._mostrar_canvas(fig, frame)