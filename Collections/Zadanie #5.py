i = 0
x = 0
y = 0
print("    ", end="")
while i<10:
    print (f"{i:3}", end="")
    i +=1
print()
print()
for x in range (10):
    print (f"{x:3} "    "", end="")
    for y in range (0,10):
        print (f"{x*y:3}", end="")
    print()

