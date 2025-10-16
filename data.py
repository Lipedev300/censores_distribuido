import random
import time

cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Recife",
    "Salvador",
    "Florianópolis",
    "Curitiba",
    "Porto Alegre"
]

def escolherCidade():
    return random.choice(cidades)

def gerarIdCensor(cidade):
    prefixo = cidade[:3].upper()
    sufixo = random.randint(100, 1000)
    return f"{prefixo}-{sufixo}"

#criando função de gerar dados
def gerarDados(cidade, id):
    temperatura = round(random.uniform(5, 45), 1)
    umidade = random.randint(40, 95)
    pressao = round(random.uniform(980, 1030), 1)
    return {
        "cidade_censor": cidade,
        "id_censor": id,
        "data/hora": time.strftime("%y-%m-%d-%h:%m%s"),
        "dados meteorológicos": {
            "temperatura, graus celsius": temperatura,
            "Pressão_hpa": pressao,
            "umidade do ar, porcentagem": umidade
        }
    }