# billing system for tea stall, menu driven to give order and produce bill

while True:

    ch = input("Enter choice (y/n)")

    if ch=="y" or ch=="Y":
        print("1.Tea----10")
        print("4.Coffee----40")
        print("3.Water----20")
        print("1.Bun Maska----50")
        print("")
        print("Enter number of tea, coffee, water, Bun Maska")
        print("-----------")

        t,c,w,b = map(int,input().split())
        print(f"Your Order is tea:{t} coffee:{c} water:{w} bun:{b}")

        print("-----")
        print("Bill")
        print("")
        if t>0 :
            print(f"Tea  - 10X {t} : {t*10}")
        if c>0 :
            print(f"Coffee  - 40X {c} : {c*40}")
        if w>0 :
            print(f"Water  - 20X {w} : {w*20}")
        if b>0 :
            print(f"Bun  - 50X {b} : {b*50}")  
        print("-----------")
        print(f"Total------:{t*10 + c*40 + w*20 + b*50}")                      
    elif ch=="n" or ch=="N":
        print("Thanks visit again...")
        break
    else :
        print("Choose only from 'y' or 'n'")