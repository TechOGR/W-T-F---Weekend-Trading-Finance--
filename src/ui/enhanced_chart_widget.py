"""
Widget de gráfico mejorado con mejor visualización
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
import numpy as np

class EnhancedChartWidget(QWidget):
    """Widget de gráfico mejorado con mejor visualización"""
    
    def __init__(self):
        super().__init__()
        self.is_dark = False
        self.setup_ui()
        
    def setup_ui(self):
        """Configurar la interfaz del gráfico"""
        layout = QVBoxLayout()
        
        # Crear figura y canvas
        self.figure = Figure(figsize=(12, 6), dpi=100, facecolor='white', edgecolor='none')
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        self.setLayout(layout)
        
        # Configurar estilo inicial
        self.setup_chart_style()
    
    def setup_chart_style(self):
        """Configurar el estilo del gráfico"""
        # Estilo profesional
        try:
            plt.style.use('seaborn-v0_8-whitegrid')
        except Exception:
            plt.style.use('seaborn')

        # Paleta de colores elegante
        self.colors = {
            'positive': '#2ecc71',      # Verde suave
            'negative': '#e74c3c',      # Rojo elegante
            'withdrawal': '#f1c40f',    # Dorado para retiros
            'reinvestment': '#8e44ad',  # Púrpura
            'neutral': '#bdc3c7',       # Gris
            'text': '#2c3e50',          # Texto oscuro
            'grid': '#ecf0f1',          # Grilla clara
            'avg_line': '#3498db'       # Línea de promedio
        }

        # Configurar fuentes
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']
        plt.rcParams['font.size'] = 10
    
    def update_chart(self, data_model):
        """Actualizar el gráfico con datos del modelo"""
        try:
            self.figure.clear()
            
            # Crear subplot principal
            ax = self.figure.add_subplot(111)
            
            # Obtener datos
            daily_data = []
            days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
            
            for i, day in enumerate(days):
                amount = data_model.daily_amounts.get(day, 0)
                destination = data_model.daily_destinations.get(day, '')
                daily_data.append({
                    'day': day[:3],  # Abreviar para mejor visualización
                    'amount': amount,
                    'destination': destination,
                    'is_positive': amount > 0,
                    'is_withdrawal': destination == 'Retiro Personal'
                })
            
            # Preparar datos para el gráfico
            x_positions = np.arange(len(daily_data))
            amounts = [d['amount'] for d in daily_data]
            
            # Determinar colores de las barras
            colors = []
            for data in daily_data:
                if data['amount'] < 0:
                    colors.append(self.colors['negative'])
                elif data['amount'] == 0:
                    colors.append(self.colors['neutral'])
                else:  # Es positivo
                    if data['is_withdrawal']:
                        colors.append(self.colors['positive'])
                    else:
                        colors.append(self.colors['withdrawal'])
            
            # Crear barras con mejor proporción
            bar_width = 0.6
            bars = ax.bar(x_positions, amounts, bar_width, color=colors, 
                         alpha=0.8, edgecolor='white', linewidth=1.5)
            
            # Configurar el gráfico
            ax.set_xlabel('Días de la Semana', fontsize=12, fontweight='bold', color=self.colors['text'])
            ax.set_ylabel('Monto ($)', fontsize=12, fontweight='bold', color=self.colors['text'])
            # Título sin emoji para evitar advertencias de fuente
            weekly_total = sum(amounts)
            ax.set_title('Rendimiento Semanal de Trading', fontsize=16, fontweight='bold', 
                        color=self.colors['text'], pad=16)
            
            # Configurar ejes
            ax.set_xticks(x_positions)
            ax.set_xticklabels([d['day'] for d in daily_data], fontsize=10, color=self.colors['text'])
            
            # Configurar grid
            ax.grid(True, axis='y', alpha=0.35, color=self.colors['grid'], linestyle='-', linewidth=0.8)
            ax.set_axisbelow(True)
            
            # Configurar línea base en cero
            ax.axhline(y=0, color=self.colors['text'], linewidth=1, alpha=0.5)
            
            # Añadir etiquetas de valores con mejor posicionamiento
            for i, (bar, data) in enumerate(zip(bars, daily_data)):
                height = bar.get_height()
                
                if height != 0:  # Solo mostrar etiquetas para barras con valor
                    # Determinar posición de la etiqueta
                    if height > 0:
                        y_pos = height + (max(amounts + [1]) * 0.02)  # margen por encima
                        va = 'bottom'
                    else:
                        y_pos = height - (max(abs(np.array(amounts)) + 1) * 0.02)  # margen por debajo
                        va = 'top'
                    
                    # Formatear el valor
                    value_text = f'${height:.0f}'
                    
                    # Añadir etiqueta
                    bbox_face = '#1e1e1e' if self.is_dark else 'white'
                    bbox_edge = '#2a2a2a' if self.is_dark else 'none'
                    ax.text(bar.get_x() + bar.get_width()/2., y_pos, value_text,
                           ha='center', va=va, fontsize=9, fontweight='bold',
                           color=self.colors['text'], 
                           bbox=dict(boxstyle='round,pad=0.3', facecolor=bbox_face, 
                                   alpha=0.85, edgecolor=bbox_edge))

            # Añadir línea de promedio semanal
            if amounts:
                avg = np.mean(amounts)
                ax.axhline(avg, color=self.colors['avg_line'], linestyle='--', linewidth=1.5, alpha=0.8)
                ax.text(0.99, 0.02, f'Promedio: ${avg:.2f}', transform=ax.transAxes,
                        ha='right', va='bottom', fontsize=9, color=self.colors['avg_line'],
                        bbox=dict(boxstyle='round,pad=0.25', facecolor='white', alpha=0.7, edgecolor='none'))
            
            # Ajustar límites del eje Y para dar espacio a las etiquetas
            y_min, y_max = ax.get_ylim()
            y_range = y_max - y_min
            
            if y_min < 0:
                ax.set_ylim(y_min - y_range * 0.1, y_max + y_range * 0.15)
            else:
                ax.set_ylim(y_min, y_max + y_range * 0.15)
            
            # Añadir leyenda mejorada
            legend_elements = [
                patches.Patch(color=self.colors['positive'], label='Ganancia'),
                patches.Patch(color=self.colors['negative'], label='Pérdida'),
                patches.Patch(color=self.colors['withdrawal'], label='Retiro Personal'),
                patches.Patch(color=self.colors['neutral'], label='Sin operar')
            ]
            
            ax.legend(handles=legend_elements, loc='upper right', 
                     frameon=True, fancybox=True, shadow=True, fontsize=9)

            # Subtítulo con total semanal
            ax.text(0.01, 1.02, f'Total semanal: ${weekly_total:.2f}', transform=ax.transAxes,
                    ha='left', va='bottom', fontsize=10, color=self.colors['text'])
            
            # Mejorar la apariencia general
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_color(self.colors['text'])
            ax.spines['bottom'].set_color(self.colors['text'])
            
            # Ajustar márgenes
            self.figure.tight_layout()
            
            # Actualizar canvas
            self.canvas.draw()
            
        except Exception as e:
            print(f"Error al actualizar el gráfico: {e}")
            self.show_error_message(str(e))
    
    def show_error_message(self, error_msg):
        """Mostrar mensaje de error en el gráfico"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        ax.text(0.5, 0.5, f'Error al cargar gráfico:\n{error_msg}', 
                ha='center', va='center', transform=ax.transAxes,
                fontsize=12, color='red', weight='bold')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        self.canvas.draw()
    
    def clear_chart(self):
        """Limpiar el gráfico"""
        self.figure.clear()
        self.canvas.draw()
    
    def set_theme(self, is_dark: bool):
        """Cambiar tema del gráfico"""
        self.is_dark = is_dark
        if is_dark:
            self.figure.patch.set_facecolor('#121212')
            plt.rcParams['text.color'] = '#e0e0e0'
            plt.rcParams['axes.facecolor'] = '#1e1e1e'
            plt.rcParams['axes.edgecolor'] = '#e0e0e0'
            plt.rcParams['axes.labelcolor'] = '#e0e0e0'
            plt.rcParams['xtick.color'] = '#e0e0e0'
            plt.rcParams['ytick.color'] = '#e0e0e0'
            plt.rcParams['grid.color'] = '#3a3a3a'
        else:
            self.figure.patch.set_facecolor('white')
            plt.rcParams['text.color'] = '#2c3e50'
            plt.rcParams['axes.facecolor'] = 'white'
            plt.rcParams['axes.edgecolor'] = '#2c3e50'
            plt.rcParams['axes.labelcolor'] = '#2c3e50'
            plt.rcParams['xtick.color'] = '#2c3e50'
            plt.rcParams['ytick.color'] = '#2c3e50'
            plt.rcParams['grid.color'] = '#ecf0f1'
        
        # Actualizar colores según tema
        if is_dark:
            self.colors['text'] = '#e0e0e0'
            self.colors['grid'] = '#3a3a3a'
        else:
            self.colors['text'] = '#2c3e50'
            self.colors['grid'] = '#ecf0f1'