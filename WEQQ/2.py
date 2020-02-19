import re
job=re.findall('wo*', "wow,wow,wooooooooaw~")
print(job)

print(re.findall('[0-9]+', '今天2020年2月19日'))

print(re.findall('[A-Z][a-z]+', 'Hi Jame H are you '))

print(re.findall('[A-Z][a-z]*', 'Hi Jame H are you '))

print(re.findall('[A-Za-z0-9_]{8,12}', 'phone:1A_1asd58'))

print(re.findall('-?[0-9]+%?', '12 -45 256 -1 6 23%'))

print(re.findall('[A-Z]+[a-z0-9]*', 'Hi41341234 Jame H BAS you '))

print(re.findall('\d+', "port:6000"))

print(re.findall('\D+', "port:6000"))

print(re.findall('\w+', "port:6000"))

print(re.findall('\W+', "port:6000"))

print(re.findall('\w+', "重庆，"))

print(re.findall('\W+', "重庆，"))

print(re.findall('\s+', "重庆  "))

print(re.findall('\S+', "重庆  "))

print(re.findall('\d+\.?\d*', '45 1 , 33 1.1234 4.5'))

print(re.findall(r'\$\d+', '$100'))
print(re.findall('\$\d+', '$100'))

print(re.findall('\\bis', 'This is a test'))

print(re.findall(r'ab*', 'abbbbbbbbbc'))
print(re.findall(r'ab+', 'abbbbbbbbbc'))
print(re.findall(r'ab??', 'abbbbbbbbbc'))
print(re.findall(r'ab{3,5}', 'abbbbbbbbbc'))
print(re.findall(r'ab{3,5}?', 'abbbbbbbbbc'))
print(re.findall(r'\[.+\]', '[1-5]这是xxx注释[6/10]xxx[*#006a]'))
print(re.findall(r'\[.+?\]', '[1-5]这是xxx注释[6/10]xxx[*#006a]'))

print(re.findall(r'(ab)', 'ababababababab'))

print(re.search(r'(ab)', 'ababababababab').group())

print(re.search(r'(ab)+', 'ababababababab').group())

print(re.search(r'(a)\w+', 'ababababababab').group())

print(re.search(r'(王)\w+', '王者荣耀').group())

print(re.search(r'(https|http|ftp|file)://\S+',"https://www.baidu.com").group(1))

print(re.findall(r'\S+',"https://www.baidu.com"))

print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{1,3}\.[0-9]{1,3}','192.168.1.2 192.168.31.103'))



print(re.findall(r'<<+.+>>','<<红与黑>>12431234'))

print(re.findall(r'[0-9]+-+[0-9]+-[0-9]+','202-11-30 2020-1-5 2020-05-03'))

print(re.findall(r'[0-9]{18}','123456789012345678'))



