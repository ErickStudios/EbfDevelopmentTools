# libreria std para BasOS

# antes de llamar a cualquier funcion por favor hagan lo siguiente
# ```sh
# puenv
# src {fncs/funcion.sh}
# ```
# y poenv en el archivo de la funcion
# no hay subrutinas realmente xd

# normalmente aqui se guarda el program counter antes de una funcion
# asi esta definido el comando popc
rese 0
# parametro 1 para las funciones
# se encuentra en el stack principal
rese 1
# parametro 2 para las funciones
# se encuentra en el stack principal
rese 2
# parametro 3 para las funciones
# se encuentra en el stack principal
rese 3
# parametro 4 para las funciones
# se encuentra en el stack principal
rese 4
# parametro 5 para las funciones
# se encuentra en el stack principal
rese 5
# parametro 6 para las funciones
# se encuentra en el stack principal
rese 6
# parametro 7 para las funciones
# se encuentra en el stack principal
rese 7
# parametro 8 para las funciones
# se encuentra en el stack principal
rese 8
# parametro 9 para las funciones
# se encuentra en el stack principal
rese 9
# bandera que indica si se ha regresado para que el
# scriptiador no regrese a la instruccion 0 y en cambio
# ponga a la instruccion anterior y continue con su vida
rese 10
# la direccion a las lineas del script anterior en forma de array
# de strings
rese 11
# la direccion donde se guarda la direccion al string[] de las lineas
# del script anterior
rese 12
# la direccion donde se guarda la linea actual del script anterior
rese 13

puenv