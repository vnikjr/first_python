import time
x = [1, 2, 7, 9, 11]
y = []
for i in range(len(x)):
    y.append(x[i]*x[i]*x[i])
print(x)
time.sleep (1)
print(y)
