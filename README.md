# Poloniex API

---

## Sobre a Aplicação

A aplicação coleta dados em tempo real do Endpoint "https://poloniex.com/public?command=returnTicker"

A aplicação é dividida em duas partes: Um executor que salva informações de acordo com parâmetros passados pelo usuário (Veja a explicação detalhada abaixo)
e uma página Web que renderiza as informações em uma tabela construída em HTML e CSS e com o microframework de Python Flask

---

## Informações coletadas

As informações coletadas pela aplicação são: Id, Name, last, High24hr e Low24hr

### Explicando as informações
**Name ->** Nome da Criptomoeda

**Last ->** Traz o último valor (price) da criptomoeda em questão

**High24hr ->** Traz o valor (price) mais alto coletado daquela criptomoeda

**Low24hr* ->** Traz o valor (price) mais baixo coletado daquela criptomoeda

-----

## Como funciona a aplicação:

Esta aplicação, ao rodar, percorre a lista de todas as criptomoedas presentes no endpoint "returnTicker" e adiciona essas informações no banco de dados.
O usuário pode determinar qual criptomoeda pode adicionar

*OBS:* O período escolhido deve ser informado em segundos e as opções disponíveis são: **60, 300 e 600** segundos (1 minuto, 5 minutos e 10 minutos)

Se a criptomoeda digitada não estiver disponível, a lista com as criptomoedas aparecerá imediatamente

---

## Inicializando a aplicação

Para inicializar a aplicação, basta estar no nível do arquivo docker-compose.yml, lembrando que o Docker e o Docker-Compose precisam estar instalados.
Estando no nível do arquivo do Docker Compose, digite o seguinte comando:

	`docker-compose up -d --build`

Este comando fará o "build" de toda a aplicação (Banco de dados, página Web e Aplicação)
Após este comando ser finalizado, os contêineres de "app" e "web" podem ser rodados individualmente.

**OBS:** Para rodar o contêiner "web" certifique-se de que o contêiner "app" esteja rodando em "background" tendo em vista que o contêiner web necessita de informações do contêiner app

Para executar qualquer um dos contêineres, utilize o comando:
	`docker-compose exec [nomedoContainer]`

O contêiner "app" irá rodar uma aplicação em um terminal e salvará as informações dos candles de acordo com o período determinado pelo usuário.
Ao salvar uma informação de candle, uma mensagem de sucesso aparecerá no terminal. Para encerrar o contêiner, digite CTRL + C

Por sua vez, o contêiner web irá renderizar uma página no endereço http://localhost:7000 com uma tabela de todos os candles salvos até o momento
Para interromper a execução da página web, assim como no contêiner web, utilize as teclas CTRL + C


## Estrutura do Banco de Dados

O banco de dados possui uma tabela chamada candles que possui os seguintes campos:

`Id int` **->** O id do candle (conjunto de informações) em questão

`currency varchar(50)` **->** Nome da criptomoeda

`period int` **->** O período escolhido pelo usuário para que as informações sejam rodadas.

`date_initial datetime` **->** Data e horário do momento em que o candle é salvo

`open_candle varchar(30)` **->** Ultimo valor da criptomoeda no momento em que os dados começaram a ser processados

`close_candle varchar(30)` **->** Ultimo valor da criptomoeda no momento em que o dado irá ser salvo (Fim do período escolhido)

`high varchar(30)` **->** Salva as informações do valor mais alto da criptomoeda registrado nas últimas 24 horas

`low varchar(30)` **->** Salva as informações do valor mais baixo da criptomoeda registrado nas últimas 24 horas


Para mais informações sobre Poloniex, visite o site:

https://docs.poloniex.com/#introduction
