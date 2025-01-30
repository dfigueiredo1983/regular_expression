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

texto = '''
<p>Frase 1</p><p>Frase 2</p><p>Frase 3</p><div>Frase 4</div><p></p>
'''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
print()
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))





