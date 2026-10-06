#"Range" serve para criar uma sequencia/lista de numeros muito utilizado com "for".
#a estrutura é: range(Inicio, Fim, Passo).
#você tambem pode determinar onde a sequencia comeca, onde ela termina e quantas casas ela deve pular.
#o final sempre ira terminar em um numero antes do numero final definido, se eu digitar para parar no 11, a sequencia ira terminar no 10, pois ele tambem está contando com o numero zero.

for numero in range(1, 11, 2):
    print(numero)