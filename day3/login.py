user = {
    "user_id" : "asdf",
    "password" : "1234",
}

i = 0
login_success = False
while i < 5 and not login_success:
    password = input("input password: ")
    if password == user["password"]:
        print("login success!")
        login_success = True
    else:
        print("login failed, try again")
        i += 1

if not login_success: #5번 틀리면 나옴
    print("user locked")