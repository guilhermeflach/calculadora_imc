print("Calculadora de IMC")

peso = float(input("Insira seu peso em kilogramas: "))
altura = float(input("Insira sua altura em metros: "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")