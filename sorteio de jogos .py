import numpy as np
print("")
mega = []

for list in range(1, 61):
    mega.append(list)

print("MEGA SENA", (sorted(np.random.choice(mega, 6, replace=False))))
print(" ")

loto_facil = []

for i in range(1, 26):
    loto_facil.append(i)

print("LOTO FÁCIL", (sorted(np.random.choice(loto_facil, 15, replace=False))))
print(" ")

quina = []
for i in range(1, 81):
    quina.append(i)

print("QUINA", (sorted(np.random.choice(quina, 5, replace=False))))
print('')
