n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if (n1 == n2):
    print("Os números são iguais")
elif (n1 > n2):
    print(f"{n1} é maior do que {n2}")
else:
    print(f"{n2} é maior do que {n1}")