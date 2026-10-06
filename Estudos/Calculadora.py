def somar(numero1, numero2):
    return numero1 + numero2
def subtrair(numero1, numero2):
    return numero1 - numero2
def multiplicar(numero1, numero2):
    return numero1 * numero2
def dividir(numero1, numero2):
    return numero1 / numero2

numero1 = float(input("Digite o primeiro numero: "))
operacao = input("Digite a operação: ")
numero2 = float(input("Digite o segundo numero: "))

if operacao == "+":
    resultado = somar(numero1, numero2)
elif operacao == "-":
    resultado = subtrair(numero1, numero2)
elif operacao == "*":
    resultado = multiplicar(numero1, numero2)
elif operacao == "/":
    resultado = dividir(numero1, numero2)
else:
    print("operaçãp invalida!!")

print("resultado: ", resultado)