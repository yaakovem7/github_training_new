#1,2
# try:
#     a=1/0
# except:
#     print("divided in 0")
#

#3 - not legal,the finally should be under the try
# try:
#     x=1
# finally:
#     print("finaly")

#4- any type
#5- to general. recomended to be more dedicated to particular ry
#6- IOError - file open/close/read/write issues.
     #ZeroDivisionError - except when we migh divif number in 0

#7-10
# my_file=open("D:/temp/words.txt",'a+',encoding='utf-8')
# content= my_file.write("Yaakov Magar1\n")
# my_file.seek(0)
# content= my_file.read()
# print(content)
# content= my_file.write("יעקב מגר")
# my_file.seek(0)
# content= my_file.read()
# print(content)




#11
#from flask import Flask
# app = Flask(__name__)
#
# @app.route("/content")
# def get_file():
#     return open("D:/temp/words.txt").read(), 200 # status code
#
# @app.route("/register")
# def write_file():
#     open("D:/temp/words.txt","w").write("hello")
#     return "sucess", 201 # status code
# app.run(host='127.0.0.1', debug=True, port=30000)

import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)




