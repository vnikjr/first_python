
while True:
    try:
        x = float(input("число 1: "))
    except ValueError:
        print('Введите число')
    else:
        break
 
while True:
    try:
        y = float(input("число 2: "))
    except ValueError:
        print('Введите число')
    else:
        break
 
answer = ""
oper = input("какую операцию сделаем: ")
if oper == "+":
    answer = x + y
elif oper == "-":
    answer = x - y
elif oper == "*":
    answer = x * y
elif oper == "/":
    answer = x / y
elif oper == "**" or oper == "^":
    answer = x ** y
    
else:
     answer = "ошибка "
if answer == "ошибка ":
    print (answer) 
else:
    print ("ответ ", answer)

