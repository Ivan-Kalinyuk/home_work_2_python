n=int(input('Введите любое натуральное (>=1) число: '))
i=0
sum=0
ar=[]
while i<n:
    m=round((1+1/(i+1))**(i+1),2)
    ar.append(m)
    sum=sum+m
    i=i+1
print(f'Вот список:{ar}')
print(f'Вот сумма чисел в этом списке: {sum}')