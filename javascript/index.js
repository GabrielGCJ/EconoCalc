const fraudas = []

const calcularFraudas = () => {
  var nomeFrauda = prompt("Digite a marca da fralda:")
  var valorFrauda = parseFloat(prompt("Digite o valor da fralda:"))
  var quantidadeFrauda = parseInt(prompt("Digite a quantidade de fraldas:"))
  var preçoCadaFrauda = (valorFrauda / quantidadeFrauda).toFixed(2)

  const frauda = {
    nomeFrauda,
    valorFrauda,
    quantidadeFrauda,
    preçoCadaFrauda
  }

  fraudas.push(frauda);
  console.log(fraudas);
}

var quantasMarcasDeFraudas = parseInt(prompt("Quantas marcas de fraldas iremos avaliar hoje?"))

for (var i = 0; i < quantasMarcasDeFraudas; i++) {
  calcularFraudas()
}

const encontrarFraudaMaisBarata = () => {
  if (fraudas.length === 0) {
    console.log("A lista de fraldas está vazia.")
  }

  let valorMaisBarato = fraudas[0]

  for (var i = 1; i < fraudas.length; i++) {
    if (fraudas[i].preçoCadaFrauda < valorMaisBarato.preçoCadaFrauda) {
      valorMaisBarato = fraudas[i];
    }
  }

  console.log(`A fralda mais barata é da marca ${valorMaisBarato.nomeFrauda}, a unidade sai a R$${valorMaisBarato.preçoCadaFrauda}`);
}

encontrarFraudaMaisBarata()