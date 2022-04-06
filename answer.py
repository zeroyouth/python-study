# 1번
print("name:    코딩왕\nage:    28\nevent:  개발자\nnationality:    Korea, Republic of")

# 2번
invest_cost = int(input("투자금액을 입력해주세요($단위): "))
profit = int(input("예상 수익률을 입력해주세요 (%단위): "))
print(f"예상되는 수익은 {int(invest_cost * profit/100)}$ 입니다.")

# 3번
number_a = input("첫 번째 값을 입력해 주세요.")
number_b = input("두 번째 값을 입력해 주세요.")
print(number_a == number_b)

# 4번
print("안녕하세요 제 이름은 \'한상훈\"입니다. \n감사합니다.")

# 5번
invest_const2 = int(input("투자금액을 입력해주세요 ($단위):"))
invest_rate = int(input("투자 수익률을 입력해주세요 ($단위):"))
print(f"예상되는 수익은 ($): \n철수는 {invest_const2}$를 투자해 {invest_rate}%의 이익을 즉 {int(invest_const2 * invest_rate/100)}$를 얻게 됩니다.")