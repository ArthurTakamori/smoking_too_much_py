tempo = float(input("Insira tempo como fumante (em anos):"))
valor = float(input("Insira o valor do Maço:"))
quant = float(input("Insira Quantidade de maços por dia:"))

gasto = (tempo * 12 * 30) * valor * quant

if gasto <20000:
    print(f"Com o valor R$ {gasto:.2f}, você poderia ter dado entrada em um carro.")
elif gasto >= 20000 and gasto <= 50000:
    print(f"Com o valor R$ {gasto:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor R$ {gasto:.2f}, você poderia ter comprado um carro zero.")
