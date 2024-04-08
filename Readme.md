# README 

### AUTOR

#### Gino Reginato

## Descripción 

Este código es una implementación en Python de una función para determinar si un número dado es primo o no.

>     Se define una función llamada is_primo que toma un argumento llamado value, que es el número que queremos verificar si es primo o no.
>     La primera condición verifica si el valor es menor o igual a 1. Si es así, devuelve False, ya que los números menores o iguales a 1 no son considerados primos.
>     La segunda condición verifica si el valor es igual a 2 o 3. Si es así, devuelve True, ya que 2 y 3 son números primos.
>     La tercera condición verifica si el valor es divisible por 2 o 3. Si es divisible por alguno de ellos, devuelve False, ya que ningún número divisible por 2 o 3 puede ser primo, excepto el propio 2 o 3.
>     Después de las condiciones anteriores, se inicia un bucle for que itera desde 2 hasta la raíz cuadrada de value más 1. Este rango es suficiente para verificar si value es divisible por algún otro número que no sea 1 o sí mismo.
>     Dentro del bucle, se verifica si value es divisible por i. Si lo es, significa que value no es un número primo y se imprime "no es" (esto parece ser un mensaje de depuración). Luego, la función devuelve False.
>     Si el bucle termina sin encontrar ningún divisor para value, significa que value es un número primo, por lo que la función devuelve True.

En resumen, este código define una función llamada is_primo que verifica si un número dado es primo o no, siguiendo los pasos estándar de determinación de números primos.