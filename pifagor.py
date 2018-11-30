#!/usr/bin/python
# coding: utf-8


def main():
    for a in xrange(1, 11):
        s = ""
        for b in xrange(1, 11):
            s = s + ("% 4d" % (a * b))
        print s


if __name__ == "__main__":
    main()

