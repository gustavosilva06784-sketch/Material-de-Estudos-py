def calculadora():
    numero1 = float(input("digite o primeiro numero: "))
    operador = input("Digite a operacao: ")
    numero2 = float(input("digite o segundo numero: "))

    if operador ==  "+":
        return "Resultado", numero1 + numero2
    elif operador == "-":
        return"Resultado", numero1 - numero2
    elif operador == "*":
        return"resultado:", numero1 * numero2
    elif operador == "/":
        return"resultado", numero1 // numero2
    else:
        print("operação invalida!")
resultado = calculadora()
print("Resultado: ", resultado)