# open("caminho", "r")

#  Modes/Modos
# r - read/leitura
# a - append/incrementar
# w - write/escrita
# # x - create/criar
# # r+ - read and write/leitura e escrita

# # arquivo = open("study12/test.txt", "r")
# # arquivo = open("study12/test.txt", "w") ira limpar o arquivo e colocar novas informações diferente do a
# # arquivo = open("study12/test2.txt", "w")
# arquivo = open("study12/test3.txt", "x")


# # print(arquivo.readable())
# # print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# # print(arquivo.readline())

# lista = arquivo.readlines()
# print(lista)
# print(lista[3])

# arquivo.write("Madandoka\n")
# arquivo.write("Cobol\n")


# arquivo.close()

import os # biblioteca para remover arquivos

# os.remove("study12/test3.txt") # comando para remover arquivos

# if os.path.exists("study12/test3.txt"):
#  os.remove("study12/test3.txt")
# else: 
#   print("Arquivo não existe")

# if os.path.exists("study12/test2.txt"):
#  os.remove("study12/test2.txt")
# else: 
#   print("Arquivo não existe")

os.rmdir("study12/nova_pasta") # comando para remover pastas, só funciona se a pasta estiver vazia

