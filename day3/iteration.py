menus = ["chicken", "pizza", "beer"]

# for문을 활용하여 메뉴 말하기
for menu in menus:
    print(f"We have {menu},")

print("They're fantastic!")

# 문자형도 반복 가능
spelling = ""
word = "fantastic"
for char in word:
    spelling += char + ", "

print(f"{word} is spelled: {spelling[:-2]}.")

# 열거하기
nth = 1
for menu in menus:
    print(f"{nth}번째 먹고 싶은 음식은 {menu}")
    nth = nth +1 

# 위와 같은 코드를 더 간단하게 사용하는 방법
for index, menu in enumerate(menus):
    print(f"{index + 1}번째 먹고 싶은 음식은 {menu}")