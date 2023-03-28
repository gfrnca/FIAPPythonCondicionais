lado1 = float(input("Qual o tamanho do primeiro lado?: "))
lado2 = float(input("Qual o tamanho do segundo lado?: "))
lado3 = float(input("Qual o tamanho do terceiro lado?: "))

if (lado1 == lado2 == lado3):
    print("O triângulo é equilátero")
elif (lado1 == lado2 or lado1 == lado3):
    print("O triângulo é isósceles")
elif (lado2 == lado1 or lado2 == lado3):
    print("O triângulo é isósceles")
elif (lado3 == lado1 or lado3 == lado2):
    print("O triângulo é isósceles")
else:
    print("O triângulo é um escaleno")