import socket
import json

#definição da função de análise de clima
def analisarClima(dicionario):
    temperatura = dicionario["dados meteorológicos"]["temperatura, graus celsius"]
    umidade = dicionario["dados meteorológicos"]["umidade do ar, porcentagem"]
    pressao = dicionario["dados meteorológicos"]["pressão_hpa"]
    status = "Clima estável"

    #condicionais para pressão
    if pressao < 1005:
        status = "Clima instável, possibilidade grande de chuvas e ventos"
    elif pressao > 1020:
        status = "Tempo bom e agradável"
    
    #condicionais de temperatura
    if temperatura < 20:
        status += " | Alerta de frio, mantenha-se aquecido e agasalhado"
    elif temperatura > 30:
        status += " | Alerta de calor: tente se manter hidratado e em um ambiente agradável"

    #condicionais de umidade do ar
    if 40 <= umidade <= 70:
        status += " | Umidade normal, tempo bom"
    elif umidade < 40:
        status += " | Clima muito seco, tome bastante água e mantenha-se hidratado"
    else:
        status += " | Clima muito úmido, tome cuidado com alimentos mofados e bactérias que podem se proliferar"
    return status

#configuração do servidor
endereco = "127.0.0.1"
porta = 13000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((endereco, porta))
sock.listen(porta)
print("Servidor ativo escutando na porta ", porta)
while True:
    try:
        conexaoCliente, enderecoCliente = sock.accept()
        print("Cliente conectado!")
        while True:
            try:
                dados = conexaoCliente.recv(1024)
                if not dados:
                    print("Cliente desconectou, sem mensagens")
                    break
                mensagem_cliente = dados.decode("utf-8")
                censor_dict = json.loads(mensagem_cliente)
                print("Dados do censor: \n", censor_dict)
                cidade = censor_dict["cidade_censor"]
                status_clima = analisarClima(censor_dict)
                print("Com base na análise realizada, na cidade ", cidade, " o status sobre o clima aqui é: ", status_clima)
            except Exception as e:  
                #lidando com mensagens não recebidas ou algo assim
                print("Mensagem não encontrada, erro de conexão")
                break
        #fechando a conexão do cliente
        conexaoCliente.close()
    except KeyboardInterrupt:
        #lidando com o encerramento do servidor pelo usuário (ctrl+c)
        print("Servidor encerrado pelo usuário")
        break
    except Exception as e:
        #lidando com erros de conexão
        print("Erro ao conectar, tente novamente")
        break

#fechando o socket
sock.close()