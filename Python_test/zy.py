x = input()

for  i in x:
    if i.islower():
        print(i.lower(),end=" ",)
    elif i.isupper():
        print(i.upper(),end=" ",)
    elif x.isnumeric():
        print(i,end=" ",)