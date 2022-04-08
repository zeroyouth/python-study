# range(n) 함수는 0부터 n-1까지 돌려줍니다.

for num in range (1,100):
    print(num)

# range(start, end)로 사용하면 된다.
for i in range(1, 11):
    print(i)

# enumerate : 열거하다
athletes = ['박찬호','안산','김연아']
for idx, item in enumerate(athletes):
    print(f"{idx + 1}: {item}")

# 반복문 벗어나고 싶으면 break 
# continue

for i in range(1, 10):
    if i == 5:
        print("컨티뉴")
        continue
    print(i)