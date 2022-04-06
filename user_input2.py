number_a = input('숫자 1 : ')
number_b= input('숫자 2 : ')
print('둘을 곱한 값은?', str(int(number_a) * int(number_b))) # input은 입력 값을 문자로 받음

print(f'둘을 곱한 값은? {int(number_a) * int(number_b)}')

user_name = input('이름을 입력해주세요: ')
user_password = input('비밀번호를 입력해주세요: ')
print(f'유저 이름은 {user_name} , 유저의 비밀번호는 {user_password}입니다.')

# f 문자열 포매팅을 사용하면 변수를 그대로 사용할 수 있다.

# 변수 선언과 동시에 할당을 해주어야 한다. 
a = None
a = 123
type(a)
# >>> <class 'int'>