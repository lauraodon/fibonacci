'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Check Point 1
Aluna:
Laura Giancoli Aschenbrenner - RM 87194
'''
N = int(input('Digite um valor: '))
if N < 2:
    print('Escolha um número maior')
else:
    a = 0
    b = 1
    r = 3
    print(a)
    print(b)
    while N >= r:
        prox = a + b
        print(prox)
        a = b
        b = prox
        r += 1
    print('Fim da linha')