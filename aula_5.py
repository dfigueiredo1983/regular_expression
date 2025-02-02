# Meta caracteres: ^ $ * + ? { } ( )
# ( ) grupos pega os elementos do grupo, segue a ordem dos elementos do grupo
# Ex: o grupo (abc) deve combinar exatamente com qualquer string que tenha essa
# mesma sequência de caracteres
# [] conjunto pega os elementos do conjunto
# o grupo [abc] deve combinar com qualquer string que tenha os caracteres 'a', 'b' o 'c'
# [a-z] range, pega elementos da letra 'a' até a letra 'z'
import re

texto = '''
<p>Frase 1</p><p>Frase 2</p><p>Frase 3</p><div>Frase 4</div><p>123</p>
'''

# print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))
# print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
# print()
# print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))
# print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1MAIS"\3"COISAS\4', texto))
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1\4', texto))

