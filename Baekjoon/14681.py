x = int(input())
y = int(input())

if (-1000<=x<=1000 and x!=0) and (-1000<=y<=1000 and y!=0) :
    if x > 0 :
        if y > 0 :
            print(1)
        else :
            print(4)
    
    else :
        if y > 0 :
            print(2)
        else :
            print(3)
