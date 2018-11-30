x = int(input("число 1: "))
y = int(input("число 2: "))
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
else:
     answer = "ошибка "
if answer == "ошибка ":
    print (answer * 2) 
else:
    print ("ответ ", answer)
