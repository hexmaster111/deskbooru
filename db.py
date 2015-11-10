import sys
import os
import sqlite3
import hashlib

class db(object):
    
    global filenames
    filenames = []

    def hashlist(self):
        h = hashlib.md5()
        count = 0
        for arg in filein:
            with open(arg, 'rb') as f:
                buff = f.read()
                h.update(buff)
                md5hash = h.hexdigest()
                filenames.append(filein[count])
                filenames.append(md5hash)
                count += 1
 
    global conn
    conn = sqlite3.connect('tags.db')
    global c
    c = conn.cursor()

    def create(self):
        open('tags.db', 'a+')
        c.execute('''CREATE TABLE files 
                  (filename text, hash integer)''')
        
    
    def add(self):
        c.execute('INSERT INTO files VALUES (?, ?)', filenames)
        conn.commit()


sys.argv.pop(0)
filein = sys.argv


if os.path.isfile('tags.db') == False:
    db().create()
else:
    db().hashlist()
    print filenames
    conn.close()
