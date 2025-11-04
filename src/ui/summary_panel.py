"""
Panel de resumen para mostrar estadísticas y análisis AI
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QFrame, QTextEdit, QGroupBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class SummaryPanel(QWidget):
    """Panel de resumen mejorado para mostrar estadísticas y análisis"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        """Configurar la interfaz del panel"""
        layout = QVBoxLayout()
        
        # Título principal
        self.title_label = QLabel("📊 RESUMEN SEMANAL")
        self.title_label.setObjectName("summary_title")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            QLabel {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 10px;
            }
        """)
        layout.addWidget(self.title_label)
        
        # Frame para estadísticas
        self.stats_frame = QFrame()
        self.stats_frame.setFrameStyle(QFrame.StyledPanel)
        self.stats_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        
        stats_layout = QVBoxLayout()
        
        # Capital inicial
        self.initial_capital_label = QLabel("Capital Inicial: $100.00")
        self.initial_capital_label.setObjectName("initial_capital")
        self.initial_capital_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #34495e;")
        stats_layout.addWidget(self.initial_capital_label)
        
        # Balance actual
        self.current_balance_label = QLabel("Balance Actual: $100.00")
        self.current_balance_label.setObjectName("current_balance")
        self.current_balance_label.setStyleSheet("font-size: 14pt; font-weight: bold; color: #2c3e50;")
        stats_layout.addWidget(self.current_balance_label)
        
        # Ganancia/Pérdida total
        self.profit_loss_label = QLabel("Ganancia/Pérdida: $0.00 (0.00%)")
        self.profit_loss_label.setObjectName("profit_loss")
        self.profit_loss_label.setStyleSheet("font-size: 13pt; font-weight: bold; color: #2c3e50;")
        stats_layout.addWidget(self.profit_loss_label)
        
        # Layout para detalles
        details_layout = QHBoxLayout()
        
        # Columna de retiros
        self.withdrawal_group = QGroupBox("💰 Retiros Personales")
        withdrawal_layout = QVBoxLayout()
        self.withdrawal_label = QLabel("$0.00")
        self.withdrawal_label.setObjectName("positive")
        self.withdrawal_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #27ae60;")
        withdrawal_layout.addWidget(self.withdrawal_label)
        self.withdrawal_group.setLayout(withdrawal_layout)
        details_layout.addWidget(self.withdrawal_group)
        
        # Columna de total semanal
        self.total_group = QGroupBox("📊 Total Semanal")
        total_layout = QVBoxLayout()
        self.weekly_total_label = QLabel("$0.00")
        self.weekly_total_label.setObjectName("weekly_total")
        self.weekly_total_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #2c3e50;")
        total_layout.addWidget(self.weekly_total_label)
        self.total_group.setLayout(total_layout)
        details_layout.addWidget(self.total_group)
        
        # Columna de reinversión
        self.reinvestment_group = QGroupBox("🔄 Reinversión")
        reinvestment_layout = QVBoxLayout()
        self.reinvestment_label = QLabel("$0.00")
        self.reinvestment_label.setObjectName("positive")
        self.reinvestment_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #f39c12;")
        reinvestment_layout.addWidget(self.reinvestment_label)
        self.reinvestment_group.setLayout(reinvestment_layout)
        details_layout.addWidget(self.reinvestment_group)
        
        # Columna de rendimiento
        self.performance_group = QGroupBox("📈 Rendimiento")
        performance_layout = QVBoxLayout()
        self.performance_label = QLabel("0.00%")
        self.performance_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #3498db;")
        performance_layout.addWidget(self.performance_label)
        
        # Días positivos/negativos
        self.days_label = QLabel("Días: +0 / -0")
        self.days_label.setStyleSheet("font-size: 10pt; color: #7f8c8d;")
        performance_layout.addWidget(self.days_label)
        
        self.performance_group.setLayout(performance_layout)
        details_layout.addWidget(self.performance_group)
        
        stats_layout.addLayout(details_layout)
        self.stats_frame.setLayout(stats_layout)
        layout.addWidget(self.stats_frame)
        
        # Sección de consejo del día
        self.advice_group = QGroupBox("Consejo del día")
        advice_layout = QVBoxLayout()
        self.daily_advice_label = QLabel("")
        self.daily_advice_label.setWordWrap(True)
        self.daily_advice_label.setStyleSheet("font-size: 10pt; color: #2c3e50;")
        advice_layout.addWidget(self.daily_advice_label)
        self.advice_group.setLayout(advice_layout)
        layout.addWidget(self.advice_group)

        # Sección de análisis AI
        self.ai_group = QGroupBox("🤖 Análisis AI")
        ai_layout = QVBoxLayout()
        
        # Resumen del análisis
        self.ai_summary_label = QLabel("Esperando datos...")
        self.ai_summary_label.setWordWrap(True)
        self.ai_summary_label.setStyleSheet("""
            QLabel {
                background-color: #e8f4f8;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #bee5eb;
                font-weight: bold;
                color: #0c5460;
            }
        """)
        ai_layout.addWidget(self.ai_summary_label)
        
        # Detalles del análisis
        self.ai_details_text = QTextEdit()
        self.ai_details_text.setReadOnly(True)
        self.ai_details_text.setMaximumHeight(150)
        self.ai_details_text.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 5px;
                padding: 8px;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 9pt;
            }
        """)
        ai_layout.addWidget(self.ai_details_text)
        
        self.ai_group.setLayout(ai_layout)
        layout.addWidget(self.ai_group)
        
        # Panel de estado
        self.status_label = QLabel("✅ Listo")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #d4edda;
                color: #155724;
                padding: 5px;
                border-radius: 3px;
                border: 1px solid #c3e6cb;
                font-size: 9pt;
            }
        """)
        layout.addWidget(self.status_label)
        
        # Añadir espaciador
        layout.addStretch()
        
        self.setLayout(layout)
        self.is_dark = False
    
    def update_summary(self, summary_data: dict, ai_analysis: dict, capital_data: dict = None):
        """Actualizar el panel con nuevos datos"""
        # Actualizar información del capital
        if capital_data:
            initial_capital = capital_data.get('initial_capital', 100.0)
            current_balance = capital_data.get('current_balance', initial_capital)
            total_profit_loss = capital_data.get('total_profit_loss', 0)
            profit_loss_percentage = capital_data.get('profit_loss_percentage', 0)
            
            # Actualizar capital inicial
            self.initial_capital_label.setText(f"Capital Inicial: ${initial_capital:.2f}")
            
            # Actualizar balance actual
            self.current_balance_label.setText(f"Balance Actual: ${current_balance:.2f}")
            
            # Actualizar ganancia/pérdida total con color
            profit_text = f"Ganancia/Pérdida: ${total_profit_loss:.2f} ({profit_loss_percentage:.2f}%)"
            self.profit_loss_label.setText(profit_text)
            
            if total_profit_loss >= 0:
                self.profit_loss_label.setStyleSheet("font-size: 13pt; font-weight: bold; color: #27ae60;")
            else:
                self.profit_loss_label.setStyleSheet("font-size: 13pt; font-weight: bold; color: #e74c3c;")
        
        # Actualizar valores principales (total semanal tradicional)
        total = summary_data.get('total_weekly', 0)
        
        # Actualizar detalles
        withdrawal = summary_data.get('total_withdrawal', 0)
        reinvestment = summary_data.get('total_reinvestment', 0)
        performance = summary_data.get('performance_percentage', 0)
        positive_days = summary_data.get('positive_days', 0)
        negative_days = summary_data.get('negative_days', 0)
        
        self.withdrawal_label.setText(f"${withdrawal:.2f}")
        self.reinvestment_label.setText(f"${reinvestment:.2f}")
        self.weekly_total_label.setText(f"${total:.2f}")
        self.performance_label.setText(f"{performance:.2f}%")
        
        # Color del rendimiento
        if performance >= 0:
            self.performance_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #27ae60;")
        else:
            self.performance_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #e74c3c;")
        
        self.days_label.setText(f"Días: +{positive_days} / -{negative_days}")
        
        # Actualizar análisis AI
        if ai_analysis:
            self.ai_summary_label.setText(ai_analysis.get('summary', 'Sin análisis disponible'))
            
            # Construir texto detallado
            details_text = ""
            
            if 'insights' in ai_analysis:
                details_text += "🔍 INSIGHTS:\n"
                for insight in ai_analysis['insights']:
                    details_text += f"• {insight}\n"
                details_text += "\n"
            
            if 'recommendations' in ai_analysis:
                details_text += "💡 RECOMENDACIONES:\n"
                for rec in ai_analysis['recommendations']:
                    details_text += f"• {rec}\n"
                details_text += "\n"
            
            if 'risk_assessment' in ai_analysis:
                details_text += f"⚠️  EVALUACIÓN DE RIESGO:\n{ai_analysis['risk_assessment']}\n"
            
            if 'performance_rating' in ai_analysis:
                details_text += f"\n⭐ CALIFICACIÓN: {ai_analysis['performance_rating']}"
            
            self.ai_details_text.setPlainText(details_text)

    def update_daily_advice(self, advice: dict):
        """Actualizar el consejo del día en el panel."""
        if not advice:
            self.daily_advice_label.setText("")
            return
        title = advice.get('title', 'Consejo del día')
        message = advice.get('message', '')
        replaced = message.replace("\n", "<br>")
        html = f"<b>{title}</b><br><br>{replaced}"
        self.daily_advice_label.setText(html)
    
    def update_status(self, status: str):
        """Actualizar el estado"""
        self.status_label.setText(status)
        
        # Cambiar color según el estado
        if "Guardado" in status or "Listo" in status:
            if self.is_dark:
                self.status_label.setStyleSheet("""
                    QLabel {
                        background-color: #16331f;
                        color: #8fce9b;
                        padding: 5px;
                        border-radius: 3px;
                        border: 1px solid #1f4d2c;
                        font-size: 9pt;
                    }
                """)
            else:
                self.status_label.setStyleSheet("""
                    QLabel {
                        background-color: #d4edda;
                        color: #155724;
                        padding: 5px;
                        border-radius: 3px;
                        border: 1px solid #c3e6cb;
                        font-size: 9pt;
                    }
                """)
        elif "Error" in status:
            if self.is_dark:
                self.status_label.setStyleSheet("""
                    QLabel {
                        background-color: #3a1f20;
                        color: #f19999;
                        padding: 5px;
                        border-radius: 3px;
                        border: 1px solid #5a2b2d;
                        font-size: 9pt;
                    }
                """)
            else:
                self.status_label.setStyleSheet("""
                    QLabel {
                        background-color: #f8d7da;
                        color: #721c24;
                        padding: 5px;
                        border-radius: 3px;
                        border: 1px solid #f5c6cb;
                        font-size: 9pt;
                    }
                """)
        else:
            if self.is_dark:
                self.status_label.setStyleSheet("""
                    QLabel {
                        background-color: #3a2f1f;
                        color: #e2c97a;
                        padding: 5px;
                        border-radius: 3px;
                        border: 1px solid #5a4a2b;
                        font-size: 9pt;
                    }
                """)
            else:
                self.status_label.setStyleSheet("""
                    QLabel {
                        background-color: #fff3cd;
                        color: #856404;
                        padding: 5px;
                        border-radius: 3px;
                        border: 1px solid #ffeaa7;
                        font-size: 9pt;
                    }
                """)

    def set_theme(self, is_dark: bool):
        """Aplicar estilos específicos del panel según el tema."""
        self.is_dark = is_dark
        if is_dark:
            # Encabezado
            self.title_label.setStyleSheet(
                """
                QLabel {
                    background-color: #1e1e1e;
                    color: #e0e0e0;
                    padding: 10px;
                    border-radius: 5px;
                    margin-bottom: 10px;
                    border: 1px solid #2a2a2a;
                }
                """
            )
            # Marco y grupos
            self.stats_frame.setStyleSheet(
                """
                QFrame {
                    background-color: #1e1e1e;
                    border: 1px solid #2a2a2a;
                    border-radius: 5px;
                    padding: 10px;
                }
                """
            )
            for group in [self.withdrawal_group, self.total_group, self.reinvestment_group, self.performance_group, self.advice_group, self.ai_group]:
                group.setStyleSheet(
                    """
                    QGroupBox {
                        color: #e0e0e0;
                        border: 1px solid #2a2a2a;
                        border-radius: 5px;
                        margin-top: 6px;
                    }
                    QGroupBox::title {
                        subcontrol-origin: margin;
                        subcontrol-position: top left;
                        padding: 0 3px;
                        background-color: transparent;
                    }
                    """
                )
            # Etiquetas
            self.initial_capital_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #e0e0e0;")
            self.current_balance_label.setStyleSheet("font-size: 14pt; font-weight: bold; color: #e0e0e0;")
            # profit_loss_label se ajusta en update_summary según signo
            self.weekly_total_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #e0e0e0;")
            self.withdrawal_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #f5d76e;")
            self.reinvestment_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #e0e0e0;")
            self.performance_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #e0e0e0;")
            self.days_label.setStyleSheet("font-size: 10pt; color: #b0b0b0;")
            self.daily_advice_label.setStyleSheet("font-size: 10pt; color: #e0e0e0;")
            self.ai_summary_label.setStyleSheet(
                """
                QLabel {
                    background-color: #1e1e1e;
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid #2a2a2a;
                    font-weight: bold;
                    color: #e0e0e0;
                }
                """
            )
            self.ai_details_text.setStyleSheet(
                """
                QTextEdit {
                    background-color: #1e1e1e;
                    border: 1px solid #2a2a2a;
                    border-radius: 5px;
                    padding: 8px;
                    font-family: 'Consolas', 'Monaco', monospace;
                    font-size: 9pt;
                    color: #e0e0e0;
                }
                """
            )
        else:
            # Volver a estilos claros originales
            self.title_label.setStyleSheet(
                """
                QLabel {
                    background-color: #3498db;
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    margin-bottom: 10px;
                }
                """
            )
            self.stats_frame.setStyleSheet(
                """
                QFrame {
                    background-color: #f8f9fa;
                    border: 1px solid #dee2e6;
                    border-radius: 5px;
                    padding: 10px;
                }
                """
            )
            for group in [self.withdrawal_group, self.total_group, self.reinvestment_group, self.performance_group, self.advice_group, self.ai_group]:
                group.setStyleSheet("")
            self.initial_capital_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #34495e;")
            self.current_balance_label.setStyleSheet("font-size: 14pt; font-weight: bold; color: #2c3e50;")
            self.weekly_total_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #2c3e50;")
            self.withdrawal_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #27ae60;")
            self.reinvestment_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #f39c12;")
            self.performance_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #3498db;")
            self.days_label.setStyleSheet("font-size: 10pt; color: #7f8c8d;")
            self.daily_advice_label.setStyleSheet("font-size: 10pt; color: #2c3e50;")
            self.ai_summary_label.setStyleSheet(
                """
                QLabel {
                    background-color: #e8f4f8;
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid #bee5eb;
                    font-weight: bold;
                    color: #0c5460;
                }
                """
            )
            self.ai_details_text.setStyleSheet(
                """
                QTextEdit {
                    background-color: #f8f9fa;
                    border: 1px solid #dee2e6;
                    border-radius: 5px;
                    padding: 8px;
                    font-family: 'Consolas', 'Monaco', monospace;
                    font-size: 9pt;
                }
                """
            )