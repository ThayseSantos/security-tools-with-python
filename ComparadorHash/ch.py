import hashlib

arquivo1 = 'primeiro.txt'
arquivo2 = 'segundo.txt'

#ripemd160 = algoritmo de hash
hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

#comparação:
if hash1.digest() != hash2.digest():
    print('Hashs Diferentes:')
    print('Hash do primeiro arquivo: {} \nHash do segundo arquivo: {}'.format(hash1.hexdigest(), hash2.hexdigest()))
else:
    print('Hashs Iguais:')
    print('Hash do primeiro arquivo: {} \nHash do segundo arquivo: {}'.format(hash1.hexdigest(), hash2.hexdigest()))
