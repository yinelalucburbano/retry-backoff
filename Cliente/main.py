import requests
import time
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

URL = "http://servicio-error:3000/data"

def log_de_reintento(retry_state):
    """Función personalizada para que el log se vea bonito"""
    tiempo = retry_state.next_action.sleep
    intento = retry_state.attempt_number
    print(f"REINTENTO. Falló el intento #{intento}. Esperando {tiempo:.1f}s...")

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    before_sleep=log_de_reintento
)
def realizar_peticion():
    print(f"Enviando petición a {URL}...")
    response = requests.get(URL, timeout=3)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print("\nINICIANDO PRUEBA DE RESILIENCIA")
    time.sleep(2) 
    
    MAX_RONDAS = 8
    for i in range(1, MAX_RONDAS + 1):
        print(f"\nRONDA DE PRUEBA {i}/{MAX_RONDAS}")
        try:
            resultado = realizar_peticion()
            print(f"El servidor respondió: {resultado['message']}")
        except Exception:
            print(f"ERROR CRÍTICO: Se agotaron los reintentos en la ronda {i}.")
        
        print(f"Pausa antes de la siguiente ronda\n")
        time.sleep(5)

    print("\nPRUEBA FINALIZADA")