import random

parte1 = [
    "O código está funcionando perfeitamente",
    "Preciso revisar esse commit",
    "Vamos atualizar o repositório"
]
parte2 = [
    "Servidor reiniciado sem apresentar erros",
    "Deploy finalizado com sucesso",
    "Adicionei logs para debug"
]
parte3 = [
    "Pull request enviado agora",
    "Testes automatizados passaram corretamente",
    "Banco de dados atualizado hoje"
]

print(random.choice(parte1), random.choice(parte2), random.choice(parte3))
