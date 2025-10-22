#Projeto de simulação de censores
Desenvolvedor: Luiz Felipe de Souza Basso

Este projeto é uma simulação de envio e recebimento de dados em tempo real por parte de censores meteorológicos.
Ele é um sistema distribuído construído com base em sockets TCP, que conta com um servidor responsável por fazer o processamento, análise e envio de status climático com base nos dados apresentados por diferentes clientes, que na verdade são cidades.
O servidor suporta concorrência (threading), o que significa que o envio de dados por um cliente não interfere no desempenho de outro censor que esteja também enviando.

## principais funcionalidades

** - Sistema distribuído baseado em sockets TCP e concorrência (threads), construído em python **
** - Comunicação concorrente entre cliente e servidor **
** - Envio de dados em tempo real para o servidor **
** - Análise de dados climáticos conforme métricas climáticas reais, incluindo números de temperatura, pressão e umidade do ar **

## como executar

-- 1. Com o projeto aberto, rode o código do servidor (server.py) em um terminal
-- 2. Agora, abra outro terminal e rode o código do cliente (cliente.py)
-- 3. Repita o mesmo processo em outros um ou dois terminais, rodando sempre o código do cliente
-- 4. Você verá a concorrência e comunicação bidirecional entre cliente e servidor acontecendo, pois os clientes enviam os dados, o servidor os processa e entrega o status climático apenas no terminal daquele cliente específico