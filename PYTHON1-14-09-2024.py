# Pergunta ao usuário sobre sol e dinheiro para possibilidade ir pra praia ou ficar em casa
sol = input("Você tem sol? (sim/não): ")
money = input("Você tem dinheiro? (sim/não): ")

# Determina o papel com base nas respostas, assumindo que o usuário insira exatamente "sim" ou "não"
role = "Praia" if sol == "sim" and money == "sim" else "Netflix"

# Exibe o resultado
print("O seu rolê é:", role)
