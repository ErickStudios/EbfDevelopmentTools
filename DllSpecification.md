# bienvenido a la documentacion de construccion de DLLS coerentes

Fuentes
    * [Documentacion de uso de la libreria](./LibDoc.md) para saber sobre el uso de la libreria

# teoria

en EBF (o por lo menos en la libreria estandart para KellyBootloader) las dlls tienen como parametro
* `DllIO.ReasonForCall` la rason para llamar
* `DllIO.Params` parametros adicionales
* `DllIO.ReturnValue` el valor de retorno

## Parametros
los parametros tienen que ser un array para que puedan pasar varios parametros
y tienen que usarse asi
* con herramientas de manipulacion de arrays debe extraer cualquier item que quiera de los parametros para usarlos, puede guardarlos en otra variable pero no los liberes si solo copias la direccion ya que liberarias el parametro original y puede causar erroes si aun se necesita
* si lo vas a liberar usa una copia que esa si se puede liberar

## rason de llamada
aqui no puedo establezer nada por que las librerias pueden usar el `DllIO.ReasonForCall` para diferentes cosas dependiendo de la dll asi que tendras que leer la documentacion de la dll para saber como usarlo

## valor de retorno
aqui tampoco puedo hacer nada, tendras que leer la documentacion de la libreria que uses