# Pergunta ao usuário sobre sol e dinheiro, dessa vez utilizando if dentro de if.
sol = input("Você tem sol? (sim/não): ")
money = input("Você tem dinheiro? (sim/não): ")

# Determina com base nas respostas
if sol == "sim":
    if money == "sim":
        role = "Praia"
    else:
        role = "Netflix"
else:
    role = "Netflix"

# Printa o resultado
print("O seu rolê é:", role)
