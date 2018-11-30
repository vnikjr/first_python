#!/usr/bin/python
# coding: utf-8


import urllib3


def main():
    urllib3.disable_warnings()
    with urllib3.PoolManager() as http:
        r = http.request('GET', "https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D0%B9%D0%B5%D1%81,_%D0%A2%D0%BE%D0%BC%D0%B0%D1%81")
    print r.data


if __name__ == "__main__":
    main()

