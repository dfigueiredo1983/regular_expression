# Meta caracteres: ^ $ * + ? { } ( )
# ( ) grupos pega os elementos do grupo, segue a ordem dos elementos do grupo
# [] conjunto pega os elementos do conjunto
# [a-z] range, pega elementos da letra 'a' até a letra 'z'
import re

texto = '''
<p>Frase 1</p><p>Frase 2</p><p>Frase 3</p><div>Frase 4</div><p></p>
'''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
print()
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))