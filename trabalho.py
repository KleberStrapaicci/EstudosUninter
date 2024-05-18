# a.print com uma mensagem de boas-vindas
print("Bem-vindo a loja de Raçao da esquina")
# b.input do valor unitário e da quantidade do produto
valor_unitario = float(input("Qual é o valor da Ração: "))
quantidade = int(input("Quantos pacotes de Ração: "))
# c.valor total sem desconto
valor_total_sem_desconto = valor_unitario * quantidade
#d.estruturas if, elif e else
if valor_total_sem_desconto < 2500:
    desconto = 0
elif valor_total_sem_desconto < 6000: 
    desconto = 4
elif valor_total_sem_desconto < 10000:
    desconto = 7
else:
    desconto = 11
#e.valor total com desconto
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto / 100)
#f.saida dos valores sem e com descontos 
print(f"\nValor total sem desconto: R${valor_total_sem_desconto:.2f}")
print(f"Valor total com desconto: R${valor_total_com_desconto:.2f}")
if valor_total_sem_desconto >= 2500:
    print(f"Desconto aplicado: {desconto}%")
else:
    print("Nenhum desconto aplicado.")