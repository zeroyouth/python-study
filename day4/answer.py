#1
from sys import prefix


present_dict = {'아이패드': 600000, '애플워치':300000, '맥북':1000000}
result = 0 
for price in present_dict.values():
    result = result + price
print(result)

def calculator(dict):
    result = 0
    for price in dict.values():
        result += price
    return result

print(calculator(present_dict))

#2
def func(m,list):
    result = 0
    for n in list:
        if n  % m == 0:
            result += n
    return result

number_list = [3,2,4,7,9,10,12,40]
m = 3

print(func(3,number_list))

# 3
# for index, char in enumerate(url):
#     if char == '.':
#         dot_index.append(index)
# print(url[dot_index[0]+1:dot_index[1]}]

def get_brand(url):
    parsed_list = url.split('.')
    print(parsed_list[1])

url = 'https://www.google.com'
url2 = 'https://www.naver.com'

parsed_list = url.split('.')
print(get_brand(url))
print(get_brand(url2))

# 4
input_num = 1
brand_name = 'naver'

prefix_list = ['http://www', 'https://www']
sed_list = [prefix_list[input_num-1], brand_name, 'com']
answer = '.'.join(parsed_list)
print(answer)

def make_url(input_num, brand_name):
    prefix_list = ['http://www', 'https://www']
    parsed_list = [prefix_list[input_num-1],brand_name,'com']
    answer = '.'.join(parsed_list)
    return answer

print(make_url(1,'kakao'))