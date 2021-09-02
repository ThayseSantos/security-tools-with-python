import hashlib


txt = input('Digite o texto a ser convertido:')

menu = int(input('''### MENU - ESCOLHA O TIPO DE HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                R: '''))
if menu == 1:
    resultado = hashlib.md5(txt.encode('utf-8'))
    print('O hash MD5 é: ', resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(txt.encode('utf-8'))
    print('O hash SHA1 é: ', resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(txt.encode('utf-8'))
    print('O hash SHA256 é: ', resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha256(txt.encode('utf-8'))
    print('O hash SHA512 é: ', resultado.hexdigest())
