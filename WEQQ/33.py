import re

fr=open('exc2.txt')
while True:
    data=''
    for line in fr:
        if line=='\n':
            # 一段结束
            break
        data += line
    print(data)




    if not data:
        break





