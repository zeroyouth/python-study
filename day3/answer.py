# 1 
A = [1,25,30,6,2,99,10,11,31,32,5]
answer = []
idx = 0

for num in A:
    if num < 13:
        answer.append(num)
answer.sort()
print(f"1번의 답은 : {answer}")

# 2
i = 0
while i < 10:
    print("*1*")
    i += 1

for _ in range(10):
    print("*1*")

# 3
late = int(input("지각한 시간은 몇 분 입니까?"))

if late <=0:
    number = 0
elif late <=5:
    number = 10
elif late <=10:
    number = 20
elif late <=30:
    number = 30
else:
    number = 50

if number > 0:
    for i in range(number):
        print(f"{i+1} 다시는 지각을 안하겠습니다.")
else:
    print("이 친구는 지각을 하지 않았습니다.")

# 4번
for i in range(10):
    print("*"*(i+1))

# 5번
for i in range(11):
    if i <= 5: # 홀수개의 별이 찍힌다는 것을 생각한다.
        print(" "*(5-i)+(2*i + 1) * "*") 
    else:
        n = i - 5
        print(" "*(i-5)+(2*(10-i) + 1)* "*")

#5.1 (계단 만들기)
for i in range(10):
    print((" "*(10-i))+("*"*(i+1)))

#5.2 다이아몬드 키우기
diamond = int(input('별 최대 개수 : '))

if diamond % 2 == 1:
    i = 1
else :
    i = 2

for i in range(i, diamond+1, 2):
    blank = ' '*((diamond-i)//2)
    star = '*'*i # 여기에 * 대신 다양한 기호 사용 가능!
    
    print(blank, star,blank)

for i in range(i-2, 0, -2):
    blank = ' '*((diamond-i)//2)
    star = '*'*i
    
    print(blank, star,blank)