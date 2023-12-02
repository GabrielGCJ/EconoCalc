print('EconoBeer')

beers = []

def beerCalc():
    nameBeer = input("Digite o nome da cerveja: ")
    priceBeer = float(input("Digite o valor da cerveja: "))
    quantityBeer = int(input("Digite a quantidade de cerveja em ML: "))
    priceMlBeer = format(priceBeer / quantityBeer, '.6f')

    beer = {
        "nameBeer": nameBeer,
        "priceBeer": priceBeer,
        "quantityBeer": quantityBeer,
        "priceMlBeer": priceMlBeer
    }

    beers.append(beer)
    print(beers)

beersEvaluated = int(input("Quantos tipos de cerveja iremos avaliar hoje?"))

for i in range(beersEvaluated):
    beerCalc()

def cheapestBeer():
    if len(beers) == 0:
        print("A lista de cervejas está vazia.")
        return

    cheapest = beers[0]

    for i in range(1, len(beers)):
        if beers[i]["priceMlBeer"] < cheapest["priceMlBeer"]:
            cheapest = beers[i]

    print(f"A cerveja mais barata é da marca {cheapest['nameBeer']}, o valor do ML sai a R${cheapest['priceMlBeer']}")

cheapestBeer()