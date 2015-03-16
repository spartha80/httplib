from collections import Set 
import socket
import time
import sys

current_milli_time = lambda: int(round(time.time() * 1000))

class t:
    def __init__(self):
        self.ts = current_milli_time()


def main():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dict_ = {}
    dict_[sock1] = t()
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #time.sleep(1)
    dict_[sock2] = t()
    if sock1 in dict_:
        print dict_[sock1]
    else:
        print "Out"
    if sock2 in dict_:
        print dict_[sock2]
    else:
        print "Out"
    del dict_[sock1]
    if sock1 in dict_:
        print dict_[sock1]
    else:
        print "Out"
    if sock2 in dict_:
        print dict_[sock2]
    else:
        print "Out"


if __name__ == "__main__":
    main()