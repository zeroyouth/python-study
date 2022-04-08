from multiprocessing import Condition


user = {
    "id" : 'hooni',
    "password" : '1234'
}

print('로그인 창 접속')
user_id_input = input('아이디를 입력해주세요 : ')
user_password_input = input('비밀번호를 입력해주세요: ')

if (user_password_input == user['password']):
    if (user_id_input == user['id']):
        print('로그인 성공')
    else: 
        print('로그인 실패')
else: 
    print('로그인 실패')
print(user_id_input, user_password_input)

num_a = input('첫번째 숫자를 입력 해주세요. ')
num_b = input('두번째 값을 입력해주세요.')
o = input('연산자를 입력해주세요.')

if (o == "+"):
    print(f'두 수를 더한 값은 {num_a + num_b} 입니다.')
elif (o == '-'):
    print(f'두 수를 뺀 값은 {num_a - num_b} 입니다.')
elif (o == '*'):
    print(f'두 수를 뺀 값은 {num_a * num_b} 입니다.')
elif (o == '/'):
    print(f'두 수를 뺀 값은 {num_a / num_b} 입니다.')
else:
    print('잘못입력하셨습니다.')