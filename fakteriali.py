import time 
def f(n):
    answer = 1
    for i in range(1, n + 1):
        answer = answer * i
    return answer

for i in range(1, 21):
    print(i, f(i))
    time.sleep(0.3)
