import random

parte1 = []
parte2 = []
parte3 = []

lingua = int(input("Escolha a língua: 1 - portuguÊs; 2 - inglês\n"))

if lingua == 2:
    parte1 = []
    parte2 = []
    parte3 = []

print(random.choice(parte1), random.choice(parte2), random.choice(parte3))
