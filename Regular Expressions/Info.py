# https://regex101.com   --> tu będzie info o tym oraz gotowe zbiory i definicje

# ..ks. --> . zastępuję jeden znak
# .*    --> zastępuje wszystkie znaki
# .+    --> jedno lub więcej wystąpień
# [ab] --> szuka znaku ze zbioru: tu a lub b
# [a-z]  --> zakres szukania od a do z
# [^a] --> ^ oznacza zaprzeczenie - w tym wypadk zaznaczy wszystko co nie jest lierą a
# \. --> faktyczne wskazanie kropki jako znaku
# \d - cyfra
# \D - wszystko co nie jest cyfrą
# [sda]{3} --> *to zero lub więcej dopasowań, . to jedno lub więcej, a {3} oznacza dokładnie trzy dopasowania
# [sda](2,3} --> dwa lub trzy wystąpienia - szukamy znaków należących do tego zbioru,
#                ale kolejność jest nie ważna, ważne, żeby były obok siebie
# sd - szukanie dokładnie sd
#[A-Z][a-z}* --> to powinno pomóc wyszukać imię - pierwszy znak z przedzialu A-Z, a potem dowolnie wiele razy małe a-z
