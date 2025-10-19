<!--
* LibDoc.md
*
* escrito para guias de uso de la libreria LibEbfDevelopmentTools
-->

# Aviso

ErickBinaryFormat fue creado como una herramienta educativa para enseñar arquitectura de sistemas y programación de bajo nivel de forma accesible. Aunque es un proyecto abierto, se solicita respetar su propósito original.

Por favor, evita usar ErickBinaryFormat para contenido inapropiado, ofensivo, político o culturalmente sensible. No está prohibido, pero recuerda que cualquier mal uso puede afectar la percepción del proyecto y recaer sobre sus creadores.

El equipo de ErickCraftStudios, les da las gracias y les desea suerte y reconocimiento en su proyecto :)

# Documentacion de EbfDevelopmentTools
Bienvenido a la documentacion de EbfDevelopmentTools

nos importa la facilidad de uso y la portabilidad de un compilar una vez, ejecutar donde sea y aparte sin sistema operativo

tambien nos importa nuestro objetivo, hacer el bajo nivel accesible a niños y adolecentes y intuitivo

aparte no queremos darte la tarea dificil de reinventar las funciones tu mismo y con el riesgo de que fallen, por eso existe esta libreria y asi todo el sufrimiendo de implementacion va para mi y no tendras que hacer nada, solo usarla

aqui te documentamos el uso de la libreria

# Linea de comandos

`ShellApi.heasm` es un modulo que permite obtener parametros de la shell con la que se llamo el programa

Funciones/tapots:
## GetParam
* obtener el numero de parametro
* parametros
    * `Number` el parametro a obtener , empieza con 0 como el primero
* retorna 
    * `Cout` el puntero al array

Notas: algunas veces al no llamar desde la shell puede que no pase nada al leer los parametros o puede que cause una excepcion y ErickBinaryFormat se cuelgue, asegurate de evitar casos como estos verificando punteros nulos

# Arrays

`Array.heasm` es un modulo que permite modificar arrays

Funciones/tapots:

## GetArrayLength
* obtiene la longitud de un array
* parametros
    * `Array` el array
* retorna 
    * `GetOn` la longitud extraida
## GetArrayItem
* obtiene el item de un array
* parametros
    * `PtrTo` el array
    * `Item` el item a obtener, se pasa una direccion como valor , no se permiten valores directos
* retorna 
    * `ReturnOn` el elemento extraido
## SetArrayItem
* cambia el valor de un item de un array
* parametros
    * `PtrTo` el array
    * `Item` el item a obtener, solo valores directos
    * `NewValue` el nuevo valor, no se permiten valores directos
## PtrSetArrayItem
* cambia el valor de un item (como una variable) de un array
* parametros
    * `PtrTo` el array
    * `Item` el item a obtener, no se permiten valores directos
    * `NewValue` el nuevo valor, no se permiten valores directos
## CoppyToArray
* copia el valor de un array a otro
* parametros
    * `PtrTo1` el array 1
    * `PtrTo2` el array 2
    * `Item1` el item a extraer del array 1, no se permiten valores literales
    * `Item2` el item al cual se le copiara el item del array 1 al del 2, solo se permiten valores directos
## BufferCmp
* una comparacion de buffer si if directo
* parametros
    * `Array1` el array 1
    * `Array2` el array 2
* retorna
    * `(LET*)256` 1 si son iguales y 0 si no lo son
## BufferNCmp
* una comparacion de buffer con longitud maxima si if directo
* parametros
    * `Array1` el array 1
    * `Array2` el array 2
    * `Len` la longitud a la que se termina la comparacion, solo valores literales
* retorna
    * `(LET*)256` 1 si son iguales y 0 si no lo son
## PtrLenBufferNCmp
* `BufferNCmp` pero la longitud es un valor de una variable
* parametros
    * `Array1` el array 1
    * `Array2` el array 2
        * `Len` la longitud a la que se termina la comparacion, no se permiten valores literales

# funciones que te facilitan la vida

`Helpers.heasm` es un modulo que proporciona funciones rapidas

Enums/macros:
* _EbfNullPtr_
## comparaciones avanzadas
* _ComparatorType_IfEqual_
* _ComparatorType_IfGreater_
* _ComparatorType_IfNotGreater_
* _ComparatorType_JumpsAnyWays_
## codigos de escaneo de teclas
* _SCAN_NULL_
* _SCAN_UP_
* _SCAN_DOWN_
* _SCAN_RIGHT_
* _SCAN_LEFT_
* _SCAN_HOME_
* _SCAN_END_
* _SCAN_INSERT_
* _SCAN_DELETE_
* _SCAN_PAGE_UP_
* _SCAN_PAGE_DOWN_
* _SCAN_F1_
* _SCAN_F2_
* _SCAN_F3_
* _SCAN_F4_
* _SCAN_F5_
* _SCAN_F6_
* _SCAN_F7_
* _SCAN_F8_
* _SCAN_F9_
* _SCAN_F10_
* _SCAN_F11_
* _SCAN_F12_
* _SCAN_ESC_
## colores de consola
* _ConsoleColor_black_
* _ConsoleColor_lightblack_
* _ConsoleColor_darkgray_
* _ConsoleColor_gray_
* _ConsoleColor_lightgray_
* _ConsoleColor_white_
* _ConsoleColor_darkred_
* _ConsoleColor_red_
* _ConsoleColor_brightred_
* _ConsoleColor_darkorange_
* _ConsoleColor_orange_
* _ConsoleColor_brightorange_
* _ConsoleColor_darkyellow_
* _ConsoleColor_yellow_
* _ConsoleColor_brightyellow_
* _ConsoleColor_darkgreen_
* _ConsoleColor_green_
* _ConsoleColor_brightgreen_
* _ConsoleColor_darkcyan_
* _ConsoleColor_cyan_
* _ConsoleColor_brightcyan_
* _ConsoleColor_darkteal_
* _ConsoleColor_teal_
* _ConsoleColor_brightteal_
* _ConsoleColor_darkblue_
* _ConsoleColor_blue_
* _ConsoleColor_brightblue_

Funciones/tapots:

solo se mencionaran las funciones que son basicas para no marear a los principiantes, tal vez no sepan que es OR , MASK y XOR, igualmente la documentacion esta en el archivo

## SetForegroundColor
* cambia el color del texto de la consola
* parametros
    * `Color` el color, no se permite valores literales
## SetBackgroundColor
* cambia el color del fondo de la consola
* parametros
    * `Color` el color, no se permite valores literales
## SetCursorPos
* cambia la posicion del cursor de la consola
* parametros
    * `X` la nueva posicion en X, solo valores literales
    * `Y` la nueva posicion en Y, solo valores literales
## WaitMicroseconds
* espera una cantidad de microsegudos
* parametros
    * `Ms` los microsegundos, solo valores literales
## WaitKeyAndRead
* espera a que se presione una tecla y lo lee
* retorna
    * `EfiKeyStructPtr` como la tecla (use registros temporales como 1 para evitar perdidas de datos en variables)
## GetTime
* obtiene la fecha y hora
* retorna
    * `EfiTimeStructPtr` la estructura en formato EfiTime
## PrintNumber
* imprime un numero en la consola
* parametros
    * `Number` el numero, no hay version de puntero asi que usa_CallOut 18 {PunteroATuNumero}`
## PrintHexNumber
* imprime un numero hexadecimal en la consola sin el `0x`
* parametros
    * `Number` el numero, no hay version de puntero asi que usa_CallOut 19 {PunteroATuNumero}`
## Atoi
* convierte un texto a numero
* parametros
    * `Str` el puntero al string
* retorna
    * `NumberCout` como salida
## Xtoi
* convierte un texto hexadecimal a numero
* parametros
    * `Str` el puntero al string
* retorna
    * `NumberCout` como salida
## _Shutdown_
* apaga la pc
* usa `call _Shutdown_` por que no es un tapot
## _Reset_
* reinicia la pc
* usa `call _Reset_` por que no es un tapot
## PrintPool
* imprimir un pool como string
* parametros
    * `Str` el puntero al string
## While
* hace algo mientras una variable es true (vease (LET)1)
* la funcion debe tener una instruction `__asm ret` y usa `FUNCTION` por que tapot es una macro y no una funcion a la que se puede llamar en tiempo de ejecucion
* parametros
    * `Var` la variable, no se permiten valores literales
    * `Function` la funcion, no se permite un puntero a la funcion
## DrawRectangle
* dibuja un rectangulo
* parametros
    * `PosX` la posicion en X (no se permiten valores literales)
    * `PosY` la posicion en Y (no se permiten valores literales)
    * `SizeX` el tamaño en X (no se permiten valores literales)
    * `SizeY` el tamaño en Y (no se permiten valores literales)
    * `Red` el valor del canal rojo (no se permiten valores literales)
    * `Green` el valor del canal verde (no se permiten valores literales)
    * `Blue` el valor del canal azul (no se permiten valores literales)
## SplitStr
* recuerda, tenga a mano una copia de respañdo del original por que no se liberara solo de la memoria y al perder la direccion del original nunca podra liberarlo y se acomularan en la memoria
* separa un string
* parametros
    * `StrToSplitPtr` el puntero al string a separar
    * `Splitter` el puntero al string separador
* retorna
    * `ReturnOn` como la direccion al nuevo array con las direcciones de las separaciones
## StrReplace
* recuerda, tenga a mano una copia de respañdo del original por que no se liberara solo de la memoria y al perder la direccion del original nunca podra liberarlo y se acomularan en la memoria
* remplaza un por otro
* parametros
    * `StrPtr` el puntero al string a renplazar
    * `OldStr` el puntero al string original
    * `NewStr` el puntero al string que remplazara a OldStr
* retorna
    * `ReturnOn` como la direccion al nuevo array con las direcciones de las separaciones
## CmpAndJump
* compara y salta
* parametros
    * `Value1` el operador 1 en una variable (no se aceptan valores literales)
    * `Value2` el operador 2 en una variable (no se aceptan valores literales)
    * `JumpIf` saltar si retorno especificamente un estado de ComparatorType (solo valores literales)
    * `JumpTo` la etiqueta a la que saltara (un function, no se aceptan tapots, no se aceptan punteros a funciones)
    * `SaveProgramCounter` 1 si se quiere guardar el puntero de instrucciones para usar ret para volver al mismo lugar y seguir, si es 0 no se guardara
## IfManual
* un if manual
* parametros
    * `JumpTo` la etiqueta a la que se saltara
    * `SaveProgramCounter` la posibilidad de hacer ret para continuar, 0 si no, 1 si se desea

# llamadas

`RamCode.heasm` es un modulo para ejecutar y manejar codigo en la ram

Funciones/tapots:
## ExecuteCodeFromRam
* ejecuta codigo en la ram
* parametros
    * `PtrToCode` el puntero al string que contiene el codigo
## SaveMeInRam
* guardar el codigo actual en la ram
* retorna
    * `SavePtrIn` el puntero al codigo guardado

# estructuras que facilitan todo

`Structs.heasm` es un modulo que proporciona varias estructuras

Swincs (Estructuras):

algunas no se mencionan por que ya hay tapots en ebfbegimmers.heasm que ya lo facilitan mas y aparte puede usar registros temporales mientras que las instancias no por que usan variables y ocupan espacio

## EfiKey
* retornado por la llamada 12
* estructura
    * `ScanCode` : el codigo de escaneo
    * `UnicodeChar` el caracter unicode
## EfiTime
* retornado por la llamada 13, espera no no lo digas
* estructura
    * `Second` : el segundo
    * `Minute` : el minuto
    * `Hour` : la hora
    * `Day` : el dia del mes
    * `Month` : el mes
    * `Year` : el año
## ArrayAllocationMethod
* pasado como argumento por la llamada 14
* estructura
    * `PtrTo` : donde retorna la direccion
    * `Size` : el tamaño
## ConsoleSize
* pasado como argumento y devuelto por la llamada 44
* estructura
    * `Colummns` : las columnas
    * `Rows` : las lineas

# librerias dinamicas

`Dll.heasm` es un modulo que contiene la definicion de una llamada a una dll

Swincs (Estructuras):
## DllParams
* parametros que necesita una dll para cargar su maximo esplendor
* estructura
    * `ReasonForCall` : la rason por la que se llamo, aqui no puedo establecer un standart por que cada dll tiene su propia manera de usar el ReasonForCall, tendras que leer la documentacion de la libreria que usaras si es que tiene :(
    * `Params` : el puntero a los parametros que necesita la dll
    * `ReturnValue` : lo pongo como let por que no se que retornara cada dll, si es un valor normal pues que bien, si es un array, pues como let y array se comportan internamente de la misma manera por que depende solo de como lo use el usuario, array solo es una convension de let para que sea mas entendible y comodo para la logica y la comprension del programador, si let tiene un valor literal funciona y si apunta a un array pues automaticamente `array [Index] NewValue` lo sabe y lo maneja bien, no te preocupes esta bien, si? 
## DllIO
instancia de `DllParams`

# manejo de archivos

`File.heasm` es un modulo para interactuar con el fs

Funciones/tapots:
## ExecuteFile
* ejecuta un archivo desde el fs
* parametros
    * `FileNamePool` el string que contiene el nombre y direccion del archivo
# WriteFile
* escribe un archivo en el fs
* parametros
    * `FileNamePool` el string que contiene el nombre y direccion del archivo
    * `FileContentPool` el string que contiene el contenido que se va a escribir
## LoadFileToMem
* cargar un archivo en la ram
* parametros
    * `FileNamePool` el nombre del archivo
* retorna
    * `FileNamePool` como el contenido

# optimizacion

`Optimization.heasm` es un modulo que permite optimizacion

Funciones/tapots:
## EditHighPartVar
* edita la parte alta de una variable
* parametros
    * `VarToEdit` la variable que edita
    * `NewValue` el nuevo valor, no se permiten valores literales
## EditLowPartVar
* edita la parte baja de una variable
* parametros
    * `VarToEdit` la variable que edita
    * `NewValue` el nuevo valor, no se permiten valores literales
## ReadHighPartVar
* lee la parte alta de una variable
* parametros
    * `VarToEdit` la variable que leera
* retorna
    * `ReturnOn` como resultado
## ReadLowPartVar
* lee la parte baja de una variable
* parametros
    * `VarToEdit` la variable que leera
* retorna
    * `ReturnOn` como resultado

# puertos PCi

`Pci.heasm` es un modulo que permite interactuar con puertos PCi, todo lo tecnico se esconde en el codigo fuente de las llamadas asi que solo necesitaras preocuparte por el tipo de dispositivo PCi al que quieres acceder y a que registro quieres acceder de ese puerto

Constantes/Enums:

## PciClass
* clases de PCis
* elementos
    * _PciClassDisplayCtrl_
    * _PciClassVga_
    * _PciClassBridge_
    * _PciClassIsa_
    * _PciClassIsaPositiveDecode_
    * _PciClassNetwork_
    * _PciClassEthernet_

Funciones/tapots:
## PciRead
* lee un valor de un puerto PCi
* parametros
    * `Pci` el puerto pci, solo se permiten el formato de direcciones de PCis de UEFI divididos en un array de 4 elementos
* retorna
    * `ReturnOn` el valor leido
## PciWrite
* escribe en un puerto PCI
* parametros
    * `Pci` el puerto pci, solo se permiten el formato de direcciones de PCis de UEFI divididos en un array de 4 elementos
    * `Data` el dato, no se permiten valores literales
## _IPciFindFirstChildOf
* encuentra una clase de PCI y la devuelve
* parametros
    * `Type` el tipo, no se permiten valores literales, y puedes guiarte de `PciClass`
    * `Register` el registro, no se permiten valores literales
* retorna
    * `ReturnOn` el puntero al array de 4 elementos que contiene la direccion completa del registro del PCi

# manejo

`ExtendedRam.heasm` es un modulo para acceder a la ram extendidad

## EditBlockValue
* edita un valor de un bloque
* parametros
    * `Blk` el bloque
    * `Offset` el offset
    * `Val` el nuevo valor, no se permiten valores literales
## GetBlockValue
* obtiene un valor de un bloque
* parametros
    * `Blk` el bloque
    * `Offset` el offset
* retorna
    * `Var` el valor