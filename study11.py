
try:
    numero = int(input("Digite um numero: "))
    print(numero)
except ZeroDivisionError: # Tratamento de erro
    print("Divisáo por zero não é possivel")
except ValueError: # Tratamento de erro
    print("Digite um  valor válido.")
except:
    print("Erro inesperado")
finally: # Sempre será executado
    print("Fim do programa")