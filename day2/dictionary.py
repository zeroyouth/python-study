from optparse import Values


user_list = ['youngeun', 24]

user = {"name" : "youngeun", "age" : 24 }
user["age"] = 25
print(user)

print(user.get("hobby")) #>>>None

numbers = { }
numbers["num"] = numbers.get("num", 0) + 3 #{num: 3}
numbers["num"] = numbers.get("num", 0) + 3 #{num: 6}
numbers["num"] = numbers.get("num", 0) + 3 #{num: 9}
print(numbers)

# 추가하기 
user.update({"hobby":"dance"})
print(user)

# keys valuesrkqt
items = user.keys()
print(items)
values = user.values()
print(values)

user_2 = {"hobbies": {'favorite':'reading'}}
hobby = user_2["hobbies"]['favorite']
print(hobby)