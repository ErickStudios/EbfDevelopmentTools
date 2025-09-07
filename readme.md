# EbfDevelopmentTools

Bienvenido a EBFDevelopmentTools, esto contiene la libreria STD oficial de KellyBootloader para crear ciertos programas o bootloaders y tambien los sistemas operativos y programas pueden usar la libreria

puedes ver la [documentacion](./LibDoc.md) de uso de la libreria
tambien puedes ver la [especificacion de dlls](./DllSpecification.md) para crear una o saber como se manejan

no todo son librerias .heasm, tambien incluye codigo fuente de dlls

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