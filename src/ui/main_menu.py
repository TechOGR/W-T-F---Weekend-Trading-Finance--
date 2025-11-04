"""
Menú principal con opción de modo oscuro
"""

from PyQt5.QtWidgets import (QMenuBar, QMenu, QAction, QMessageBox, QFileDialog,
                             QApplication, QStyle)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QKeySequence
import os

class MainMenuBar(QMenuBar):
    """Menú principal de la aplicación"""
    
    # Señales
    save_triggered = pyqtSignal()
    load_triggered = pyqtSignal()
    load_from_db_triggered = pyqtSignal()
    set_capital_triggered = pyqtSignal()
    theme_changed = pyqtSignal(bool)  # True para modo oscuro
    show_daily_advice_triggered = pyqtSignal()
    show_weekly_summary_triggered = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dark_mode = False
        self.setup_menus()
    
    def setup_menus(self):
        """Configurar los menús"""
        # Menú Archivo
        file_menu = self.addMenu('📁 Archivo')
        
        # Acción Guardar
        save_action = QAction('💾 Guardar Semana', self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.setStatusTip('Guardar datos de la semana actual')
        save_action.triggered.connect(self.save_triggered.emit)
        file_menu.addAction(save_action)
        
        # Acción Cargar
        load_action = QAction('📂 Cargar Semana', self)
        load_action.setShortcut(QKeySequence.Open)
        load_action.setStatusTip('Cargar datos desde archivo')
        load_action.triggered.connect(self.load_triggered.emit)
        file_menu.addAction(load_action)
        
        # Acción Cargar desde BD
        load_db_action = QAction('🗄️ Cargar desde Base de Datos', self)
        load_db_action.setStatusTip('Cargar datos guardados en la base de datos')
        load_db_action.triggered.connect(self.load_from_db_triggered.emit)
        file_menu.addAction(load_db_action)
        
        file_menu.addSeparator()
        
        # Acción Establecer Capital Inicial
        set_capital_action = QAction('💰 Establecer Capital Inicial', self)
        set_capital_action.setStatusTip('Configurar el capital inicial de la semana')
        set_capital_action.triggered.connect(self.set_capital_triggered.emit)
        file_menu.addAction(set_capital_action)
        
        file_menu.addSeparator()
        
        # Acción Salir
        exit_action = QAction('🚪 Salir', self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.setStatusTip('Salir de la aplicación')
        exit_action.triggered.connect(self.parent().close)
        file_menu.addAction(exit_action)
        
        # Menú Vista
        view_menu = self.addMenu('👁️ Vista')
        
        # Acción Modo Oscuro
        self.dark_mode_action = QAction('🌙 Modo Oscuro', self)
        self.dark_mode_action.setCheckable(True)
        self.dark_mode_action.setStatusTip('Activar/desactivar modo oscuro')
        self.dark_mode_action.triggered.connect(self.toggle_dark_mode)
        view_menu.addAction(self.dark_mode_action)
        
        # Menú Asistente
        assistant_menu = self.addMenu('🧭 Asistente')
        daily_advice_action = QAction('📌 Mostrar consejo del día', self)
        daily_advice_action.setStatusTip('Ver recomendaciones según el día actual')
        daily_advice_action.triggered.connect(self.show_daily_advice_triggered.emit)
        assistant_menu.addAction(daily_advice_action)

        weekly_summary_action = QAction('🗓️ Resumen semanal', self)
        weekly_summary_action.setStatusTip('Mostrar resumen con sugerencia de retiro y reinversión')
        weekly_summary_action.triggered.connect(self.show_weekly_summary_triggered.emit)
        assistant_menu.addAction(weekly_summary_action)
        
        # Menú Ayuda
        help_menu = self.addMenu('❓ Ayuda')
        
        # Acción Acerca de
        about_action = QAction('ℹ️ Acerca de', self)
        about_action.setStatusTip('Información sobre la aplicación')
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        # Acción Instrucciones
        instructions_action = QAction('📖 Instrucciones', self)
        instructions_action.setStatusTip('Ver instrucciones de uso')
        instructions_action.triggered.connect(self.show_instructions)
        help_menu.addAction(instructions_action)
    
    def toggle_dark_mode(self, checked):
        """Cambiar entre modo claro y oscuro"""
        self.dark_mode = checked
        self.theme_changed.emit(checked)
        self.apply_theme_to_menu()
    
    def apply_theme_to_menu(self):
        """Aplicar tema al menú"""
        if self.dark_mode:
            # Estilo modo oscuro para el menú
            self.setStyleSheet("""
                QMenuBar {
                    background-color: #1e1e1e;
                    color: #e0e0e0;
                    padding: 5px;
                    border-bottom: 1px solid #2a2a2a;
                }
                
                QMenuBar::item {
                    background-color: transparent;
                    padding: 8px 15px;
                    margin: 2px;
                    border-radius: 4px;
                }
                
                QMenuBar::item:selected {
                    background-color: #2a2a2a;
                    color: #e0e0e0;
                }
                
                QMenuBar::item:pressed {
                    background-color: #3a3a3a;
                    color: #e0e0e0;
                }
                
                QMenu {
                    background-color: #1e1e1e;
                    color: #e0e0e0;
                    border: 1px solid #2a2a2a;
                    border-radius: 4px;
                    padding: 5px;
                }
                
                QMenu::item {
                    padding: 8px 20px;
                    margin: 2px;
                    border-radius: 3px;
                }
                
                QMenu::item:selected {
                    background-color: #2a2a2a;
                    color: #e0e0e0;
                }
                
                QMenu::separator {
                    height: 1px;
                    background-color: #2a2a2a;
                    margin: 5px 10px;
                }
            """)
        else:
            # Estilo modo claro para el menú
            self.setStyleSheet("""
                QMenuBar {
                    background-color: #f8f9fa;
                    color: #2c3e50;
                    padding: 5px;
                    border-bottom: 1px solid #dee2e6;
                }
                
                QMenuBar::item {
                    background-color: transparent;
                    padding: 8px 15px;
                    margin: 2px;
                    border-radius: 4px;
                }
                
                QMenuBar::item:selected {
                    background-color: #e9ecef;
                    color: #3498db;
                }
                
                QMenuBar::item:pressed {
                    background-color: #3498db;
                    color: white;
                }
                
                QMenu {
                    background-color: white;
                    color: #2c3e50;
                    border: 1px solid #dee2e6;
                    border-radius: 4px;
                    padding: 5px;
                }
                
                QMenu::item {
                    padding: 8px 20px;
                    margin: 2px;
                    border-radius: 3px;
                }
                
                QMenu::item:selected {
                    background-color: #3498db;
                    color: white;
                }
                
                QMenu::separator {
                    height: 1px;
                    background-color: #dee2e6;
                    margin: 5px 10px;
                }
            """)
    
    def show_about(self):
        """Mostrar diálogo Acerca de"""
        QMessageBox.about(self, "Acerca de W-T-F Trading Manager",
                         """
                         <h3>W-T-F (Weekend Trading Finance) Manager</h3>
                         <p><strong>Versión:</strong> 2.0</p>
                         <p><strong>Descripción:</strong></p>
                         <p>Aplicación para gestionar y analizar el rendimiento semanal de trading,
                         con análisis AI, persistencia de datos y visualizaciones mejoradas.</p>
                         <p><strong>Características:</strong></p>
                         <ul>
                             <li>✅ Gestión de datos semanales</li>
                             <li>✅ Análisis AI de rendimiento</li>
                             <li>✅ Persistencia en SQLite</li>
                             <li>✅ Visualizaciones interactivas</li>
                             <li>✅ Modo oscuro/claro</li>
                             <li>✅ Exportación de datos</li>
                         </ul>
                         <p><strong>Desarrollado con:</strong> Python, PyQt5, Matplotlib, SQLite</p>
                         """)
    
    def show_instructions(self):
        """Mostrar instrucciones de uso"""
        QMessageBox.information(self, "Instrucciones de Uso",
                             """
                             <h3>📖 Instrucciones de Uso</h3>
                             
                             <h4>📝 Ingreso de Datos:</h4>
                             <ul>
                                 <li>Haz clic en cualquier celda de la tabla</li>
                                 <li>Ingresa el monto del día</li>
                                 <li>Selecciona el destino (Retiro Personal o Reinversión)</li>
                                 <li>Los cambios se guardan automáticamente</li>
                             </ul>
                             
                             <h4>💾 Guardar y Cargar:</h4>
                             <ul>
                                 <li><strong>Guardar:</strong> Archivo → Guardar Semana (Ctrl+S)</li>
                                 <li><strong>Cargar:</strong> Archivo → Cargar Semana (Ctrl+O)</li>
                                 <li><strong>BD:</strong> Archivo → Cargar desde Base de Datos</li>
                                 <li><strong>Capital:</strong> Archivo → Establecer Capital Inicial</li>
                             </ul>
                             
                             <h4>🎨 Personalización:</h4>
                             <ul>
                                 <li>Vista → Modo Oscuro para cambiar el tema</li>
                                 <li>Los gráficos se actualizan automáticamente</li>
                                 <li>El análisis AI se genera con cada cambio</li>
                             </ul>
                             
                             <h4>📊 Análisis:</h4>
                             <ul>
                                 <li>Resumen semanal en el panel derecho</li>
                                 <li>Gráfico de barras con colores por tipo</li>
                                 <li>Análisis AI con recomendaciones</li>
                                 <li>Estadísticas de rendimiento</li>
                             </ul>
                             
                             <p><strong>💡 Consejo:</strong> Usa el análisis AI para mejorar tu estrategia de trading.</p>
                             """)