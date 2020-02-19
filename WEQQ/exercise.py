'''
使用input输入一个端口名称，匹配到其对应的 address is 什么

段落之间有空行
每段的收个单词是端口名称

思路：先找到对应的那一段文字
'''
import re

# port = input("端口：")
fr=open('exc.txt')
# while True:
#     data=''
#     for line in fr:
#         if line =='\n':
#             #一段结束
#             break
#         data+=line
#     if not data:
#         #文件结尾
#         break
#     print(data)
#
# fr.close()
data=fr.read()

    # #匹配首单词
    # obj=re.match(r"\S+",data)
    # # print(obj)
    #
    # #确定是否为目标段
    # if port==obj.group():
    #     pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
    #     print(data)
    #     obj=re.search(pattern,data)
    #     print(obj.group())
    #     break


# print('全局变量：',data)

# 匹配首单词
obj = re.match(r"\S+", data)
print('obj:',obj)
# print(obj)
port='BVI1'
# 确定是否为目标段
if port == obj.group():
    pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
    print(data)
    obj = re.search(pattern, data)
    print(obj.group())


# pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
# data2='Hardwaridge-Group Virtual Interface, address is 10f3.116c.e6a7re is B'
#
#
# obj=re.findall(pattern,data)
# print(obj)

