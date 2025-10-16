import socket

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
                mensagem = dados.decode("utf-8")
                print("Mensagem do cliente: ", mensagem)
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