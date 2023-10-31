print('EcoFraudas')

fraldas = []

def calcular_fraldas():
    nome_fralda = input("Digite a marca da fralda: ")
    valor_fralda = float(input("Digite o valor da fralda: "))
    quantidade_fralda = int(input("Digite a quantidade de fraldas: "))
    preço_cada_fralda = round(valor_fralda / quantidade_fralda, 2)

    fralda = {
        "nomeFralda": nome_fralda,
        "valorFralda": valor_fralda,
        "quantidadeFralda": quantidade_fralda,
        "preçoCadaFralda": preço_cada_fralda
    }

    fraldas.append(fralda)
    print(fraldas)

quantas_marcas_de_fraldas = int(input("Quantas marcas de fraldas iremos avaliar hoje?"))

for i in range(quantas_marcas_de_fraldas):
    calcular_fraldas()

def encontrar_fralda_mais_barata():
    if len(fraldas) == 0:
        print("A lista de fraldas está vazia.")
        return

    valor_mais_barato = fraldas[0]

    for i in range(1, len(fraldas)):
        if fraldas[i]["preçoCadaFralda"] < valor_mais_barato["preçoCadaFralda"]:
            valor_mais_barato = fraldas[i]

    print(f"A fralda mais barata é da marca {valor_mais_barato['nomeFralda']}, a unidade sai a R${valor_mais_barato['preçoCadaFralda']}")

encontrar_fralda_mais_barata()