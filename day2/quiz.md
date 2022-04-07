# Collections 실습 과제

# list 관련

## 연습문제 1

유저 아이디가 담긴 배열에
새로운 유저 hooni가 들어왔다.
유저 아이디가 담긴 배열에 hooni를 추가해주어라

### 유저데이터

```
user_id = ['love77', 'hani900','random123']
```

### 출력 결과

```
['love77', 'hani900','random123', 'hooni']

```

## 연습문제 2

유저 아이디가 담긴 배열에 hani900이 탈퇴했습니다.
담긴 배열에 hani900을 제거하시오.

### 유저 데이터

```
user_id = ['love77','hani900','random123','hooni']
```

### 출력 결과

```
['love77','random123','hooni']
```

## 연습문제 3

유저 아이디 hooni의 index를 출럭하시오.

### 유저 데이터

```
user_id = ['love77','hani900','random123','hooni']
```

### 출력 결과

```

3

```

## 연습문제 4

아래 숫자 배열을 sort method를 활용해서 오름차순 정렬해서 출력하시오.

### 숫자 배열 데이터

```
numbers = [1,3,10,2,4,8,7,6]
```

### 출력 결과

```
[1, 2, 3, 4, 6, 7, 8, 10]
```

# dictionary관련

## 연습문제 1

아래 학교 학교 class_a의 학생들중 mike의 역사 점수가 실제로 95점인데 80점으로 나왔다 이를 수정하고 출력하시오

### 학교 데이터

```
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
```

### 출력 결과

```
school = {
    "class_a":{
        "student_1":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":95
            }
        }
    }
}
```

## 연습문제 2

학생 dictionary 자료형의 이름을 비공개로 하기위해서 제거하기로했다.
이 name key를 제거 하고 출력하시오

### 학생 데이터

```
student = {
    "name": "hooni",
    "class": 9,
    "marks": 75
}
```

### 출력 결과

```
student = {
    "class": 9,
    "marks": 75
}

```

## 연습문제 3

오진혁 선수의 데이터가 다음 아래와 같이 있을때
key값과 values의 값들을 따로 배열로 저장하고 싶다는 요청이 들어왔다
keys와 values method를 활용해서 다음 아래와 같이 출력되게 하시오

### 오진혁 선수의 데이터

```
user_oh = {
    "name": "오진혁",
    "event": "archery",
    "age": 40,
    "height": 182,
}
```

### 출력 결과

```
오진혁 선수의 key값은 ['name', 'event', 'age', 'height']이고 values의 값은 ['오진혁','archery', 40, 182]입니다.
```

# Tuple, unpacked

연습문제 1

```
a = 1
b = 3

```

위 코드를 tuple과 unpack을 활용해서 다음과 같이 출력하시오

```
a의 값은 1이고 b의 값은 3입니다.
```

# advanced

다음과 같은 데이터가 주어질 때
안산 선수의 점수를 200에서 205로 변경하고
김은미 선수의 나이를 24로 변경하고

바뀐 결과를 출력하시오

### 선수 데이터

```
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

```

### 출력 결과

```

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
    "score": 205,
    },
    {
    "name": "김은미",
    "event": "archery",
    "age": 24,
    "score": 180,
    }
]

```
