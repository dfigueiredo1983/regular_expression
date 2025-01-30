# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html

import re

# findall search sub
# compile

string = 'Este é um teste de expressões regulares. O teste e feito de forma simples. Teste, testes, testem, este também vale'

# print(re.search(r'teste', string)) # encontra a primeira ocorrência dentro da string ou None
# print(re.findall(r'teste', string)) # retorna uma lista com todas as ocorrência da pesquisa

# print(re.sub(r'teste', 'DANIEL', string))   # Substitui todas as ocorrências pela string indicada
                                            # ou seja, trocou todas as ocorrências de teste por DANIEL


# print(re.sub(r'[.-]', '', '725.220.111-20')) # remove os elementos dentro do conjunto [.-] da string indicada

# nome = 'Daniel do Carmo Figueiredo'
# print(nome.upper())
# print(nome.lower())
# print(re.sub(" ", "", nome).lower())
# print(re.sub(" ", "", nome).capitalize())

# print(re.findall(r'\b[tT]?este[sm]?\b', string)) # retorna uma lista com todas as ocorrência da pesquisa
# print(re.findall(r'\b[tT]este[sm]?\b', string)) # retorna uma lista com todas as ocorrência da pesquisa

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DANIEL', string))

reg_cpf = re.compile(r'[.-]')
print(reg_cpf.sub("", "725.220.111-20"))


