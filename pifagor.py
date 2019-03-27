#!/usr/bin/python
# coding: utf-8


def main():
    for a in range(1, 11):
        s = ""
        for b in range(1, 11):
            s = s + ("% 4d" % (a * b))
        print(s)


if __name__ == "__main__":
    main()

