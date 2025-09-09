#
# install.py
#
# instalador de KellyBootloader
#

# os usado para la creacion de directorios y archivos
import os

# requests para enviar solicitudes
import requests

#
# YesNo
#
# representa la desicion
#
YesNo = ""

# 
# efi_boot_path
#
# carpeta de boot
#
efi_boot_path = os.path.join("efi", "boot")

#
# bootx64_path
#
# direccion del ejecutable uefi
#
bootx64_path = os.path.join(efi_boot_path, "bootx64.efi")

#
# kelly_path
#
# carpeta de configuracion y dependencias de kellybootloader
#
kelly_path = "Kelly"

#
# BootloaderUrl
#
# representa la url al ejecutable
#
BootloaderUrl = "https://github.com/ErickStudios/KellyBootloader/raw/refs/heads/main/image/efi/boot/bootx64.efi"

#
# CreateDirs
#
# crea los directorios
# 
def CreateDirs():
    # crear carpetas
    os.makedirs(efi_boot_path, exist_ok=True)
    os.makedirs(kelly_path, exist_ok=True)

# 
# DownloadFile
#
# descargar un archivo desde una url
#
def DownloadFile(
        Url: str,
        File: str
):
    
    # intentar encontrar el contenido del .efi
    response = requests.get(Url)

    # si se pudo
    if response.status_code == 200:
        # abrir el archivo
        with open(File, "wb") as f:
            # escribirlo
            f.write(response.content)

        # avisar de el exito
        print(f"{Url} Descargado correctamente")
    else:
        # no se pudo
        print(f"Error al descargar {Url}: {response.status_code}")

#
# DownloadEfi
#
# descarga el bootx64.efi
#
def DownloadEfi():
    # intentar encontrar el contenido del .efi
    response = requests.get(BootloaderUrl)

    # si se pudo
    if response.status_code == 200:
        # abrir el archivo
        with open(bootx64_path, "wb") as f:
            # escribirlo
            f.write(response.content)

        # avisar de el exito
        print(f"Descargado correctamente")
    else:
        # no se pudo
        print(f"Error al descargar: {response.status_code}")

#
# DownloadDependences
#
# descarga las dependencias
#
def DownloadDependences():

    # descargar ErickExp.dll
    DownloadFile(
        "https://raw.githubusercontent.com/ErickStudios/EbfDevelopmentTools/refs/heads/main/lib/Dlls/ErickExp.dll",
        os.path.join(kelly_path, "ErickExp.dll")
    )

#
# inicio de instalador
#

# crear directorios
print("Creando carpetas del bootloader")
CreateDirs()

# descargar el .efi
print("Descargando el ejecutable de kellybootloader...")
DownloadEfi()

# preguntar si se quiere descargar las dependencias
print("Desea descargar las dependencias (S/Y)/N: ")
YesNo = input().strip().lower()

if YesNo in ["s", "y"]:
    DownloadDependences(
    )

print("gracias por usar KellyBootloader, para acutalizar el bootloader vuelve a ejecutar el instalador")