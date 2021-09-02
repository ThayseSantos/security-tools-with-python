import ctypes


pasta = input('Digite o caminho do arquivo a ser ocultado: ')

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)
if retorno:
    print('Arquivo foi ocultado!')
else:
    print('Algo está errado...')
