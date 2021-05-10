usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(f"Números Sem repetição: {usuarios_data_science | usuarios_machine_learning}")
print(f"Números repetidos: {usuarios_data_science & usuarios_machine_learning}")
print(f"Quem está em datascience e não está em machine Learning: {usuarios_data_science - usuarios_machine_learning}")