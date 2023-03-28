n1 = float(input("Qual a primeira nota?: "))
n2 = float(input("Qual a segunda nota?: "))
n3 = float(input("Qual a terceira nota?: "))

media = (n1 + n2 + n3) / 3

if media >= 6: 
    print(f"O aluno foi APROVADO com a média de: {round(media, 2)}!")
else:
    print(f"O aluno foi REPROVADO com a média de: {round(media, 2)}!")
