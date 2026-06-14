from datetime import datetime
import time
import os

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def reloj_en_tiempo_real():
    """Muestra un reloj actualizado en tiempo real"""
    try:
        while True:
            limpiar_pantalla()
            ahora = datetime.now()
            
            # Formato personalizado
            hora_formateada = ahora.strftime("""
╔════════════════════════════════════╗
║             RELOJ DIGITAL          ║
╠════════════════════════════════════╣
║  %H:%M:%S
║  %A, %d de %B de %Y
╚════════════════════════════════════╝
            """).strip()
            
            print(hora_formateada)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n¡Reloj detenido!")

if __name__ == "__main__":
    reloj_en_tiempo_real()