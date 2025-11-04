"""
Sistema de consejos diarios y resumen semanal.
"""

from datetime import datetime

def get_daily_advice(model):
    """Obtener consejo del día basado en el día actual y el rendimiento.
    Devuelve un dict con 'title' y 'message'.
    """
    today_idx = datetime.now().weekday()  # 0=Lunes ... 6=Domingo
    total = model.get_total_profit_loss()
    percentage = model.get_profit_loss_percentage()
    initial = model.initial_capital
    balance = model.get_current_balance()

    positive = total > 0

    day_names = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    day = day_names[today_idx]

    base = f"Capital: ${initial:.2f} | Balance: ${balance:.2f} | Resultado: ${total:.2f} ({percentage:.2f}%)"

    if today_idx == 0:  # Lunes
        msg = (
            "Arranca la semana con foco. Define objetivos realistas y planifica tus operaciones clave.\n"
            "• Revisa el capital inicial y riesgos.\n"
            "• Evita sobreoperar: calidad sobre cantidad.\n"
            f"• {('Buen inicio, mantén disciplina.' if positive else 'Si el inicio es flojo, sé selectivo y reduce tamaño.')}"
        )
        return {"title": f"Consejo del día - {day}", "message": f"{base}\n\n{msg}"}

    if today_idx == 1:  # Martes
        msg = (
            "Consolida momentum: busca confirmaciones, no persigas entradas tardías.\n"
            "• Ajusta stops a estructura real, no a números redondos.\n"
            f"• {('Protege ganancias y no las regales.' if positive else 'Minimiza pérdidas, espera setups A+.')}"
        )
        return {"title": f"Consejo del día - {day}", "message": f"{base}\n\n{msg}"}

    if today_idx == 2:  # Miércoles
        msg = (
            "Mitad de semana: evalúa progreso y corrige derivas.\n"
            "• Si vas bien, evita el exceso de confianza.\n"
            "• Si vas mal, simplifica y baja exposición."
        )
        return {"title": f"Consejo del día - {day}", "message": f"{base}\n\n{msg}"}

    if today_idx == 3:  # Jueves
        msg = (
            "Prepara el cierre semanal. Sé selectivo y evita forzar trades.\n"
            "• Prioriza setups con confluencias claras.\n"
            "• No persigas recuperaciones a última hora."
        )
        return {"title": f"Consejo del día - {day}", "message": f"{base}\n\n{msg}"}

    if today_idx == 4:  # Viernes
        msg = (
            "Cierra la semana con cabeza fría.\n"
            "• Evita arriesgar ganancias consolidadas.\n"
            "• Documenta aprendizajes clave para el sábado."
        )
        return {"title": f"Consejo del día - {day}", "message": f"{base}\n\n{msg}"}

    if today_idx == 5:  # Sábado
        withdraw = max(0.0, total) * 0.30
        reinvest = max(0.0, total) - withdraw
        msg = (
            "Día de promedio semanal y retiros.\n"
            f"• Resultado semanal: ${total:.2f}.\n"
            f"• Recomendación de retiro: ${withdraw:.2f} (30% de las ganancias).\n"
            f"• Recomendación de reinversión: ${reinvest:.2f}.\n"
            f"• {('¡Semana ganadora! Felicitaciones 👏' if positive else 'Semana en rojo: enfócate en revisar y ajustar 📘')}"
        )
        return {"title": f"Consejo del día - {day}", "message": f"{base}\n\n{msg}"}

    # Domingo
    msg = (
        "Descansa y prepara la estrategia de la próxima semana.\n"
        "• Revisa diarios y marcas clave.\n"
        "• Planifica escenarios y tus límites."
    )
    return {"title": f"Consejo del día - {day}", "message": f"{base}\n\n{msg}"}


def get_weekly_summary_message(model):
    """Construir mensaje de resumen semanal con sugerencia de retiro y reinversión."""
    total = model.get_total_profit_loss()
    percentage = model.get_profit_loss_percentage()
    initial = model.initial_capital
    balance = model.get_current_balance()
    withdraw = max(0.0, total) * 0.30
    reinvest = max(0.0, total) - withdraw

    if total >= 0:
        headline = "¡Semana de ganancias! 🎉"
    else:
        headline = "Semana desafiante 💡"

    message = (
        f"{headline}\n\n"
        f"Capital inicial: ${initial:.2f}\n"
        f"Balance actual: ${balance:.2f}\n"
        f"Resultado semanal: ${total:.2f} ({percentage:.2f}%)\n\n"
        f"Retiro recomendado (30%): ${withdraw:.2f}\n"
        f"Reinversión sugerida: ${reinvest:.2f}\n"
        "\nConsejo: documenta tus mejores y peores operaciones para aprender rápido."
    )
    return message