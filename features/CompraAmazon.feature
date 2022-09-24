#language: pt
Funcionalidade: Comprar produto na Amazon
  Fluxo de compras no site da amazon
  Esquema do Cenário: comprar <titulo> a partir da busca
    Dado que acesso o site da amazon
    Quando busco por <produto> e pressiono Enter
    Então exibe uma lista de produtos relacionados com <produto>
    Quando escolho <titulo>
    Então aparece <titulo> no valor de <preco>
    Exemplos:
      |produto|titulo|preco|
      |hunter x hunter|Hunter X Hunter - Volume 11| R$ 23,90|
      |slam dunk|Slam Dunk Vol. 4| R$ 22,90|
      |o menino do pijama listrado|O menino do pijama listrado|R$ 29,94|
      |clean code|Código limpo: Habilidades práticas do Agile Software|R$ 70,99|