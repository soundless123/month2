import  re

pattern=r"(ab)cd(?P<dog>ef)"

regex=re.compile(pattern)

obj=regex.search('abcdefghki')

print(obj.span())#匹配到内容在目标字符串的位置s[0:6]
print(obj.groupdict())#捕获组名与其对应内容的字典
print(obj.group())
print(obj.group(1))
print(obj.group(2))
print(obj.group('dog'))