def registration():
    login = input("login: ")
    password = input("password: ")
    name = input('name: ')
    with open('file.txt','a') as f:
        f.write(login+' login '+password+' password '+name+' name ')
    
    
def login(dict):
    dict = dict
    print(dict)
    login = input("login: ")
    password = input("password: ")
    if login in dict and password in dict:
        for key,value in dict.items():
            if value == 'name':
                print('Hello',key)
    else:
        print("Try again!")
        
                    

while True:
    ans = int(input("Choose 1 - login, 2 - registration, 3 - exit: "))
    if ans == 1:
        with open('file.txt','r') as f:
            str = f.read()
        list = str.split()
        dict = dict(zip(list[::2], list[1::2]))
        login(dict)
    elif ans == 2:
        registration()
    elif ans == 3:
        break