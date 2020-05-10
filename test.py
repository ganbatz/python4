too = int(input("too: "))

for i in range(1, too+1):
    txt = str(i)[::-1]
    if i == int(txt):
        print(txt)