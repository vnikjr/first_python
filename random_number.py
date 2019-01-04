import random
def main():
    x = random.randint (1, 10)
    for i in range(0, 4):
        y = int(input("я загодал число от 1 дот 10"))
        if y > x:
            print ("нет у меня число меньше ")
        else:
            if y == x:
                print ("да ты угадал")
                return
            else:
                if y < x:
                    print ("нет у меня число больше")
main()
