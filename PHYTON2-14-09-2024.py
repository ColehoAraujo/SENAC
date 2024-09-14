# Pergunta ao usuário sobre sol e dinheiro, utilizando OR, IF, ELSE
sol = input("Você tem sol? (sim/não): ")
money = input("Você tem dinheiro? (sim/não): ")

# Determina as respostas, usando 'or' para verificar se pelo menos um é 'sim'
if sol == "sim" or money == "sim":
    role = "Praia"
else:
    role = "Netflix"

# Printa o resultado
print("O seu rolê é:", role)
