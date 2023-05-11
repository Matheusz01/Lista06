internet = float(input("Informe o valor de internet na fatura: "))
ligacao_l = float(input("Informe o valor de ligação local na fatura:"))
ligacao_u = float(input("Informe o valor de ligação urbana na fatura: "))
torpedo= float(input("Informe o valor de torpedos na fatura: "))

fatura_desconto = (internet + ligacao_l) + (ligacao_u + torpedo)

if (internet > ligacao_l) and \
        (internet > ligacao_u) and \
        (internet > torpedo):
    print("O tipo de desconto concedido foi de 5% de internet")
    desconto = (internet * 0.05)
    sem_desconto = (internet * 0.05) + (internet + ligacao_l) + (ligacao_u + torpedo)

elif (ligacao_l > internet) and \
        (ligacao_l > ligacao_u) and \
        (ligacao_l > torpedo):
    print("O tipo de desconto concedido foi de 10% de ligação local")
    desconto = (ligacao_l * 0.10)
    sem_desconto = (ligacao_l * 0.10) + (ligacao_l + internet) + (ligacao_u + torpedo)

elif (ligacao_u > internet) and \
        (ligacao_u > ligacao_l) and \
        (ligacao_u > torpedo):
    print("O tipo de desconto concedido foi de 10% de ligação inter urbana")
    desconto = (ligacao_u * 0.10)
    sem_desconto = (ligacao_u * 0.10) + (ligacao_u + internet) + (ligacao_l + torpedo)

else:
    print("O tipo de desconto concedido foi de 50% de torpedos")
    desconto = (torpedo * 0.50)
    sem_desconto = (torpedo * 0.50) + (torpedo + internet) + (ligacao_l + ligacao_u)

print(f"O valor do desconto foi de R${desconto}")
print(f"O valor sem desconto é de R${sem_desconto}")
print(f"o valor com desconto é R${fatura_desconto}")
