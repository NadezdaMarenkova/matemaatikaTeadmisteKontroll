import random 

k=int(input("Сколько примеров желаете решить? \n")) # Запрашиваем у пользователя желаемое кол-во примеров
p=int(input("Выберите сложность примера: \n1 - легкий уровень \n2 - средний уровень \n3 - сложный уровень \n")) # Предлогаем пользователю выбрать сложность заданий
print("\t!!! Обрати внимание !!!\n* Ответ округляем до двух знаков после запятой  *\n")
o=0

if p==1:        # Легкий уровень 
    for i in range(1,k+1):
        a=random.randint(1,10) # Задаем предел промежутка для случайного числа  
        b=random.randint(1,10)
        ans1=float(a+b)
        ans2=float(input(f"Решите пример: \n{a} + {b} = "))
        if 2*ans1==ans1+ans2: # Проверка ответа, сравниваем ответ примера, с ответом пользователя.
            o=o+1
        else:
            print(f"\nПравильный ответ: {ans1}\n")

elif p==2:       # Средний уровень
    for i in range(1,k+1):
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=random.randint(1,10)
        variant=random.randint(1,3) # Рандомные варианты примеров
        if variant==1:
            ans1=float(a+b-c)
            ans2=float(input(f"Решите пример: \n{a} + {b} - {c} = "))
        elif variant==2:
            ans1=float(a+b+c)-(b+c)
            ans2=float(input(f"Решите пример: \n{a} + {b} - {c} - ({b} + {c}) = "))
        elif variant==3:
            ans1=float(a+b)*c
            ans2=float(input(f"Решите пример: \n{a} + {b} * {c} = "))
        if 2*ans1==ans1+ans2:
            o=o+1
        else:
            print(f"\nПравильный ответ: {ans1}\n")


elif p==3:      # Сложный уровень
    for i in range(1,k+1):
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=random.randint(1,10)
        d=random.randint(1,10)
        variant=random.randint(1,3)
        if variant==1:
            ans1=float(a+d-c)*(b+c)/a
            ans1=round(ans1,2)
            ans2=float(input(f"Решите пример: \n({a} + {d} - {c}) * ({b} + {c}) / {a} = "))
        elif variant==2:
            ans1=float(a/b*c)-(d+c)+(b**2)
            ans1=round(ans1,2)
            ans2=float(input(f"Решите пример: \n({a} / {b} * {c}) - ({d} + {c}) + ({b}**2) = "))
        elif variant==3:
            ans1=float(b*c*a)/d+(c**2)+d
            ans1=round(ans1,2)
            ans2=float(input(f"Решите пример: \n({b} * {c} * {a}) / {d} + ({c}**2) + {d} = "))
        if 2*ans1==ans1+ans2:
            o=o+1
        else:
            print(f"\nПравильный ответ: {ans1}\n")
else:
    print("Error value")

print(f"Количество правильных ответов:  {o}")
hind=(o/k)*100 # Выщитываем кол-во правильных ответов и сообщаем тестируемому оценку.
if hind <=59:
    print("Ваша оценка: 2")
elif hind <=74:
    print("Ваша оценка: 3")
elif hind <=90:
    print("Ваша оценка: 4")
else:
    print("Ваша оценка: 5")

