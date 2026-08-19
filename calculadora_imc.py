def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

print("Calculadora de IMC")

peso = float(input("Insira seu peso em kilogramas: "))
altura = float(input("Insira sua altura em metros: "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")



classificacao = classificar_imc(imc)
print(f"Classificação: {classificacao}")

