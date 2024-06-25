#EXERCÍCIO 1
def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num - 1)
print(fatorial(5)) 

#EXERCÍCIO 2
def mostrar_sequencia(inicio, fim):
    if inicio > fim:
        return
    else:
        print(inicio)
        mostrar_sequencia(inicio + 1, fim)
mostrar_sequencia(3, 7)

#EXERCÍCIO 3
def exponencial(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * exponencial(base, exp - 1)
print(exponencial(2, 4))  

#EXERCÍCIO 4
def soma_pesos(numero, digitos):
    if numero == 0:
        return 0
    else:
        return soma_pesos(numero // 10, digitos + 1) + (numero % 10) * 2 ** digitos
print(soma_pesos(1100, 0)) 

#EXERCÍCIO 5
def soma(x, y):
    if y == 0:
        return x
    else:
        return soma(x + 1, y - 1)

#EXERCÍCIO 6
def pesquisa_bin(vetor, valor, inferior, superior):
    if inferior > superior:
        return False
    else:
        meio = (inferior + superior) // 2
        if vetor[meio] == valor:
            return meio
        elif vetor[meio] < valor:
            return pesquisa_bin(vetor, valor, meio + 1, superior)
        else:
            return pesquisa_bin(vetor, valor, inferior, meio - 1)
vetor = [2, 5, 7, 10, 15, 18, 22, 25, 30, 35]
print(pesquisa_bin(vetor, 18, 0, len(vetor) - 1)) 
print(pesquisa_bin(vetor, 20, 0, len(vetor) - 1))  

#EXERCÍCIO 7
def para_binario(num):
    if num == 0:
        return ''
    else:
        return para_binario(num // 2) + str(num % 2)

#Saída func
def de_decimal_para_binario(numero):
    resultado_binario = para_binario(numero)
    if resultado_binario == '':
        return '0'
    else:
        return resultado_binario

#Exemplo
print(de_decimal_para_binario(12))