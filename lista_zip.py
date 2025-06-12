#-*-coding:utf8;-*-
#qpy:console
#lista_zip.py
def espaco():
    print("")
espaco()
    
musicas = ["another brick in the wall", "stairway to heaven", "we will Rock you", "my Generation"]
horarios = ["19:00", "19:45", "20:10", "20:30"]

for m, h in zip(musicas, horarios):
    print(m, h )

espaco()

#dicionários e for loops

meu_dicio = {"nome":"Estevão", "idade": "31", "endereço":"SCL 409"}
espaco()

print(meu_dicio)
espaco()

print(meu_dicio["nome"])
espaco()

print(meu_dicio["idade"]) 
espaco()
#iterando dicionários
#percorrendo chaves de um dicionário como percorremos listas.

skills = {"velocidade":8, "sabedoria":7, "carisma":9}
for k in skills:
    print(k)

for k, v in skills.items():
    print (k, v)
espaco()

#else em listas

frutas = ['pera', 'uva', 'maça','abacaxi']
for fruta in frutas:
    if fruta == "abacaxi":
        print("Encontrado o abacaxi")
        break
else: 
    print("abacaxi não  encontrado ")
espaco()

#aplicando o conhecimento 

notas = [1, 6, 4, 10, 3, 2, 0, 7]
maior_nota = notas[0]
for n in notas:
    if n > maior_nota:
        maior_nota = n
print(maior_nota)
        
        
    
