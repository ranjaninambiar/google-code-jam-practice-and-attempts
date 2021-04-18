t=int(input())
tc=1
while(t>0):
    n=int(input())
    l=list(map(int,input().split(" ")))
    s="A"
    od=65
    c=1
    for i in range(n):
        if(c==1):#odd case
            temp=od
            od=od+l[i]
            try:
                while(od-l[i+1]<ord(s[-1])):
                    od=od+1
            except:
                pass
            count=0
            start=temp+1
            end=od
            
            while(count<l[i]-1 and start<end):
                s+=chr(start)
                start+=1
                count+=1
                
            s+=chr(od)
            #print(s)
            c=-1
            continue
        elif(c==-1):#even case
            count=0
            start=65
            if(l[i]==1):
                s+=chr(start)
                c=1
                continue
            else:
                start=65+(l[i]-1)
                while(count<l[i] ):
                    s+=chr(start)
                    start-=1
                    count+=1
                    
            #print(s)
            c=1
            continue
    print("Case #"+str(tc)+": "+str(s))
    tc+=1
    t-=1
