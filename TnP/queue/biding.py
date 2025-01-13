
bid=[]

while True:
    value=input("Enter bid:")

    if value=="":
        break
    else:
        bid.append(value)
    
print(f"Max bid is: {max(bid)} at {bid.index(max(bid))+1}")
print(f"Second Max bid is: {sorted(bid)[-2]} at {bid.index(sorted(bid)[-2])}")