Implementación del Patrón Retry con Backoff Exponencial

Este repositorio contiene una demostración práctica del patrón de diseño de microservicios Retry with Exponential Backoff, implementado utilizando Python (Tenacity), Node.js y orquestado con Docker Compose.

1. Conceptos Teóricos

¿Qué es el patrón Retry?

Es un mecanismo de resiliencia que permite a un sistema recuperarse de fallos transitorios (errores temporales de red, sobrecarga momentánea o reinicio de servicios) reintentando una operación fallida automáticamente.


Características Principales

Detección de Transitoriedad: Solo actúa ante errores que tienen probabilidad de ser temporales (ej. HTTP 503, Timeouts).

Políticas de Abandono: Define un límite máximo de intentos para evitar el consumo infinito de recursos.

Aislamiento de Lógica: Separa la gestión de errores de la lógica de negocio.

Idempotencia: Crucial para asegurar que reintentar una operación no cause efectos secundarios duplicados (ej. evitar cobros dobles).


Tipos de Backoff
Fijo: Espera siempre el mismo intervalo entre intentos (ej. 2s, 2s, 2s).

Exponencial: Aumenta el tiempo de espera exponencialmente en cada fallo (ej. 2s, 4s, 8s, 16s). Es el estándar para evitar saturar servicios.

Con Jitter: Añade una variación aleatoria al tiempo exponencial para evitar que múltiples clientes reintenten exactamente al mismo tiempo (Thundering Herd Problem).


2. Tecnologías Utilizadas

Docker & Docker Compose: Para la orquestación de microservicios.

Python: Lenguaje del microservicio Cliente.

Tenacity: Librería de Python especializada en reintentos basada en decoradores.

Node.js & Express: Lenguaje del microservicio de Error (Servidor).


3. Estructura del Proyecto

Patron/
    cliente/
        -dockerfile
        -main.py
    Servicio/
        -Dockerfile
        -server.js
    Docker-compose
    
  

4. Instrucciones de Ejecución

Clonar el repositorio:

git clone 


Levantar los servicios:

docker-compose up --build


Observar el comportamiento:

Verás en la consola los intentos del cliente-retry.

Cuando el servicio responde con un 500 Internal Server Error, el cliente aplicará el Backoff Exponencial.

Notarás que el tiempo entre los mensajes [REINTENTO] aumenta progresivamente.
