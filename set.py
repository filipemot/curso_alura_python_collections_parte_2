usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(f"Números Sem repetição: {usuarios_data_science | usuarios_machine_learning}")
print(f"Números repetidos: {usuarios_data_science & usuarios_machine_learning}")
print(f"Quem está em datascience e não está em machine Learning: {usuarios_data_science - usuarios_machine_learning}")

#Set Imutável
usuarios_data_science = frozenset(usuarios_data_science)
#usuarios_data_science.add(15)

#Retirando Duplicidade de Palavras
minha_palavra = "Meu nome é Filipe, o seu nome é Carlos"
print(set(minha_palavra.split()))#{'o', 'nome', 'é', 'seu', 'Meu', 'Filipe,', 'Carlos'}
