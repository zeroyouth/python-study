from math import factorial


input_number = 11.5

# 코드 영역의 시작을 알린다. 
try:
    factorial(input_number)

# 예상되는 예외의 종류를 except 뒤에 적어준다.
except ValueError:
    # 예외 만났을 때 어떻게 해소할지 작성
    print("value error")
# finally는 except의 실행여부와 상관없이 위의 코드가 다 끝나고 
# 실행되는 코드임 
finally:
    print("finally off work")


def print_n_times(word, n):
    if n > 1000:
        raise ValueError('n is too large')
    
    if not isinstance(n, int):
        raise Exception()

    for _ in range(n):
        print(word)

try:
    print_n_times('happy', '123')
# 여러개의 except를 둘 수 도 있다.   
except ValueError:
    print('n is too large')
except Exception as E:
    print(E)
# 예상치 못한 에러가 나올경우
except:
    print('error hapepend')
finally:
    print("I am done")