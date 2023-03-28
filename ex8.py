n1 = float(input("Qual o primeiro número?: "))
n2 = float(input("Qual a segundo número?: "))
n3 = float(input("Qual a terceiro número?: "))

if (n1 < n2 and n3): 
    print(f"O número {n1} é o menor.")
elif (n2 < n1 and n3): 
    print(f"O número {n2} é o menor.")
elif (n3 < n1 and n2):
    print(f"O número {n3} é o menor.")
elif (n1 == n2 == n3):
    print("Os números são iguais")