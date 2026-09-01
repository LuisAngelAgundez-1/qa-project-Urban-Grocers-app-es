# Proyecto Automatización - Urban Routes

## Descripción del Proyecto
Este proyecto contiene pruebas automatizadas para la aplicación web **Urban Routes**. El objetivo principal es verificar el correcto funcionamiento del flujo completo para pedir un taxi, simulando las interacciones reales de un usuario en el navegador.

El script de pruebas automatiza las siguientes acciones:
1. Configuración de la ruta (dirección de origen y destino).
2. Selección de la tarifa "Comfort".
3. Llenado del número de teléfono y confirmación mediante código SMS simulado.
4. Vinculación de una tarjeta de crédito como método de pago.
5. Inserción de un mensaje directo para el conductor.
6. Selección de artículos adicionales (manta, pañuelos y 2 helados).
7. Confirmación final para la búsqueda y asignación del taxi.

## Tecnologías y Técnicas Utilizadas
Para el desarrollo de este proyecto de automatización se implementaron las siguientes herramientas y patrones de diseño:
* **Python:** Lenguaje de programación principal.
* **Selenium WebDriver:** Herramienta utilizada para la interacción y control automatizado del navegador web.
* **Pytest:** Framework de pruebas utilizado para estructurar, ejecutar y validar los casos de prueba.
* **Page Object Model (POM):** Patrón de diseño implementado para separar los localizadores y métodos de interacción (`UrbanRoutesPage`) de la lógica de las pruebas (`TestUrbanRoutes`), facilitando el mantenimiento y la escalabilidad del código.
* **Esperas Explícitas (WebDriverWait):** Uso de esperas dinámicas para asegurar la sincronización correcta entre el código y las animaciones o tiempos de carga de la interfaz web.

## Instrucciones para ejecutar las pruebas

Sigue estos pasos para ejecutar el script de pruebas en tu entorno local:

1. **Requisitos previos:**
   Asegúrate de tener instalado Python en tu sistema, así como un IDE (como PyCharm o VSCode).

2. **Instalar dependencias:**
   Abre la terminal en el directorio raíz del proyecto e instala los paquetes necesarios (Selenium y Pytest) ejecutando:
   ```bash
   pip install pytest selenium
