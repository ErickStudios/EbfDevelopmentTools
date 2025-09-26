# EbfDevelopmentTools

Bienvenido a EBFDevelopmentTools, esto contiene la libreria STD oficial de KellyBootloader para crear ciertos programas o bootloaders y tambien los sistemas operativos y programas pueden usar la libreria

puedes ver la [documentacion](./LibDoc.md) de uso de la libreria
tambien puedes ver la [especificacion de dlls](./DllSpecification.md) para crear una o saber como se manejan

no todo son librerias .heasm, tambien incluye codigo fuente de dlls, 

## Dependencias externas
* para las dependencias externas cuando pruebe su proyecto para usar las dlls, puede encontrarlas en la carpeta `lib/Dlls/` y copiarlas o descargarlas a su unidad de almacenamiento donde este instalado KellyBootloader y donde pruebas tu programa 
* asegurate de que tu programa este en la misma unidad de almacenamiento que el bootx64.efi de KellyBootloader ponga su programa en la carpeta root
* pongalas en la carpeta `kelly` de la unidad de almacenamiento donde pruebe su proyecto compilado, asegurate de no romper las dependencias de otros programas, asi que use siempre las .dll en la carpeta `kelly` en su almacenamiento donde tenga KellyBootloader instalado para poder ejecutar su programa o su sistema y pueda vincular el programa a la dll cargando el archivo desde el codigo de su programa

# Libreria

EbfDevelopmentTools contiene su propia libreria STD oficial para KellyBootloader que proporciona funciones que se pueden usar en todas partes y tambien funciones que pertenecen a la etapa de arranque de un sistema operativo, es el caso de la tabla de informacion del firmware que al salir de los servicios de arranque de EBF se libera toda esa informacion por que ya no la necesitas

puedes descargar la libreria solamente siguiendo estos pasos
1. asegurate de descargar la carpeta lib, si ya tienes una copia los archivos de la libreria ebf a la carpeta lib existente 
2. una vez ya tengas los archivos alli no muevas las librerias a otra carpeta debido a que el preprocesado de HEASM solo permite rutas absolutas dentro del proyecto, en el archivo `ebf.heasm` contiene varios inclusiones a `lib/ebfx.heasm`, esto indica que si o si deben estar dentro de la carpeta
3. en tu proyecto include `lib/ebf.heasm` para usar la libreria

puedes ver lo que hace cada funcion en la [documentacion](./LibDoc.md) de uso de la libreria

# Pruebas

este proyecto viene con pruebas de uso de la libreria y de heasm en general, puedes guiarte de estas pruebas para hacer tus proyectos

# sabias que

aqui tambien se prueban dlls y librerias que el propio KellyBootloader usa, puedes verlos en `DllsSourceCode/` aunque algunas tal vez nunca lleguen a KellyBootloader

tambien puede ver en `DefaultApps/` algunas aplicaciones que podran descargarse para KellyBootloader y con uso en la terminal, como herramientas de diagnostico, algunas apps utiles y mucho mas

# compilando

descargue lo siguiente para desarrollar con ErickAssembly HEASM y la libreria

* ErickCompiler
    * esencial para compilar y trae el interprete de build.erc necesario para la rutina de compilacion
    * [Windows](https://www.mediafire.com/file/mvctx8p9heltlku/ErickCompilerWindows.zip/file)
    * [LinuxX64](https://www.mediafire.com/file/0mzfuh7ho7tuwbc/ErickCompilerLinuxX64.zip/file)
* ErickAssembly
    * la extension para el restaltado de ErickAssembly y HEASM, trae un bonus de resaltado para ErickCompiler
    * [ErickAssembly](https://marketplace.visualstudio.com/items?itemName=ErickCraftStudios.ErickAssembly)

y tambien lo que ya dije sobre descargar la libreria

para instalar y/o actualizar KellyBootloader 
* necesita tener instalado requests en Linux puedes usar `python -m pip install requests` en windows usa `py -m pip install requests`
* descargar `install.py` para descargar el instalador (si no lo tienes, o si una version añade nuevas dlls descargalo otra vez)
* mover el `install.py` a la unidad en la que vas a instalar KellyBootloader, esto no borrara nada, solo crea las carpetas del ejecutable y de las librerias, si usas qemu pon el `install.py` en tu carpeta que el emulador usa para montarla
* abrir el `install.py` en la carpeta o unidad y listo, el instalador ya te dira que hacer

el `install.py` lo puedes conseguir [aqui](./install.py) o en la raiz de este repositorio