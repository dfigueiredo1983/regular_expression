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
João trouxe flores para sua amada namorandaem 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de João. Teve 5 filhos, todos adultos atualmente.
Maria, hoje a sua esposa, ainda fez aquele caf~e com pão de queijo nas tarde de 
domingo. Também né! Sabendo a boa mineira que é, nunca esquece seu famoso paõ de
queijo.
Não caso de ouvir a Maria: "Jooooooooooooãooooooooooooooooo, o café tá prontinho
aqui. Veeeeeeee"!
joão e maria são muitos felizes com a vida que eles tem atualmente.
'''

print(re.search(r'João|Maria', texto))
print(re.findall(r'João|Maria', texto))

print(re.findall(r'jo+ão+|maria', texto, flags=re.IGNORECASE))


