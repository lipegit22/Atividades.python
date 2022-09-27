import math

print("1.Some dois números")
print("2.Raíz quadrada de um número")
a= int(input("Digite a opção desejada; "))
if a == 1:
    NumbSom1= float(input("Digite o primeiro número: "))
    NumbSom2= float(input("Digite o segundo número: "))
    Soma = numbSom1 + numbSom2
    print(f"A soma dos números é: {soma}")
else:
    numR = float(input("Digite um número: "))
    raiz = math.sqrt(numR)
    print (f"A raiz quadrada é: {round(raiz,2)}")