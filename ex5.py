x = int(input("Valor 1:"))
y = int(input("Valor 2:"))
z = int(input("Valor 3:"))
if ((z>=x) and (z<=y)) or ((z<=x) and (z>=y)):
    print("Z, Está no intervalo!")
else:
    print("Z, Não está no intervalo!")
