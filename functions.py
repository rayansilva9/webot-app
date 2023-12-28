import random
import string
def gerar_numero_de_telefone():
    numero = ''
    for _ in range(11):  # Gera 8 dígitos aleatórios
        numero += str(random.randint(0, 9))
    return numero

def gerar_letras_aleatorias():
    letras_aleatorias = ''.join(random.choice(string.ascii_letters) for _ in range(7))
    return letras_aleatorias


def generate_user_agents(num_agents=200):
    user_agents = []

    for _ in range(num_agents):
        user_agent = (
            f'Mozilla/5.0 ({random.choice(["Windows NT 10.0", "Macintosh; Intel Mac OS X 10.15", "iPhone; CPU iPhone OS 15_0"])}) '
            f'AppleWebKit/{random.uniform(500, 600):.2f} (KHTML, like Gecko) '
            f'Chrome/{random.uniform(80, 100):.2f} Safari/{random.uniform(500, 600):.2f}'
        )
        user_agents.append(user_agent)
        random_user_agents = random.choice(user_agents)
    return random_user_agents


