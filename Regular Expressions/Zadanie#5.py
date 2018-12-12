import re
#regular expression

regex = re.compile("[0-9]+")  #zwróci obiekt reprezentujący tego regex'a - cyfry w tym wypadku
regex1 = re.compile("\D+")

regex2 = re.compile("\d{2}-\d{3}")
regex3 = re.compile("[A-Z]*[a-z]*@[a-z.]*")
regex4 = re.compile("\d{2} [A-Z][a-z]{2} \d{4}")

wynik = regex.findall("asdaltestkhdlktestashfkghlgsa234jlkdfhla")
wynik1 = regex1.findall("asdaltestkhdlktestashfkghlgsa234jlkdfhla")

wynik2 = regex2.findall("12-223")
wynik3 = regex3.findall("masdasd@gmail.com.pl")
wynik4 = regex4.findall("12 Jan 1990")

print(wynik)
print(wynik1)
print("")
print(wynik2)
print(wynik3)
print(wynik4)
