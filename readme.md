![Logo](./EbfDevToolsLogo.png)

Bienvenido a EBFDevelopmentTools, "el kit de desarrollo por excelencia de ErickBinaryFormat"

Este kit de desarrollo contiene:
* libreria Std para ErickBinaryFormat (especificamente para su implementacion estandar de la arquitectura ErickBinaryFormat en KellyBootloader)
* pruebas y ejemplos de codigo
* codigo fuente de aplicaciones del bootloader
* librerias dinamicas .dll (no son para windows si no para ErickBinaryFormat)
* instalador de KellyBootloader

todo esto con fin para que los adolesentes y niños comprendan el bajo nivel de una manera simple, y intuitiva

# guia de ayuda

Puede ver la documentacion de uso de la libreria [aqui](./LibDoc.md)

tambien puedes ver la especificacion de librerias dinamicas [aqui](./DllSpecification.md) con fines de creacion de una o uso general

## Dependencias externas
como se menciono anteriormente este kit de desarrollo tiene tambien archivos .dll mas especificamente en la carpeta [lib/Dlls/](./lib/Dlls/), pero tranquilo el codigo fuente de cada una esta en [DllsSourceCode](./DllsSourceCode/)

las dependencias extermas se descargaran desde el instalador [install.py](./install.py) y puede decidir si descargarlas a su unidad o carpeta de almacenamiento de la maquina virtual, al decidir que si se descargaran a la carpeta `kelly/` (que es la carpeta estandar donde se guardan los .dll que usan los programas, si los pone en otra carpeta podria romper compatibilidad o otros programas) de su unidad o almacenamiento de la maquina virtual

# Libreria

EbfDevelopmentTools contiene una libreria std como se menciono anteriormente, esta libreria contiene 2 tipos de definiciones

| Tipo | Descripcion |
|---|---|
| Servicios de aranque  | Estas definiciones son solo validas antes del arranque de un sistema operativo hecho en ErickBinaryFormat, se encuentran solo en [lib/Misc/System.heasm](./lib/Misc/System.heasm) y se invalidan tan pronto como se salte a la funcion `_IExitBS_` |
| Servicios de ejecucion  | Estas definiciones y funciones funcionan dentro y fuera del arranque y se pueden usar en todos lados y incluso en tiempo de ejecucion del sistema |

Para descargar y usar la libreria puedes seguir los siguientes pasos
1. descargar la carpeta [lib](./lib/)
2. copiarla al directorio raiz de tu proyecto, si ya hay una combinalas
3. en su codigo incluya la instruccion 
    ```
    %include
        lib/ebf.heasm
    ```
    para usarla

la libreria incluye documentacion con un comentario en todas las funciones y variables

# compilando

descargue lo siguiente para desarrollar con ErickAssembly HEASM y la libreria

* ErickCompiler
    * esencial para compilar y trae el interprete de build.erc necesario para la rutina de compilacion
    * [Windows](https://www.mediafire.com/file/mvctx8p9heltlku/ErickCompilerWindows.zip/file)
    * [LinuxX64](https://www.mediafire.com/file/0mzfuh7ho7tuwbc/ErickCompilerLinuxX64.zip/file)
* ErickAssembly
    * la extension para el restaltado de ErickAssembly y HEASM, trae un bonus de resaltado para ErickCompiler
    * [ErickAssembly](https://marketplace.visualstudio.com/items?itemName=ErickCraftStudios.ErickAssembly)
* KellyBootloader
    * el cargador de arranque de ErickBinaryFormat
    * puede descargarlo usando el [install.py](./install.py) que descargara tanto la version de 64 bits como la de ia32 para UEFI

# codigo fuente

Los links al codigo fuente de las herramientas estan en esta seccion aqui abajo
* [ErickCompiler](https://github.com/ErickStudios/ErickCompiler)
* [ErickAssembly](https://github.com/ErickStudios/ErickAssembly)
* [KellyBootloader](https://github.com/ErickStudios/KellyBootloader)

# instalador

para instalar y/o actualizar KellyBootloader 
* necesita tener instalado requests en Linux puedes usar `python -m pip install requests` en windows usa `py -m pip install requests`
* descargar `install.py` para descargar el instalador (si no lo tienes, o si una version añade nuevos archivos .dll descargalo otra vez)
* mover el `install.py` a la unidad en la que vas a instalar KellyBootloader, esto no borrara nada, solo crea las carpetas del ejecutable y de las librerias, si usas qemu pon el `install.py` en tu carpeta que el emulador usa para montarla
* abrir el `install.py` en la carpeta o unidad y listo, el instalador ya te dira que hacer

el `install.py` lo puedes conseguir [aqui](./install.py) o en la raiz de este repositorio