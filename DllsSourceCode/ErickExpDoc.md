# Documentacion de ErickExp.dll

ErickExp.dll usa las siguientes especificaciones

* `DllIO.ReasonForCall` no se usa para nada
* ``DllIO.Params` debe ser un array de 2 elementos, el primero es el string a examinar y luego el examinador

## Sintaxis

ErickExp parsea caracter por caracter el string a examinar, tiene la siguiente sintaxis

* `[`***`]`:
    * `***` puede ser alguno de los siguientes patrones:
        * `Any`: cualquier caracter puede ser considerado sin discriminarlo
        * `X-Y`: comparar cualquier caracter entre el rango de X y Y
        * `C91`: escape para el corchete abierto
        * `C93`: escape para el corchete cerrado
    * no comprobado que pasa si la longitud de la sintaxis de `[`***`]` es exactamente 3 asi que si lo infringes digamos que, algo malo sucede, no se que, esta vez si no se que pasara
* `D`: Compara cualquier digito 0-9
* cualquier otro caracter sera comparado con ese mismo

## Ejemplos

### ejemplo de hora

Ejemplo1:
*    String: `23:59:59`
*   Examen: `[0-2]D:[0-5]D:[0-5]D`
*   Resultado: `True`
Ejemplo2:
*    String: `00:43:32`
*   Examen: `[0-2]D:[0-5]D:[0-5]D`
*   Resultado: `True`
Ejemplo3:
*    String: `31:65:72`
*   Examen: `[0-2]D:[0-5]D:[0-5]D`
*   Resultado: `False`

# retorna

* 1: si coincide con el formato
* 0: si no coincide con el formato