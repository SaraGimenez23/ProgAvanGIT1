1. ¿Cuál es el propósito de la clase Time?
La clase Time representa una hora con soporte para formato AM/PM o de 24 horas, y permite establecer, validar y obtener una hora específica.

2. ¿Qué hace el método set_time?
El método set_time asigna una hora con horas, minutos, segundos y formato, validando que todos los valores sean correctos según el formato elegido.

3. ¿Cómo se valida el formato de hora en la clase Time?
El método __assign_format verifica si el formato es "AM", "PM" o "24 HOURS", y lo almacena en mayúsculas para evitar problemas con la capitalización.

4. ¿Qué hace la función from_string?
La función from_string crea un objeto Time a partir de una cadena de texto en formato "HH:MM
FORMAT", verificando que la cadena sea válida.

5. ¿Cómo maneja el programa las entradas inválidas del usuario?
Se implementa manejo de errores con try-except para capturar entradas no numéricas y verificaciones adicionales para asegurar que las horas, minutos y segundos sean válidos según el formato.

6. ¿Cómo se muestra la hora al usuario?
La función format_time_string devuelve la hora formateada en una cadena para ser visualizada, usando el formato adecuado (12 horas o 24 horas).

7. ¿Qué sucede si el usuario intenta introducir una hora con un formato incorrecto?
Si el formato es incorrecto, el método set_time devuelve False y se muestra un mensaje de error al usuario.
