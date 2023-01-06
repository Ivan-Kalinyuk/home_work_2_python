import random
n=int(input('Введите любое натуральное (>=1) число: '))
ar1 = []
for i in range(n):
    ar1.append(i)
print (ar1)
ar2 = ar1
for j in range(n):
    j = random.randint(0, n-1)
    ar2[i], ar2[j] = ar1[j], ar1[i]
print(ar2)
