import random
def kinut_kosti():
        return [random.randint(1, 6), random.randint(1, 6)]

def main():
    while True:
        print("что дальше будете делать? введите 1, если вы наигрались или что угодно, если хотите продолжить: ")
        deystvie = input()
        if deystvie == "1":
            return
        all_cubes = kinut_kosti()
        print(all_cubes)

main()
