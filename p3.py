def irrefutable(s):
    t='I'
    if(s[0]=='I' and s[-1]=='I' and (s[-2]=='I' or s[1]=='I')):
            return('I',len(s))
    elif(s[0]=='O' and s[-1]=='O'):
            return('O',len(s)+1)
    if(s[0]!=s[-1]):
        if(s[0]=='I'):
            s=s[1:]
        elif(s[-1]=='I'):
            s=s[:-1]
        t='O'
    #print(s)
    while(s!='' and len(s)>1):
        if(s[0]=='I' and s[-1]=='I' and (s[-2]=='I' or s[1]=='I')):
            return('I',len(s)+2)
        elif(s[0]=='O' and s[-1]=='O' and (s[-2]=='O' or s[1]=='O')):
            return('O',len(s)+2)
        elif(s[0]!=s[-1] and t=='I'):
            if(s[0]=='I'):
                s=s[1:]
                continue
            elif(s[-1]=='I'):
                s=s[:-1]
                continue
            t='O'
        elif(s[0]!=s[-1] and t=='O'):
            if(s[-1]=='O'):
                s=s[:-1]
                #print("O")
                continue
            elif(s[0]=='O'):
                s=s[1:]
                continue
            t='I'
        elif(s[0]==s[-1] and t=='I'):
            if(s[0]=='I'):
                s=s[1:]
            #print(s)
            t='O'
            continue
        elif(s[0]==s[-1] and t=='O'):
            if(s[0]=='O'):
                s=s[1:]
            #print(s)
            t='I'
            continue
        
    if(len(s)==1):
        return(s,len(s))
        
            
t=int(input())
tc=1
while(t>0):
    s=input()
    s,i=irrefutable(s)
    print("Case #"+str(tc)+": "+str(s)+" "+str(i))
    tc+=1
    t-=1
