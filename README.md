# Proyecto Automatización E2E - Urban Routes

## Descripción del Proyecto
Este repositorio contiene pruebas automatizadas para la aplicación web Urban Routes. El objetivo principal es verificar el correcto funcionamiento del flujo completo (End-to-End) para solicitar un vehículo, simulando interacciones reales de un usuario en el navegador mediante automatización de la interfaz.

**Flujo automatizado:**
* Configuración de la ruta de viaje (origen y destino).
* Selección de la tarifa de servicio "Comfort".
* Ingreso de número telefónico y confirmación mediante código SMS simulado.
* Vinculación de tarjeta de crédito como método de pago principal.
* Selección de artículos adicionales (mantas, pañuelos, helados) y envío de mensaje al conductor.
* Confirmación final y despliegue del modal de asignación de vehículo.

## Tecnologías y Patrones de Diseño
* **Python:** Lenguaje de programación principal de la suite.
* **Selenium WebDriver:** Interacción, control del DOM y aserciones.
* **Pytest:** Framework utilizado para la ejecución y estructuración de los tests.
* **Page Object Model (POM):** Implementado para separar la capa de localizadores de la lógica de negocio.
* **WebDriverWait:** Uso de esperas explícitas para asegurar la sincronización con la interfaz.

## Estructura del Proyecto

| Archivo | Descripción |
| :--- | :--- |
| `main.py` | Contiene la clase principal `UrbanRoutesPage` (localizadores y métodos) y la clase `TestUrbanRoutes` con los casos de prueba. |
| `data.py` | Almacena las variables de entorno, URLs y datos de prueba para mantener un enfoque escalable. |
| `helpers.py` | Incluye funciones auxiliares avanzadas, como la intercepción de red para capturar el código SMS del backend. |

## Instrucciones de Ejecución

**1. Instalar dependencias**
Abre la terminal en el directorio raíz del proyecto e instala los paquetes necesarios ejecutando el siguiente comando:
pip install pytest selenium

**2. Ejecutar las pruebas**
Para iniciar la suite de automatización, ingresa el siguiente comando en la terminal:
pytest main.py
