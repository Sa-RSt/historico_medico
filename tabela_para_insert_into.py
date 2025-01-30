import sys
import re

pat_declaracao = r'\s*(?:create|CREATE)\s+(?:table|TABLE)\s+(?P<nome_tabela>\w*)\s*\(\s*(?P<colunas>.*)\s*,.*(?:primary|PRIMARY).*\).*;\s*'
decl_tabela = sys.stdin.read()
parse = re.match(pat_declaracao, decl_tabela, re.MULTILINE)
nome_tabela = parse.group('nome_tabela')
colunas = parse.group('colunas')

pat_coluna = r'\s*(?P<nome_coluna>[a-zA-Z]\w*)\s+[a-zA-Z][\w\s\(\)]*,\s*'
nomes_colunas = [m.group('nome_coluna') for m in re.finditer(pat_coluna, colunas)]
print(f"print('INSERT INTO {nome_tabela}')")
print("print('(", ', '.join(nomes_colunas), ")')", sep='')
print("print('VALUES')")
