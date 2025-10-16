import data
import socket
import json
import time

#variáveis
cidade_censor = data.escolherCidade()
id_censor = data.gerarIdCensor(cidade_censor)

#configuração de conexão com o servidor
endereco_servidor = "127.0.0.1"
porta_servidor = 13000

while True:
    try:
        #criando socket e cconectando ao servidor
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((endereco_servidor, porta_servidor))
            print("Cliente conectado!")
            while True:
                try:
                    dados = data.gerarDados(cidade_censor, id_censor)
                    mensagem = json.dumps(dados)
                    s.sendall(mensagem.encode("utf-8"))
                    time.sleep(3)
                except Exception as e:
                    #lidando com erros ao enviar dados
                    print("Erro ao enviar dados, tente novamente. Mensagem: ", e)
                    break
    except Exception as e:
        #lidando com erros de conexão
        print("Erro de conexão, tente novamente")
        break