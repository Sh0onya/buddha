def change(x):
    x = int(x)
    if(x < 1000):
        x = x
    elif(x >= 1000 and x < 1000000):
        x = str(round(x/1000,1))+"K"
    elif(x >= 1000000 and x < 1000000000):
        x = str(round(x/1000000,1))+"M"
    elif(x >= 1000000000 and x < 1000000000000):
        x = str(round(x/1000000000,1))+"B"
    else:
        x = str(round(x/1000000000000,1))+"T"
    print(x)

n = 1
while(n >= 1):
    n = int(input("Enter a number: "))
    
    change(n)
