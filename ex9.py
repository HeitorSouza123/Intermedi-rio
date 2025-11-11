lado1 = int(input("Digite o valor do primeiro lado:"))
lado2 = int(input("Digite o valor do segundo lado:"))
lado3 = int(input("Digite o valor do terceiro lado:"))
if (lado1 == lado2) and (lado1 == lado3):
    print("Triangulo Equilátero")
elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print("Triangulo Isósceles")  
elif (lado1 != lado2) and (lado1 != lado3):
    print("Triangulo Escaleno")
else:
    print("Lado inválido!")
