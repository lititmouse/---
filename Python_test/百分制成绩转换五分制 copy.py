while True:
    x = float(input())

    if x > 100 :
        print("data error")
    elif x >= 90 :
        print("A")
    elif x >= 80 :
        print("B") 
    elif x >= 70:
        print("C")
    elif x >= 60 :
        print("D")
    elif x >= 0 :
        print("E")
    else :
        print("end")
        break
