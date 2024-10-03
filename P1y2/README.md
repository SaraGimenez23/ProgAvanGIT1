## Preguntas y respuestas  a ChatGPT:

**Pregunta 1:** En este código, (ejercicio 1) ¿cuántos númenos coge en el *range(1, 6)*?<br>
**Respuesta:** La función range(1, 6) genera una secuencia de números desde el 1 hasta el 5, excluyendo el 6. Así que en total, el rango captura 5 números: 1, 2, 3, 4 y 5.<br><br>
**Pregunta 2:** En este código, (ejercicio 2) ¿qué significa *text = text.lower().strip()*?<br>
**Respuesta:** text.lower():convierte todo el texto en minúsculas. Es decir, transforma cada letra mayúscula de la cadena en su correspondiente letra minúscula.<br>
text.strip(): elimina los espacios en blanco (incluyendo tabulaciones o saltos de línea) al principio y al final de la cadena.<br><br>
**Pregunta 3:** En el ejercicio 5, ¿cuál es la función de *append()*? en *tasks.append(task)* <br>
**Respuesta:** La función append es un método de las listas en Python que agrega un nuevo elemento al final de la lista. En este caso, la lista tasks es la lista global que almacena las tareas pendientes, y el elemento que se está añadiendo es la variable task.<br>
La expresión tasks.append(task) inserta ese nuevo elemento al final de la lista.<br><br>
**Pregunta 4:** En la función *find_longest_and_shortest(strings)* del ejercicio 6, ¿qué hace el argumento *key=len*?<br>
**Respuesta:** El argumento key=len se utiliza para indicar cómo se debe comparar cada elemento de la lista strings al buscar el valor máximo o mínimo.<br>
max(strings, key=len): Busca la cadena más larga en la lista strings porque compara los elementos según su longitud, calculada por la función len().<br>
min(strings, key=len): Busca la cadena más corta en la lista strings, de manera similar, comparando la longitud de cada cadena.<br><br>
**Pregunta 5:** En el ejercicio 4, ¿para qué se utiliza la función *len()*?<br>
**Respuesta:** En el código de la función todos_unicos(numeros), la función len() se utiliza para calcular la longitud (es decir, el número de elementos) de la lista numeros y del conjunto set(numeros).<br><br>
**Pregunta 6:** En la función *def print_strings_starting_with_letter(strings, letter)* del ejercicio 6, ¿cuál es la función del *startswith*?<br>
**Respuesta:** Este es un método de cadena en Python. Se utiliza para comprobar si una cadena comienza con una subcadena específica (en este caso, un solo carácter).<br>
La sintaxis es: string.startswith(substring), donde substring es la cadena con la que deseas verificar el comienzo de string.<br><br>
**Pregunta 7:** En el código del main() del ejercicio 3, ¿qué hace la instrucción *input()*?<br>
**Respuesta:** La instrucción input() se utiliza para capturar la entrada del usuario, permitiéndole especificar un límite que guiará la lógica del programa al generar y analizar números primos. Sin input(), el programa no podría personalizar su comportamiento según la entrada del usuario.

