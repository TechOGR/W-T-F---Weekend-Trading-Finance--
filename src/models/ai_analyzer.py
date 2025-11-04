"""
Analizador AI para interpretar resultados de trading
Proporciona análisis inteligente de patrones y recomendaciones
"""

import random
from typing import Dict, List

class AIAnalyzer:
    """Analizador AI para interpretar resultados de trading"""
    
    def __init__(self):
        self.insights = [
            "Tu rendimiento muestra una tendencia positiva consistente.",
            "Considera aumentar tu capital de trading gradualmente.",
            "Los días con pérdidas parecen estar bien controlados.",
            "Tu estrategia de reinversión está funcionando eficientemente.",
            "Podrías considerar diversificar tus operaciones.",
            "El patrón de ganancias sugiere buena gestión de riesgo.",
            "Tus días de reinversión muestran resultados prometedores.",
            "Considera establecer metas semanales más ambiciosas.",
            "Tu consistencia es clave para el crecimiento a largo plazo.",
            "Los días con ganancias altas indican buen timing de mercado."
        ]
        
        self.recommendations = [
            "Mantén tu estrategia actual - está funcionando bien.",
            "Considera aumentar tu tamaño de posición gradualmente.",
            "Asegúrate de mantener un diario de trading.",
            "Revisa y ajusta tu estrategia cada semana.",
            "No te confíes demasiado tras semanas ganadoras.",
            "Considera tomar descansos entre sesiones de trading.",
            "Mantén disciplina con tus reglas de entrada/salida.",
            "Aprende de los días con pérdidas para mejorar.",
            "Considera establecer stop-loss más estrictos.",
            "No inviertas más de lo que puedes permitirte perder."
        ]
    
    def analyze_weekly_performance(self, summary: Dict, daily_data: Dict) -> Dict:
        """Analizar el rendimiento semanal y proporcionar insights"""
        analysis = {
            'summary': '',
            'insights': [],
            'recommendations': [],
            'risk_assessment': '',
            'performance_rating': ''
        }
        
        # Generar resumen basado en el rendimiento
        total_weekly = summary['total_weekly']
        performance_percentage = summary['performance_percentage']
        positive_days = summary['positive_days']
        negative_days = summary['negative_days']
        
        # Análisis de rendimiento
        if total_weekly > 0:
            if performance_percentage > 20:
                analysis['summary'] = "🚀 ¡Excelente semana! Rendimiento superior al 20%."
                analysis['performance_rating'] = "A+"
            elif performance_percentage > 10:
                analysis['summary'] = "📈 Buena semana con rendimiento positivo sólido."
                analysis['performance_rating'] = "A"
            else:
                analysis['summary'] = "✅ Semana positiva con ganancias consistentes."
                analysis['performance_rating'] = "B+"
        elif total_weekly == 0:
            analysis['summary'] = "➖ Semana neutral sin ganancias ni pérdidas significativas."
            analysis['performance_rating'] = "C"
        else:
            if performance_percentage < -20:
                analysis['summary'] = "📉 Semana difícil con pérdidas significativas."
                analysis['performance_rating'] = "D"
            else:
                analysis['summary'] = "⚠️ Semana con pérdidas moderadas."
                analysis['performance_rating'] = "C-"
        
        # Análisis de consistencia
        if positive_days >= 4:
            analysis['insights'].append("Gran consistencia con 4+ días positivos.")
        elif positive_days >= 3:
            analysis['insights'].append("Buena consistencia con mayoría de días positivos.")
        elif negative_days >= 3:
            analysis['insights'].append("Varios días negativos - revisa tu estrategia.")
        
        # Análisis de patrones diarios
        if daily_data:
            wednesday_amount = daily_data.get('Miércoles', {}).get('amount', 0)
            if wednesday_amount > 0:
                analysis['insights'].append("Tus días de reinversión están generando resultados positivos.")
            elif wednesday_amount < 0:
                analysis['insights'].append("Considera revisar tu estrategia de reinversión.")
        
        # Agregar insights aleatorios relevantes
        analysis['insights'].extend(random.sample(self.insights, 2))
        
        # Generar recomendaciones basadas en el rendimiento
        if total_weekly < 0:
            analysis['recommendations'].append("Considera reducir el tamaño de tus operaciones temporalmente.")
            analysis['recommendations'].append("Revisa y ajusta tu estrategia antes de continuar.")
        else:
            analysis['recommendations'].extend(random.sample(self.recommendations, 2))
        
        # Evaluación de riesgo
        if performance_percentage > 30 or performance_percentage < -30:
            analysis['risk_assessment'] = "Alto riesgo detectado - considera ajustar tu gestión de riesgo."
        elif performance_percentage > 20 or performance_percentage < -20:
            analysis['risk_assessment'] = "Riesgo moderado - monitorea de cerca tus operaciones."
        else:
            analysis['risk_assessment'] = "Riesgo controlado - buena gestión de riesgo."
        
        return analysis