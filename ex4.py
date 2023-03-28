letra = str(input("Digite uma letra: "))

letra = letra.lower()

if (len(letra) > 1):
    print("Apenas uma letra, por favor!")
else:
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print("A letra é uma VOGAL!")
    else:
        print("A letra é uma CONSOANTE!")