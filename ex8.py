valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
if valor1 > valor2:
    print("O maior é:", valor1)
elif valor2 > valor1:
    print("O maior é:", valor2)
elif valor1 == valor2:
    print("Os valores são iguais", valor1, ("/"), valor2)
