## 1. Problema de Negocio

Este projeto se trata de uma empresa fictícia com o intúito de aplicar os conhecimentos adquiridos durante o Curso de Analise de Dados com Python na Comunidade de DS. 

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:

### Geral
    1. Quantos restaurantes únicos estão registrados?
    2. Quantos países únicos estão registrados?
    3. Quantas cidades únicas estão registradas?
    4. Qual o total de avaliações feitas?
    5. Qual o total de tipos de culinária registrados?

### Pais
    1. Qual o nome do país que possui mais cidades registradas?
    2. Qual o nome do país que possui mais restaurantes registrados?
    3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
    4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
    5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
    6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
    7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
    8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
    9. Qual o nome do país que possui, na média, a maior nota média registrada?
    10. Qual o nome do país que possui, na média, a menor nota média registrada?
    11. Qual a média de preço de um prato para dois por país?

### Cidade
    1. Qual o nome da cidade que possui mais restaurantes registrados?
    2. Qual o nome da cidade que possui mais restaurantes com nota média acima de4?
    3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
    4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
    5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
    6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
    7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
    8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

### Restaurantes
    1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
    2. Qual o nome do restaurante com a maior nota média?
    3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
    4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
    5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
    6. Os restaurantes que aceitam pedido online são também, na média, osrestaurantes que mais possuem avaliações registradas?
    7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
    8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

### Tipos de Culinária
    1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
    2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
    3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
    4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
    5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
    6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
    7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
    8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
    9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
    10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
    11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
    12. Qual o tipo de culinária que possui a maior nota média?
    13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez. O CEO precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.

Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as perguntas feitas do CEO e criar o dashboard solicitado.

## 2. Premissas assumidas para a analise
	1. O Modelo de Negocio é WebService
	2. As principais visões de negocio foram:Visão Geral, Visão Pais , Visão Cidade, Visão Culinarias
	3. Os dados para foram fornecido pela própria empresa Fome Zero

## 3. Estratégia da solução
	O Dashboard foi desenvolvido utilizando metricas que refletem as 3 principais visões e a Paginal inical com Visão Geral.

	1. Visão Geral
	2. Visão dos Pais
	3. Visão das Cidades
	4. Visão de Culinarias
	
	Cada visão e representa seus respectivo conjunto de metricas.
	1. Visão Geral
		a. Restaurantes Cadastrados
		b. Países Cadastrados
		c. Cidades Cadastrados
		d. Avaliações Feitas na Plataforma
		e. Tipos de Culinárias Oferecida
		f. Mapa para visualização dos locais de cada restaurante
	2. Visão Paises
		a. Quantidade de Restaurantes registrados por Pais
		b. Quantidade de Cidade por Pais
		c. Média de Avaliações feitas por País
		d. Média de Preço de um prato para duas pessoas por País
	3. Visão Cidade
		a. Top 10 Cidades com mais Restaurantes
		b. Top 7 Cidades que tem Avaliação acima de 4
		c. Top 7 Cidades que tem Avaliação menor de 2.5
		d. Top 10 Cidades com mais Restaurantes
	4. Visão Culinarias
		a. metricas de culinarias italianas mais bem avaliadas
		b. Top 10 Melhores Restaurantes
		c. Top 10 Melhores Culinarias
		d. Top 10 Piores Culinarias

## 4. top 3 insights de dados
	1. Os Restaurantes que aceitam pedidos online na media são o que tem mais avaliações.
	2. Os Restaurantes que fazem reserva são tambem os que tem a maior media de prato para duas pessoas.
	3. Os Restaurantes de culinaria japonesa tem uma media maior de prato para dois maior que os BBQ.

## 5. Produto Final do Projeto
	O painel é online hospedado em Cloud e disponivel para acesso em qualquer dispositivo conectado a internet
	
	O Painel pode ser acessado atraves desse link: https://luizmoschetta-fome-zero.streamlit.app/

## 6. Objetivo
	O objetive desse projeto é criar um conjunto grafico que exibam as metricas da melhor forma possivel
	para o CEO da empresa.
	De ambas as visões é possivel visualizar todas as principais metricas da situação atual do Marketplace.

## 7. Proximos passos
	1. Criar mais filtros em ambas as visões para visualizar as metricas com pais detalhes.
	2. adicionar futuramente os top 3 insight de dados de uma maneira que seja mais facilmente compreendido.
	3. reduzir o numero de metricas.
