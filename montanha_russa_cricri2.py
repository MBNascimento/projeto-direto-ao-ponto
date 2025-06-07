print(" ")
# versão com while e input para validação da montanha_russa_cricri
idade = int(input("Idade : "))
altura = float(input("altura : "))
ticket_valido = True
while ticket_valido and idade > 18 and altura > 1.5:
    print("Ticket Válido, Entrada permitida")
    break
else:
    print("Requisitos não atendidos")

print("")
