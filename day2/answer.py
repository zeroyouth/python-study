# 1
import numbers
from optparse import Values


user_id = ['love77', 'hani900', 'random123']
user_id.append('hooni')
print(user_id)

# 2
user_id.remove('hani900')
print(user_id)

# 3
user_id =  ['love77','hani900','random123','hooni']
print(user_id.index(('hooni')))

# 4
numbers = [1,3,10,2,4,8,7,6]
numbers.sort()
print(numbers)

# dictionary - 1
school = { 
    "class_a":{ 
        "student_1":{ 
            "name":"Mike",
            "marks":{ 
                "physics":70,
                "history":80
            }
        }
    }
}

school['class_a']['student_1']["marks"]["history"] = 95
print(school)

# d -2 
student = { 
    "name": "hooni", 
    "class": 9, 
    "marks": 75 
}

student.pop('name')
print(student)

# d -3
user_oh = {
    "name": "오진혁",
    "event": "archery",
    "age": 40,
    "height": 182,
}

keys = list(user_oh.keys())
values = list(user_oh.values())
print(f"오진혁 선수의 key값은 {keys}이고 \nvalues의 값은 {values}입니다.")


# Tuple, unpacked -1
a, b = (1, 3)
print(f"a의 값은 {a}이고 b의 값은 {3}입니다.")

# advanced
athletes = [
    {
    "name": "한상훈",
    "event": "archery",
    "age": 24,
    "score": 185,
    },{
    "name": "오진혁",
    "event": "archery",
    "age": 40,
    "score": 182,
    }
    ,{
    "name": "안산",
    "event": "archery",
    "age": 40,
    "score": 200,
    },
    {
    "name": "김은미",
    "event": "archery",
    "age": 40,
    "score": 180,
    }
]

athletes[2]["score"] = 205
athletes[3]["age"] = 24
print(athletes)

