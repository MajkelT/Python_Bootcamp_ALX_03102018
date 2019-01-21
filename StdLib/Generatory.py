def generator(jakismax):
    for i in range(0, jakismax, 2):
        yield i

for x in generator(15):
    print(x)