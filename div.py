#!/usr/bin/python
# coding: utf-8

def main():
    for i in xrange(100):
        if i % 2 == 0 and i % 3 != 0:
            print i

if  __name__ == "__main__":
    main()

