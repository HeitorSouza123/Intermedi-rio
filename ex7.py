peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = peso/(altura)**2
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal", "Imc:", imc)
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso", "Imc:", imc)
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau I", "Imc:", imc)
elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade grau II", "Imc:", imc)
else:
    print("Obesidade grau III", "Imc:", imc)