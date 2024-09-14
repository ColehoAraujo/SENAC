# Lê o ano e o preço do carro
ano = int(input("Digite o ano do carro: "))
preço = float(input("Digite o preço do carro: "))

# Calculos
if ano < 1990:
    taxa = 0.01
else:
    taxa = 0.015

# Imposto a ser pago
imposto = preço * taxa

# Printa o resultado
print("O imposto a ser pago é:", imposto)
