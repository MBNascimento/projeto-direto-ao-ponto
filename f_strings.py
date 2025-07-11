# f-string.py
#-*-coding:utf8;-*-
#qpy:console

# f-strings, o método mais recente(Python 3.6+)
# uma nova forma de formatar strings muito elegante e poderosa surgiu com pyrhon 3.6,
# chamado de Literal String Interpolation, com as f-strings
# Vamos ver alguns exemplos 

def space():
    print( )
space()

nome = 'Ritchie'
mensagens = 8
print(f'Bem vindo, {nome}')
space()
print(f'{nome}, você tem {mensagens} mensagens novas')
space()

# as f-strings têm um recurso surpreendente, permitem que expressões sejam executadas dentro delas,veja abaixo.
a = 2
b = 3
print(f'O reaultado de a vezes b é {a*b}')
space()

# Formatando um float:
pi = 3.14159
print(f'O valor aproximado de pi é {pi:.2f}')

