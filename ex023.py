num = int(input('Insira um valor entre 0 e 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(m, c, d, u)
#Ex: 1934
#u // 1 -> 1934 % 10 -> 193,(4)
#d // 10 -> 193 % 10 -> 19,(3)
#c // 100 -> 19 % 10 -> 1,(9)
#m // 1000 -> 1 % 10 -> 0,(1)
