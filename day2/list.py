# 

from fileinput import hook_compressed
import numbers

#              0       1      2         3
athletes = ['오진혁','안산','황선우','서채현']
# print(athletes[2])
athletes[2] = 'hooni'
print(athletes)


# List slicing
print(athletes[1:3]) # 끝 바로 직전까지 뽑는다.
# >>> ['안산','황선우'] 만 출력됨

# 문자 추출하기
sentence = 'I am going to eat a pizza'
answer = sentence[5:7]
print(f"추출된 값은 {answer}")

# 값 추가하기 append
athletes.append('최영은')
print(athletes)

# 값 연결하기 extend
athletes_new = ['수지','아이유']
athletes_new.extend(athletes)
print(athletes_new)
# + 플러스 연산자로도 연결 가능

# 값 지우기
athletes.remove('안산')
print(athletes)

# 정렬
athletes.sort(reverse=True)
print(athletes)

numbers = [12,3,4,5,6,10]
numbers.sort() # 오름차순
print(numbers)
numbers.sort(reverse=True) # 내림차순
print(numbers)
## 정렬할 때 자료형 정리해야됨