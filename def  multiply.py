def add(x):
    if x < 0: 
        print("錯誤")

    elif x == 0: 
        return 1
        
    else: 
        a = 1
        while(x > 1): 
            a=a*x
            x=x-1
        return a 

     
z=add(10)
print(z)
    