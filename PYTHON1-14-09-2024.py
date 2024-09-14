# Pergunta ao usuário sobre sol e dinheiro, utilizando o and.
sol = input("Você tem sol? (sim/não): ")
money = input("Você tem dinheiro? (sim/não): ")

# Determina com base nas respostas
role = "Praia" if sol == "sim" and money == "sim" else "Netflix"

# Printa o resultado
print("O seu rolê é:", role)
