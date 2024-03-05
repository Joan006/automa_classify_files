# Organizador de Archivos Automático

Este script en Python organiza automáticamente los archivos en un directorio específico en categorías predefinidas según su extensión. Además, monitorea continuamente el directorio para clasificar nuevos archivos que se agregan.

## Uso

1. **Configuración del Directorio Principal:**
   - Modifica la variable `directory` al directorio que deseas monitorear.

2. **Configuración de Categorías:**
   - Define las categorías y extensiones en el diccionario `categories`.

3. **Ejecución:**
   - Ejecuta el script. Se crearán directorios iniciales para cada categoría en el directorio principal.

4. **Monitoreo Continuo:**
   - El script continuará monitoreando el directorio cada 5 segundos.
   - Los nuevos archivos se moverán automáticamente a sus respectivas categorías.

## Requisitos

- Python 3.x
- Sistema operativo compatible con la biblioteca `os`

## Configuración Adicional

- Puedes ajustar los tiempos de monitoreo cambiando el valor de `time.sleep(5)` a otro intervalo de tiempo.

## Contribuciones

Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un problema o enviar una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

