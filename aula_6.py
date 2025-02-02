# Meta caracteres: ^ $
# ^ -> começa com 
# $ -> termina com 
# [^a-z] -> qualquer coisa que não seja de 'a' até 'z' - NEGAÇÃO

import re

cpf = 'a 147.852.963-12 a'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', '123.456.789-12 qualquer coisa'))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', '123.456.789-12 qualquer coisa'))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', '123.456.789-12'))

print(re.findall(r'[^0-9]', '123.456.789-12'))

