from distutils.errors import DistutilsClassError


def print_hello_world():
    print('hello_world')

print_hello_world()

# happy 10번찍기
def print_ten_times(word):
    count = 0
    while(count < 10):
        print(word)
        count = count + 1

print_ten_times('happy')

def calculate_age(current_year, birth_year):
    return current_year - birth_year + 1 

my_age = calculate_age(2022, 2000)
print(my_age)


def get(dict, key, defalut_value = None):
    if key in dict:
        return dict[key]
    else:
        return defalut_value

my_dict = {"name" : "hooni"}
answer = get(my_dict, "age" ,24)
print(answer)

