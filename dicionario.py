aparicoes = {
    "Guilherme": 1,
    "Cachorro": 2,
    "Nome": 2,
    "Vendo": 1
}
#Outra Forma de Criar Dicionario
aparicoes_com_construtor = dict(Guilherme=2, Teste=1)
print(aparicoes_com_construtor)
print(type(aparicoes))

print(aparicoes["Guilherme"])

print(aparicoes.get("xpto", 0))

#Remover Elemento
del aparicoes["Vendo"]

#Listando os Item
for elemento in aparicoes.items():
    print(elemento)

#Listando Apenas Values
for elemento in aparicoes.values():
    print(elemento)

#Listando Apenas Chaves
for elemento in aparicoes.keys():
    print(elemento)

#Listando os Item "Desempacotando em Variável"
for elemento, chave in aparicoes.items():
    print(elemento, chave)