#-*-coding:utf8;-*-
#qpy:console
#criando_string.py
def space():
    print ()
    
space()
print("I'm fine")
print('Ele disse "bão uaí"')
print('doesn\'t')

# o \n, \t são caracteres especiais 
# que representam uma nova linha e tab, respectivamente 

# se usar um \n será quebrada uma linha
print("Primeira linha\nSegunda linha")

# se usar dois \n \n será quebrada duas linhas.
print("Primeira linha\n \nSegunda linha.")
print('\tEra uma vez')# \t insere um tab de oito índices na frase.

# r(raw string) ou backslash 
print('C:\some\name')
# para inserir strings como caminho podemos ter problemas com \n nom nome do caminho.
# nesse caso a palavra \ name fica composta com \n onde configura quebra de linha

print(r'C:\some\name')# com r(raw string)

print('C:\some\\name')# com \(backslash) adicionamos mais um contrabarra.

                     