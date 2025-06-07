# sem o else se digitado senha errada não temos retorno
senha = input("Digite a senha 1 :")
if senha == "123Oliveira4":
    print("Senha correta")

senha = input("Digite a senha 2 :")
if senha == "123Oliveira4":
    print("Senha correta")
else:
    print("Senha incorreta")

senha = input("Digite uma senha 3 : ")
if senha:
    print("Senha válida")
else:
    print("A senha não pode estar em branco ")
