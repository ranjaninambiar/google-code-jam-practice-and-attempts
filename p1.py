t=int(input())
tc=1
while(t>0):
    n=int(input())
    s=list(map(int,input().split(" ")))
    d={}
    for num in s:
        try:
            d[num]+=1
        except:
            d[num]=1
    l=list(d)
    l.sort()
    c=1
    ans=0
    for i in l:
        ans+=d[i]*c
        c+=1
    print("Case #"+str(tc)+": "+str(ans))
    tc+=1
    t-=1
    
