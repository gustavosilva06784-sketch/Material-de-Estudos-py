#"Return" serve para devolver um resultado de uma função.
#"Return" é completamente diferente de "Print".
#Com "Print" voce imprime algo na tela, ja com "Return" voce devolve um valor que voce atribuiu a uma função
#quando o codigo encontra "Return" ele termina neste exato momento.



def dobro(numero):
    return numero * 2
resultado = (dobro(16))
print(resultado)