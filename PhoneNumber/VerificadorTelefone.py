import phonenumbers
from phonenumbers import geocoder


phone = input('Digite o telefone desejado no formato +55123456789: ')

phone_number = phonenumbers.parse(phone)

print('Este telefone pertence a {}.'.format(geocoder.description_for_number(phone_number, 'pt')))
