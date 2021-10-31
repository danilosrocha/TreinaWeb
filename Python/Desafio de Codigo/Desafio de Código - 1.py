t = int(input())
lista = []
for i in range(0,t):
    conta = 0
    a, b, n = map(int, input().split())
    for cont in range(n):
        conta = (pow(2, cont) * b) + conta 
        lista.append(conta + a)
        
        print(lista[-1], end = " ")
    print()

