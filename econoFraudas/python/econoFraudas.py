fraudas = []

def calcular_fraudas():
    nome_frauda = input("Digite a marca da fralda:")
    valor_frauda = float(input("Digite o valor da fralda:"))
    quantidade_frauda = int(input("Digite a quantidade de fraldas:"))
    preço_cada_frauda = round((valor_frauda / quantidade_frauda), 2)

    frauda = {
        "nome_frauda": nome_frauda,
        "valor_frauda": valor_frauda,
        "quantidade_frauda": quantidade_frauda,
        "preço_cada_frauda": preço_cada_frauda
    }

    fraudas.append(frauda)
    print(fraudas)

quantas_marcas_de_fraudas = int(input("Quantas marcas de fraldas iremos avaliar hoje?"))

for i in range(quantas_marcas_de_fraudas):
    calcular_fraudas()

def encontrar_frauda_mais_barata():
    if len(fraudas) == 0:
        print("A lista de fraldas está vazia.")
        return

    valor_mais_barato = fraudas[0]

    for i in range(1, len(fraudas)):
        if fraudas[i]["preço_cada_frauda"] < valor_mais_barato["preço_cada_frauda"]:
            valor_mais_barato = fraudas[i]

    print(f"A fralda mais barata é da marca {valor_mais_barato['nome_frauda']}, a unidade sai a R${valor_mais_barato['preço_cada_frauda']}")

encontrar_frauda_mais_barata()

nova_adicao = int(input("Gostaria de adicionar mais alguma frauda? Se sim, quantas?"))

for i in range(nova_adicao):
    calcular_fraudas()

encontrar_frauda_mais_barata()
