a=float(input('Введите любое число: '))
a=str(a)
a=list(a)
sum=0
i=0
b=0
while i<len(a):
    if a[i]=='.':
        i=i+1
    elif a[i]=='-':
        i=i+1
    else:
        b=int(a[i])
        i=i+1
        sum=sum+b
print(f'Сумма цифр Вашего числа = {sum}')