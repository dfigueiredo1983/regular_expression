# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

# \d  Matches any decimal digit; this is equivalent to the class [0-9].
# \D  Matches any non-digit character; this is equivalent to the class [^0-9].
# \s  Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
# \S  Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
# \w  Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
# \W  Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

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

print(re.findall(r'joão|maria', texto, flags=re.IGNORECASE))


