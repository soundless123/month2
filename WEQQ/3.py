import  re
# print(re.search(r'\d{1,3}\.\d{1,3}\.\d]{1,3}\.\d{1,3}','192.168.1.2 192.168.31.103').group())


print(re.findall(r"<<\w+>>", '<<红与黑>>'))

print(re.findall(r"\d{4}-\d{1,2}-\d{1,2}", '2020-11-30 2020-1-52'))
print(re.findall(r"\d{4}-\d{1,2}-\d{1,2}", '2020-11-30 2020-1-52'))


print(re.findall(r"\d{18}", '110081199904260123'))

print(re.search(r"(\d{17})(\d|x)", '11008119990426012x').group())

regex=re.compile(r'ab')



