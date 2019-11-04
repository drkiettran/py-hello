#!/usr/bin/python3

from datetime import datetime
import sys
import os
import socket

class HelloWorld:
    def __init__(self):
        self.datetime = datetime.now().replace(tzinfo=None)

    def sayHello(self, name):
        return '{time}: Hello, {name} from {host}/{procid}'\
                .format(time=self.datetime, name = name, \
                        host=socket.gethostname(), procid=os.getpid())

def main(name):
    helloWorld = HelloWorld()
    msg = helloWorld.sayHello(name)
    print(msg)


if __name__ == '__main__':
    main(sys.argv[1])