import random
import string


TamanhoSenha = int(input('Digite o tamanho da senha que deseja: '))

EstruturaSenha = string.ascii_letters + string.digits + 'ç!@#$%^&*.()'

rnd = random.SystemRandom()  # os.urandom

print(''.join(rnd.choice(EstruturaSenha) for i in range(TamanhoSenha)))
