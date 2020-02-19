import re

# 目标字符串
s = "Alex:1996,Sunny:1998"
s1="今天2020年2月19日"

pattenr = r"(\w+:\d+)"  # 正则表达式 \w匹配普通字符（字母，下划线，汉字）
                                    #\d匹配任意数字字符

l = re.findall(pattenr, s)
print(l)

regex=re.compile(pattenr)
l2=regex.findall(s,0,9)
print(l2)

#对目标字符串切割
l=re.split(r':\,',s)
print(l)

#对目标字符串替换
l=re.finditer(r'\d+',s1)

for i in l:
    print(i.group())


# obj=re.match(r'\d+',s1)
# print(obj.group())

print()
obj=re.search(r'\d+',s1)
print(obj.group())

