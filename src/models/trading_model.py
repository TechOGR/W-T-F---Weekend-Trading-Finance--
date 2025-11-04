"""
Modelo de datos para el Gestor de Trading Quotex
Contiene las clases principales para manejar los datos de trading
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional

class TradingDataModel:
    """Modelo de datos para los resultados de trading"""
    
    def __init__(self):
        self.days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        self.destinations = {
            'Lunes': 'Retiro Personal',
            'Martes': 'Retiro Personal', 
            'Miércoles': 'Reinversión',
            'Jueves': 'Retiro Personal',
            'Viernes': 'Retiro Personal'
        }
        self.data = {day: {'amount': 0.0, 'destination': self.destinations[day]} for day in self.days}
        self.week_start_date = datetime.now().date()
        
    def update_day(self, day: str, amount: float):
        """Actualizar el monto para un día específico"""
        if day in self.data:
            self.data[day]['amount'] = amount
            
    def get_weekly_summary(self) -> Dict:
        """Calcular el resumen semanal"""
        total_weekly = sum(self.data[day]['amount'] for day in self.days)
        total_withdrawal = sum(self.data[day]['amount'] for day in self.days 
                              if self.data[day]['destination'] == 'Retiro Personal')
        total_reinvestment = sum(self.data[day]['amount'] for day in self.days 
                               if self.data[day]['destination'] == 'Reinversión')
        
        # Calcular promedio diario
        daily_average = total_weekly / 5  # 5 días hábiles
        
        # Calcular porcentaje de cambio
        total_positive = sum(max(0, self.data[day]['amount']) for day in self.days)
        total_negative = sum(abs(min(0, self.data[day]['amount'])) for day in self.days)
        
        performance_percentage = 0
        if total_positive + total_negative > 0:
            performance_percentage = (total_positive - total_negative) / (total_positive + total_negative) * 100
        
        return {
            'total_weekly': total_weekly,
            'total_withdrawal': total_withdrawal,
            'total_reinvestment': total_reinvestment,
            'daily_average': daily_average,
            'performance_percentage': performance_percentage,
            'positive_days': sum(1 for day in self.days if self.data[day]['amount'] > 0),
            'negative_days': sum(1 for day in self.days if self.data[day]['amount'] < 0)
        }
    
    def to_dict(self) -> Dict:
        """Convertir a diccionario para guardar"""
        return {
            'week_start_date': self.week_start_date.isoformat(),
            'data': self.data
        }
    
    def from_dict(self, data: Dict):
        """Cargar desde diccionario"""
        if 'week_start_date' in data:
            self.week_start_date = datetime.fromisoformat(data['week_start_date']).date()
        if 'data' in data:
            self.data = data['data']