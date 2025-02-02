# Meta caracteres: ^ $ * + ? { } ( )
# * - 0 ou n vezes
# + 1 ou n vezes ou {1,}
# ? 0 ou 1 vez
# {n} n vezes
# {min, max} de vezes
# () grupo
# [] range
# {10,} repetir 10 ou mais vezes
# {,10} repetir até 10 vezes
# {10} deve repetir exatamente 10 vezes
# {5,10} repetir de 5 a até 10 vezes
# ()+ repedit o conjunto pelo menos 1 vez
# []+ repetir o range pelo menos 1 vez

import re
from pprint import pprint

texto = '''
<p>Frase 1</p><p>Frase 2</p><p>Frase 3</p><div>Frase 4</div><p>22</p>
'''

tags = re.findall(r'(<([pdiv]{1,3})>.+?<\/\2>)', texto)
list_tags = [um for um, dois in tags]

# print(list_tags)
# pprint(list_tags)

# print('Texto interno')

tags = re.findall(r'(<([pdiv]{1,3})>(.+?)<\/\2>)', texto)
# print(tags)
list_texto = [tres for um, dois, tres in tags]

# print(list_texto)
# pprint(list_texto)

# print('Removendo um retrovisor')

# tags = re.findall(r'<([pdiv]{1,3})>(?:.+?)<\/\1>', texto)
# print(tags)

cpf = '473.258.369-12'
print(cpf)
print(re.findall(r'[0-9]{3}', cpf))
print(re.findall(r'[0-9]{3}[-.]', cpf))
print(re.findall(r'[0-9]{3}\.', cpf))
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}', cpf))
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))

print('Usando retrovisores')
print(re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))


print(re.findall(r'\b(\d{3}\.\d{3}\.\d{3}-\d{2})\b', cpf))




