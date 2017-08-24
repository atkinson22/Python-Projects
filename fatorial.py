n = int(input('Digite o numero que você deseja calcular o fatorial: '))
f = 1
i = 1

while(i <= n):
    f = f * i
    i +=1

print('O resultado é: ' + str(f))
