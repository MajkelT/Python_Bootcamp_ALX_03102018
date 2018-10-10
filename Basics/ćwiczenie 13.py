i = 0
sumatemp = 0

while True:
    temp = (input("Podaj temperaturę w tygodniu: "))
    if temp == "k":
        break
    temp = int(temp)
    sumatemp = sumatemp + temp  #sumatemp + = temp
    i = i + 1    # i + = i
print(f"Temp average: {sumatemp/i}")
