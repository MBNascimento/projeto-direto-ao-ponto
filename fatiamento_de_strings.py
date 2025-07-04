#-*-coding:utf8;-*-
#qpy:console
#fatiamento_de_strings.py
print( )

my_string = 'Pink Floyd'

# observe que a contagem na computação começa com o número 0.

print(my_string[0])
print(my_string[9])

# podemos começar a contar da direita pra 
# esquerda com índices negativos
print(my_string[-1])
print(my_string[-2])

# o fatiamento permite extrair partes da string.
# o caractere so índice se início é incluído 
# enquanto o índice do final é excluído.
print(my_string[0:2])
print(my_string[5:10])

# o índice do início pode ser omitido 
# assim o fatiamento começará no início 
# se o índice final for omitido o fatiamento vai até o fim.
print(my_string[ :6])
print(my_string[3: ])

# strings são Imutáveis 
# o conteúdo se uma string não pode ser mudado após sua criação 
# porém, isso não é um problema, pois criar strings é fácil.
my_strings = 'liga'
# my_strings[0] = 'v' ao tentar mudar a string um erro acontece
# 
print('v'+my_strings[1:])

