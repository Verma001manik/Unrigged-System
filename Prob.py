import random 
#W -> win percentage (1..10)-> 3--> 30%......
def rig_prob(w: int, n: int ):
    
     
    for _ in range(n):
        count = 0 
        arr = []
        for i in range(10):
            r  = random.randint(0,1)
            if r ==1 and count ==w:
                arr.append(0)
            elif r==1 and count <w:
                arr.append(r)
                count += 1 
            
            else:
                arr.append(r)
        print(arr)


r = rig_prob(3, 20)
