#!/usr/bin/env python3
"""
Script de inicio para W-T-F Trading Manager
Este script facilita la ejecución de la aplicación modular
"""

import sys
import os
import subprocess

def main():
    """Función principal para iniciar la aplicación"""
    
    print("🚀 Iniciando W-T-F Trading Manager...")
    print("📊 Gestor de Trading Semanal con Análisis AI")
    print("=" * 50)
    
    # Verificar que el archivo main.py existe
    if not os.path.exists('main.py'):
        print("❌ Error: No se encontró main.py")
        print("📍 Asegúrate de ejecutar este script desde el directorio correcto")
        return 1
    
    try:
        # Ejecutar la aplicación
        result = subprocess.run([sys.executable, 'main.py'])
        
        if result.returncode != 0:
            print(f"❌ La aplicación terminó con código de error: {result.returncode}")
            return result.returncode
            
    except KeyboardInterrupt:
        print("\n⏹️  Aplicación interrumpida por el usuario")
        return 0
    except Exception as e:
        print(f"❌ Error al ejecutar la aplicación: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())