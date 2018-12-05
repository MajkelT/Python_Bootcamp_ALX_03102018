# import sys
#
# try:
#     print(sys.argv[1])
# except IndexError:
#     print("Zapomniałeś podać nawę pliku")
#
# file_name = sys.argv[1]
# print("Ścieżka do pliku to:" file_name")
#
# print("Ścieżka do pliku to: ", sys.argv[1])

file_name = "dane/logs.txt"

def rozwiązanie_1():
    user_last_login = {}
    user_total_time = {}

    with open(file_name, "r") as f:
        #i = 0
        for line in f:
            user, action, time_str = line.split(";")
            time = int(time_str)
            if action == 'LOGIN':
                user_last_login[user] = time
            elif action == 'LOGOUT':
                time_temp = time - user_last_login[user]   #logout - login
                user_total_time[user] = user_total_time.get(user, 0) + time_temp   #zwraca czas albo 0 jeżeli nic wcześniej nie było
    return user_total_time

def nazwa(x):
    return x[1]  # to samo co lambda x: x[1]


print("Czas przebywania w systemie: " )
for user, time in sorted(rozwiązanie_1().items(), key = lambda x: x[1], reverse = True):  #zwraca
    print(f' - {user}: {time} s')

def rozwiązanie_2():
    user_last_login = {}
    user_last_logout = {}

    with open(file_name, "r") as f:
        # i = 0
        for line in f:
            user, action, time_str = line.split(";")
            time = int(time_str)
            if action == 'LOGIN':
                user_last_login[user] = user_last_login.get(user, 0) + time
            elif action == 'LOGOUT':
                user_last_logout[user] = user_last_logout.get(user, 0) + time
    final_result = {}
    for user in user_last_login:
        final_result[user] = user_last_logout[user] - user_last_login[user]

    return final_result

def rozwiazanie_3():
    out = {}
    with open(file_name) as f:
        for line in f:
            user, action, time_str = line.split(";")
            time = int(time_str)
            if action == "LOGIN":
                out[user] = out.get(user, 0) - time
            if action == "LOGOUT":
                out[user] = out.get(user,0) + time
        return out
    
def nazwa(x):
    return x[1]  # to samo co lambda x: x[1]


print("Czas przebywania w systemie: ")
for user, time in sorted(rozwiązanie_1().items(), key=lambda x: x[1], reverse=True):
    print(f' - {user}: {time} s')

for user, time in sorted(rozwiązanie_2().items(), key=nazwa, reverse=True):
    print(f' - {user}: {time} s')

for user, time in sorted(rozwiązanie_3().items(), key=nazwa, reverse=True):
    print(f' - {user}: {time} s')


assert rozwiązanie_1() == rozwiązanie_2()
