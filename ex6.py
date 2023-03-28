hora = int(input("Digite a decimal hora: "))
minuto = int(input("Digite a decimal minuto: "))

if (hora < 00 or hora > 23):
    print("São válidas apenas as horas entre 00:00 e 23:59")
    exit()
elif (minuto < 00 or minuto > 59):
    print("São válidas apenas as horas entre 00:00 e 23:59")
    exit()
else:
    print(f"As horas {hora}:{minuto} são válidas")