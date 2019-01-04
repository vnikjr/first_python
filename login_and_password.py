def n():
    pol_login = input("логин: ")
    pol_password = input("пароль: ")
    return pol_login, pol_password


def authorise(login, password):
    users = {"itgen": "12345"}
    if login not in users:
        return False
    if password != users[login]:
        return False
    return True


def main():
    pol_login, pol_password = n()
    if not authorise(pol_login, pol_password):
        print("неправильный логин или пароль ")
        return
    print("допуск есть")


main()
