import sys

try:
    print(sys.argv[1])
except IndexError:
    print("Zapomniałeś podać nawę pliku")

print("Ścieżka do pliku to: ", sys.argv[1])

with open(sys.argv[1], "r") as f:
    users = {}
    for line in f:
        line = line.split(";")
        user = line[0]
        action = line[1]
        time = line[2]
        time = int(time)

        #print(line, time)

        #users[user] = 0
        users[user] = time
        for user in users:
            if action == "LOGIN":
                start_time = time
                if action == "LOGOUT":
                    end_time = time
                    in_system_time = time + end_time - start_time

    #sorted(y, reverse = True)
    print(users)






