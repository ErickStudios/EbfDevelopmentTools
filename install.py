#
# install.py
#
# instalador de KellyBootloader
#

# os usado para la creacion de directorios y archivos
import os

# requests para enviar solicitudes
import requests

# for system things
import sys

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
# direccion del ejecutable uefi x64
#
bootx64_path = os.path.join(efi_boot_path, "bootx64.efi")

#
# bootia32_path
#
# direccion del ejecutable uefi ia32
#
bootia32_path = os.path.join(efi_boot_path, "bootia32.efi")

#
# kelly_path
#
# carpeta de configuracion y dependencias de kellybootloader
#
kelly_path = "Kelly"

#
# BootloaderUrlx64
#
# representa la url al ejecutable de x64
#
BootloaderUrlx64 = "https://github.com/ErickStudios/KellyBootloader/raw/refs/heads/main/image/efi/boot/bootx64.efi"

#
# BootloaderUrlia32
#
# representa la url al ejecutable de ia32
#
BootloaderUrlia32 = "https://github.com/ErickStudios/KellyBootloader/raw/refs/heads/main/image/efi/boot/bootia32.efi"

def waitkey():
    if os.name == 'nt':  # Windows
        import msvcrt
        return msvcrt.getch().decode('utf-8', errors='ignore')
    else:  # Unix-like (Linux/macOS)
        import tty
        import termios
		
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            tecla = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return tecla

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def MenuDefine(Title:str,Options: list[str]) -> str:
	OptionSel = 0
    
	key = ""

	while True:
		print(f"\033[37m\033[40m{Title}")
		clearscreen()
		print(f"\033[37m\033[40m{Title}")
		for index, value in enumerate(Options):
			colour = ""
			if index == OptionSel:
				colour = "\033[30m\033[47m"
				if key.lower() == "e":
					return value
			else:
				colour = "\033[37m\033[40m"

			print(f"{colour}{value}")

		print("W/S=move E=Select")

		key = waitkey()
		print(key)
          
		if key.lower() == "w":
			OptionSel = OptionSel - 1
		if key.lower() == "s":
			OptionSel = OptionSel + 1
     
#
# CreateDirs
#
# crea los directorios
# 
def CreateDirs(
):
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
) -> bool:
    
	# intentar encontrar el contenido del .efi
	response = requests.get(Url)

	# si se pudo
	if response.status_code == 200:
		# abrir el archivo
		if os.path.exists(File):
			with open(File, "rb") as f:
				if f.read() == response.content:
					return False

		with open(File, "wb") as f:
			# escribirlo
			f.write(response.content)

		# avisar de el exito
		print(f"{Url} Descargado correctamente")
		return True
	else:
		# no se pudo
		print(f"Error al descargar {Url}: {response.status_code}")
	return False

#
# DownloadEfi
#
# descarga el bootx64.efi
#
def DownloadEfi():
    DownloadFile(BootloaderUrlx64, bootx64_path)
    DownloadFile(BootloaderUrlia32, bootia32_path)

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

# iniciar la tienda
if False:
	while True:
		Option = MenuDefine("Bienvenido a la tienda de KellyBootloader puedes hacer lo siguiente",
		{
			"Descargar Apps",
			"Actualizar KellyBootloader", 
			"Salir"
		})
		
		if Option == "Actualizar KellyBootloader":
			DownloadEfi()
		if Option == "Salir":
			exit(0)

# preguntar si se quiere descargar las dependencias
print("Desea descargar las dependencias (S/Y)/N: ")
YesNo = input().strip().lower()

if YesNo in ["s", "y"]:
    DownloadDependences(
    )

print("gracias por usar KellyBootloader, para acutalizar el bootloader vuelve a ejecutar el instalador")