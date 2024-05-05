import random 
#W -> win percentage (1..10)-> 3--> 30%......
def rig_prob(w: int, n: int ):
    
     
    for _ in range(n):
        count1 = 0
        count0 = 0 
        arr = []
        for i in range(10):
            r  = random.randint(0,1)
            if r==0 and count0 <10-w:
                arr.append(r)
                count0 +=1 
            elif r==1 and count1 < w :
                arr.append(r)
                count1 +=1 
            elif r==1 and count1==w and count0 <10-w:
                arr.append(0)
                count0+= 1 
            elif r==0 and count0==10-w and count1< w:
                arr.append(1)
                count1+=1 

        print(arr)


r = rig_prob(7,  100)
