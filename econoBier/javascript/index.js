const beers = []

const beerCalc = () => {
  var nameBeer = prompt("Digite o nome da cerveja:")
  var priceBeer = parseFloat(prompt("Digite o valor da cerveja:"))
  var quantityBeer = parseInt(prompt("Digite a quantidade de cerveja em ml:"))
  var priceMlBeer = (priceBeer / quantityBeer).toFixed(6)

  const beer = {
    nameBeer,
    priceBeer,
    quantityBeer,
    priceMlBeer
  }

  beers.push(beer);
  console.log(beers);
}

var beersEvaluated = parseInt(prompt("Quantas tipos de cerveja iremos avaliar hoje?"))

for (var i = 0; i < beersEvaluated; i++) {
  beerCalc()
}

const cheapestBeer = () => {
  if (beers.length === 0) {
    console.log("A lista de cervejas está vazia.")
  }

  let cheapest = beers[0]

  for (var i = 1; i < beers.length; i++) {
    if (beers[i].priceMlBeer < cheapest.priceMlBeer) {
      cheapest = beers[i];
    }
  }

  console.log(`A cerveja mais barata é da marca ${cheapest.nameBeer}, o valor do ML sai a R$${cheapest.priceMlBeer}`);
}

cheapestBeer()

var novaAdição = parseInt(prompt("Gostaria de adicionar uma novq cerveja? Se sim quantas?"))

for (var i = 0 ; i = novaAdição ; i++) (
  beerCalc()
  )
  
  cheapestBeer()
