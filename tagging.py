import sys
import os
import sqlite3
import hashlib

class tag(object):
    global hashes
    hashes = []

    def id(self):
        h = hashlib.md5()
        for arg in file:
            with open(arg, 'rb') as f:
                buffer = f.read()
                h.update(buffer)
                hash = h.hexdigest()
                assign = hash
                hashes.append(assign)

if __name__ == __main__:
    file = sys.argv
    file.pop(0)

    tag().id()
    print(hashes)



