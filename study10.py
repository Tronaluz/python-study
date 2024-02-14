# frutas = {"maçã", "abacaxi", "laranja"}

# frutas.add("pera")
# frutas.remove("maçã")
# frutas.pop()

# print(frutas)


# set1 = {"maçã", "abacaxi", "laranja"}
# set2 = {0, 3, 50, -74}
# set3 = {True, False, True, False}
# set4 = {"Lucas", 23, True}

# print(set1)
# print(set2)
# print(set3)
# print(set4)


# Dictionary-py-----------------

meses = {
    "Jan":"Janeiro",
    "Fev":"Fevereiro",
    "Mar":"Março",
    "Abr":"Abril",
    "Mai":"Maio",
    "Jun":"Junho",
    "Jul":"Julho",
    "Ago":"Agosto",
    "Set":"Setembro",
    "Out":"Outubro",
    "Nov":"Novembro",
    "Dez":"Dezembro",
    # "Dez":"Dezembro", não aceita valor duplicado
}

print(meses["Jan"])
print(meses["Abc"])

print(meses.get("Jan"))
print(meses.get("Abc"))
print(meses.get("Abc", "Padrão"))

print(len(meses))