#from arzeshgozari import kish
def move(makanha,makan):                                    #تابعی که اسم و مکان مهره ای را میگیرد و تمام حرکات ممکن را نمایش میدهد

    def asb(name,i,j):
        a=[]
        halatha=[[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1]]
        for x in halatha:
            if i+x[0]>=0 and i+x[0]<=7 and j+x[1]>=0 and j+x[1]<=7:
                a.append([name,i+x[0],j+x[1]])
        s=[]
        for x in makanha:
            for z in range(len(a)):
                w=x[0]
                q=a[z][0]
                if x[1]==a[z][1] and x[2]==a[z][2] and w[0]==q[0]:
                    a[z]=[-5,-5,-5]
        for x in a:
            if x!=[-5,-5,-5]:
                s.append(x)
        return s

    def fil(name,i,j):
        f=[]
        for x in range(i-7,8-j):
            if x!=0 and x+i<8 and x+i>-1 and x+j<8 and x+j>-1:
                f.append([name,x+i,j+x])
        for z in range(j-7,8-i):
            if z!=0 and z+i>-1 and z+i<8 and j-z>=0 and j-z<=7:
                f.append([name,z+i,j-z])
        c=[]
        for x in makanha:
            for z in range(len(f)):
                w=x[0]
                q=f[z][0]
                if x[1]==f[z][1] and x[2]==f[z][2]:
                    c.append(x)
        for x in c:
            for h in range(len(f)):
                if f[h]!=0:
                    a=f[h][0][0]
                    if x[0][0]==a:
                        if x[1]>i and x[2]>j and f[h][2]>=x[2] and f[h][1]>=x[1]:
                            f[h]=0
                        elif x[1]<i and x[2]>j and f[h][2]>=x[2] and f[h][1]<=x[1]:
                            f[h]=0
                        elif x[1]<i and x[2]<j and f[h][2]<=x[2] and f[h][1]<=x[1]:
                            f[h]=0
                        elif x[1]>i and x[2]<j and f[h][2]<=x[2] and f[h][1]>=x[1]:
                            f[h]=0
                    else:
                        if x[1]>i and x[2]>j and f[h][2]>x[2] and f[h][1]>x[1]:
                            f[h]=0
                        elif x[1]<i and x[2]>j and f[h][2]>x[2] and f[h][1]<x[1]:
                            f[h]=0
                        elif x[1]<i and x[2]<j and f[h][2]<x[2] and f[h][1]<x[1]:
                            f[h]=0
                        elif x[1]>i and x[2]<j and f[h][2]<x[2] and f[h][1]>x[1]:
                            f[h]=0
        d=[]
        for x in f:
            if x!=0:
                d.append(x)
        return d

    def rokh(name,i,j):
        r=[]
        minx=0
        maxx=7
        miny=0
        maxy=7
        for x in makanha:
            if x[0][0]==name[0]:
                if x[1]<i and x[2]==j and x[1]>=minx:
                    minx=x[1]+1
                elif x[1]>i and x[2]==j and x[1]<=maxx:
                    maxx=x[1]-1
                elif x[1]==i and x[2]>j and x[2]<=maxy:
                    maxy=x[2]-1
                elif x[1]==i and x[2]<j and x[2]>=miny:
                    miny=x[2]+1
            else:
                if x[1]<i and x[2]==j and x[1]>=minx:
                    minx=x[1]
                elif x[1]>i and x[2]==j and x[1]<=maxx:
                    maxx=x[1]
                elif x[1]==i and x[2]>j and x[2]<=maxy:
                    maxy=x[2]
                elif x[1]==i and x[2]<j and x[2]>=miny:
                    miny=x[2]
        for x in range(minx,maxx+1):
            if x!=i:
                r.append([name,x,j])
        for y in range(miny,maxy+1):
            if y!=j:
                r.append([name,i,y])
        return r
    def pawn(name,i,j):
        p=[]
        n=0
        m=0
        if name[0]=="w":                                                       #پیاده های سفید
            if j==6:
                for x in makanha:
                    if x[0][0]=="b" and (x[1]==i-1 or x[1]==i+1) and x[2]==j-1:
                        p.append([name,x[1],x[2]])
                    elif x[1]==i and (x[2]==j-1):
                        n=1
                    elif x[1]==i and x[2]==j-2:
                        m=1
                if n==0:
                    p.append([name,i,j-1])
                if m==0:
                    p.append([name,i,j-2])
            n=0
            if j<6 and j>0:
                if j==1:
                    for x in makanha:
                        if x[0][0]=="b" and (x[1]==i-1 or x[1]==i+1) and x[2]==j-1:
                            p.append(["wvazir",x[1],0])
                    p.append("wvazir",i,0)
                    for h in makanha:
                        if h[1]==i and h[2]==0:
                            del(p[len(p)-1])

                else:
                    for x in makanha:
                        if x[0][0]=="b" and (x[1]==i-1 or x[1]==i+1) and x[2]==j-1:
                            p.append([name,x[1],x[2]])
                        elif x[1]==i and (x[2]==j-1):
                            n=1
                    if n==0:
                        p.append([name,i,j-1])


        n, m=0, 0
        if name[0]=="b":                                                            #پیاده های سیاه
            if j==1:
                for x in makanha:
                    if x[0][0]=="w" and (x[1]==i-1 or x[1]==i+1) and x[2]==j+1:
                        p.append([name,x[1],x[2]])
                    elif x[1]==i and (x[2]==j+1):
                        n=1
                    elif x[1]==i and x[2]==j+2:
                        m=1
                if n==0:
                    p.append([name,i,j+1])
                if m==0:
                    p.append([name,i,j+2])
            n=0

            if j>1 and j<7:
                if j==6:
                    for x in makanha:
                        if x[0][0]=="w" and (x[1]==i-1 or x[1]==i+1) and x[2]==j+1:
                            p.append(["bvazir",x[1],7])
                    p.append(["bvazir",i,7])
                    for h in makanha:
                        if h[1]==i and h[2]==7:
                            del(p[len(p)-1])

                else:
                    for x in makanha:
                        if x[0][0]=="w" and (x[1]==i-1 or x[1]==i+1) and x[2]==j+1:
                            p.append([name,x[1],x[2]])
                        elif x[1]==i and (x[2]==j+1):
                            n=1
                    if n==0:
                        p.append([name,i,j+1])
        return p


    def king(name,i,j):
        k=[]
        if i>0 and i<7 and j>0 and j<7:
            k=[[name,i-1,j-1],[name,i,j-1],[name,i+1,j-1],[name,i+1,j],[name,i+1,j+1],[name,i,j+1],[name,i-1,j+1],[name,i-1,j]]
        elif (i==0 or i==7) and j>0 and j<7:
            k=k+[[name,i,j+1],[name,i,j-1],[name,i-1,j-1],[name,i-1,j],[name,i-1,j+1]]
        elif (j==0 or j==7) and i>0 and i<7:
            k=k+[[name,i+1,j],[name,i-1,j],[name,i-1,j+1],[name,i,j+1],[name,i+1,j+1]]
        elif (j==0 and i==0):
            k=k+[[name,i,j+1],[name,i+1,j],[name,i+1,j+1]]
        elif (j==7 and i==0):
            k=k+[[name,i,j-1],[name,i+1,j],[name,i+1,j-1]]
        elif (j==0 and i==7):
            k=k+[[name,i-1,j],[name,i,j+1],[name,i-1,j+1]]
        elif (j==7 and i==7):
            k=k+[[name,i,j-1],[name,i-1,j],[name,i-1,j-1]]
        chek=[]
        superk=[]
        aaa=0
        for y in k:
            for x in makanha:
                if not(x[0][0]==y[0][0] and x[1]==y[1] and x[2]==y[2]):
                    aaa=1
                else:
                    aaa=0
                    break
            if aaa!=0:
                superk.append(y)

        for x in makanha:
            if x[0][0]!=name[0] and x[0][1:]!="king":
                chek=chek+move(makanha,x)
        for x in chek:
            for y in range(len(superk)):
                if x[1]==superk[y][1] and x[2]==superk[y][2]:
                    superk[y]=[-5,-5,-5]
        s=[]
        for x in superk:
            if x!=[-5,-5,-5]:
                s.append(x)
        o=0
        if name[0]=="w" and i==4 and j==7:
            if ["wrokh",7,7] or ["wrokh",0,7] in makanha:
                for x in makanha:
                    if (x[1]==5 or x[1]==6) and x[2]==7:
                        o=1
                        break
            a, b=-1, -1
            if o==0:
                if ["wrokh",7,7] in makanha:
                    a=makanha.index(["wrokh",7,7])
                if ["wrokh",0,7] in makanha:
                    b=makanha.index(["wrokh",0,7])
                if a!=-1:
                    s=s+["wking",6,7]+["wrokh",5,7]
                if b!=-1:
                    s=s+["wking",2,7]+["wrokh",3,7]
        o=0
        if name[0]=="b" and i==4 and j==0:
            if ["brokh",0,0] or ["wrokh",7,0] in makanha:
                for x in makanha:
                    if (x[1]==5 or x[1]==6) and x[2]==0:
                        o=1
                        break
            a, b=-1, -1
            if o==0:
                if ["brokh",7,0] in makanha:
                    a=makanha.index(["brokh",7,0])
                if ["brokh",0,0] in makanha:
                    b=makanha.index(["brokh",0,0])
                if a!=-1:
                    s=s+["bking",6,0]+["brokh",5,0]
                if b!=-1:
                    s=s+["bking",2,0]+["brokh",3,0]
        return s
    def vazir(name,i,j):
        v=[]
        v=rokh(name,i,j)+fil(name,i,j)
        return v


    if makan[0]=="wasb" or makan[0]=="basb":
        harkat=asb(makan[0],makan[1],makan[2])
    elif makan[0]=="wfil" or makan[0]=="bfil":
        harkat=fil(makan[0],makan[1],makan[2])
    elif makan[0]=="wvazir" or makan[0]=="bvazir":
        harkat=vazir(makan[0],makan[1],makan[2])
    elif makan[0]=="wpawn" or makan[0]=="bpawn":
        harkat=pawn(makan[0],makan[1],makan[2])
    elif makan[0]=="wking" or makan[0]=="bking":
        harkat=king(makan[0],makan[1],makan[2])
    elif makan[0]=="wrokh" or makan[0]=="brokh":
        harkat=rokh(makan[0],makan[1],makan[2])

    return(harkat)



mainmakanha=[["wking",1,4],["wpawn",3,5],["bfil",4,0],["wrokh",2,2],["bpawn",1,2],["bking",7,1]]                                              #ماتریسی که مکان تمام مهره ها رو داره
#print(move(mainmakanha,["bfil",4,0]))

def kish(makanha,moving):
    newmakanha=[]
    for x in makanha:
        if x[0]!=moving[0] and not(moving[1]==x[1] and moving[2]==x[2]):
            newmakanha.append(x)
    newmakanha.append(moving)
    for x in newmakanha:
        if x[0]=="wking":
            w=newmakanha.index(x)
        elif x[0]=="bking":
            b=newmakanha.index(x)

    iswchek="no"
    isbchek="no"
    for x in newmakanha:
        sm=move(newmakanha,x)
        if x[0][0]=="b" and x[0]!="bking":
            for y in sm:
                if y[1]==newmakanha[w][1] and y[2]==newmakanha[w][2]:
                    iswchek="yes"
        elif x[0][0]=="w" and x[0]!="wking":
            for y in sm:
                if y[1]==newmakanha[b][1] and y[2]==newmakanha[b][2]:
                    isbchek="yes"
        achmaz="no"
        iskish="no"
        if moving[0][0]=="w" and iswchek=="yes":
            achmaz="yes"
        if moving[0][0]=="b" and isbchek=="yes":
            achmaz="yes"
        if moving[0][0]=="w" and isbchek=="yes":
            iskish="yes"
        if moving[0][0]=="b" and iswchek=="yes":
            iskish="yes"
    return (achmaz,iskish)

def arzesh(makanha,moving):
    arzeshha={"wrokh":5, "wasb":3, "wfil":3.2, "wvazir":9,"wking":1000 ,"wpawn":1, "brokh":5 ,"basb":3, "bfil":3.2, "bvazir":9, "bking":1000, "bpawn":1}
    newmakanha=[]
    mainvalue=0
    for x in makanha:
        if x[0]!=moving[0] and not(moving[1]==x[1] and moving[2]==x[2]):
            newmakanha.append(x)
    newmakanha.append(moving)
    def arzeshmohreha(makanha,newmakanha):
        oldw, oldb, neww, newb=0, 0, 0, 0
        for x in makanha:
            if x[0][0]=="w":
                oldw=oldw+arzeshha[x[0]]
            else :oldb=oldb+arzeshha[x[0]]
        for x in newmakanha:
            if x[0][0]=="w":
                neww=neww+arzeshha[x[0]]
            else :newb=newb+arzeshha[x[0]]
        return ((neww-newb)-(oldw-oldb))

    def piadedoobl(makanha,newmakanha):
        valuepast=0
        valuenew=0
        st=[]
        sr=[]
        for x in makanha:
            if x[0]=="wpawn":
                if x[1] not in st:
                    st.append(x[1])
                else:
                    valuepast+=-0.5
            elif x[0]=="bpawn":
                if x[1] not in st:
                    st.append(x[1])
                else:
                    valuepast+=0.5
        for x in newmakanha:
            if x[0]=="wpawn":
                if x[1] not in st:
                    st.append(x[1])
                else:
                    valuenew+=-0.5
            elif x[0]=="bpawn":
                if x[1] not in st:
                    st.append(x[1])
                else:
                    valuenew+=0.5
        return (valuenew-valuepast)

    def bartaridofil(makanha,newmakanha):
        state2=0
        state1=0
        blackasb, blackfil, whiteasb, whitefil=0, 0, 0, 0
        for x in makanha:
            if x[0]=="wasb":whiteasb+=1
            if x[0]=="basb":blackasb+=1
            if x[0]=="wfil":whitefil+=1
            if x[0]=="bfil":blackfil+=1
        if whitefil+whiteasb==blackasb+blackfil>1:
            if whitefil==2 and blackasb==2:state1+=0.5
            if whitefil==1 and blackasb==0:state1+=-0.2
            if whitefil==0 and blackasb==0:state1+=-0.5
            if whitefil==1 and blackasb==2:state1+=0.2
        blackasb, blackfil, whiteasb, whitefil=0, 0, 0, 0
        for x in newmakanha:
            if x[0]=="wasb":whiteasb+=1
            if x[0]=="basb":blackasb+=1
            if x[0]=="wfil":whitefil+=1
            if x[0]=="bfil":blackfil+=1
        if whitefil+whiteasb==blackasb+blackfil>1:
            if whitefil==2 and blackasb==2:state2+=0.5
            if whitefil==1 and blackasb==0:state2+=-0.2
            if whitefil==0 and blackasb==0:state2+=-0.5
            if whitefil==1 and blackasb==2:state2+=0.2
        return state2-state1

    def makanvazir(makanha,newmakanha):
        bstate=0
        wstate=0
        for x in makanha:
            if x[0]=="wvazir":
                n=move(["wvazir",x[1],x[2]])
                a=len[n]
        for x in newmakanha:
            if x[0]=="wvazir":
                m=move(["wvazir",x[1],x[2]])
                b=len[n]
        wstate+=(b-a)*0.05
        for x in makanha:
            if x[0]=="bvazir":
                d=move(["bvazir",x[1],x[2]])
                a=len[n]
        for x in newmakanha:
            if x[0]=="bvazir":
                e=move(["bvazir",x[1],x[2]])
                b=len[n]
        bstate+=(a-b)*0.05
        before=0
        after=0
        for x in n:
            if (x[1]==5 or x[1]==5 or x[1]==5) and (x[2]==1 or x[2]==0 or x[2]==2):
                before+=0.3
        for x in m:
            if (x[1]==5 or x[1]==5 or x[1]==5) and (x[2]==1 or x[2]==0 or x[2]==2):
                after+=0.3
        wstate+=(after-before)
        before=0
        after=0
        for x in d:
            if (x[1]==5 or x[1]==5 or x[1]==5) and (x[2]==5 or x[2]==6 or x[2]==7):
                before+=0.3
        for x in e:
            if (x[1]==5 or x[1]==5 or x[1]==5) and (x[2]==5 or x[2]==6 or x[2]==7):
                after+=0.3
        bstate+=(after-before)
        return(wstate-bstate)

    def makanshah(makanha,newmakanha):
        bstate=0
        wstate=0
        a, b=0, 0
        if ["wking",6,7] or ["wking",7,7] in makanha:
            a+=1
        if ["wking",6,7] or ["wking",7,7] in newmakanha:
            b+=1
        wstate=b-a
        if ["wpawn",5,6] and ["wpawm",6,6] and ["wpawn",7,6] in makanha:
            a=0.3
        if ["wpawn",5,6] and ["wpawm",6,6] and ["wpawn",7,6] in newmakanha:
            b=0.3
        wstate+=(b-a)

        a, b=0, 0
        if ["bking",6,0] or ["bking",7,0] in makanha:
            a+=1
        if ["bking",6,0] or ["bking",7,0] in newmakanha:
            b+=1
        bstate=b-a
        if ["bpawn",5,1] and ["bpawm",6,1] and ["bpawn",7,1] in makanha:
            a=0.3
        if ["bpawn",5,1] and ["bpawm",6,1] and ["bpawn",7,1] in newmakanha:
            b=0.3
        bstate+=(b-a)
        return wstate-bstate

    def makanrokh(makanha,newmakanha):
        n=[]
        m=[]
        w=[]
        z=[]
        for x in makanha:
            if x[0]=="wrokh":
                n.append(move(makanha,["wrokh",x[1],x[2]]))
        a=len(n)

        for x in newmakanha:
            if x[0]=="wrokh":
                m.append(move(newmakanha,["wrokh",x[1],x[2]]))
        b=len(n)
        for x in makanha:
            if x[0]=="brokh":
                w.append(move(makanha,["brokh",x[1],x[2]]))
        c=len(w)

        for x in newmakanha:
            if x[0]=="brokh":
                z.append(move(newmakanha,["brokh",x[1],x[2]]))
        d=len(z)
        value=0
        value+=(b-a)*0.1-(d-c)*0.1
        return value

    def makanasb(makanha,newmakanha):
        bold=0
        wold=0
        bnew=0
        wnew=0
        value=0
        for x in makanha:
            if x[0][1:]=="asb":
                knight=move(x)
                if x[0][0]=="w":
                    wold+=len(knight)
                else:
                    bold+=len(knight)
        for x in newmakanha:
            if x[0][1:]=="asb":
                knight=move(x)
                if x[0][0]=="w":
                    wnew+=len(knight)
                else:
                    bnew+=len(knight)
        value=(wnew-wold)*0.1-(bnew-bold)*0.1
        return value

    def makanpawn(mov):
        value=0
        if mov[0][0]=="w":
            if x[1]<6 and x[1]>1 and x[2]>2:
                value+=0.05
            if x[1]>5 :
                value+=0.02
        if mov[0][0]=="b":
            if x[1]<6 and x[1]>1 and x[2]<5:
                value+=-0.05
            if x[1]>5 :
                value+=-0.02
        return value
    def makanfil(makanha,newmakanha):
        bold=0
        wold=0
        bnew=0
        wnew=0
        value=0
        for x in makanha:
            if x[0][1:]=="fil":
                fil=move(makanha,x)
                if x[0][0]=="w":
                    wold+=len(fil)
                else:
                    bold+=len(fil)
        for x in newmakanha:
            if x[0][1:]=="fil":
                fil=move(newmakanha,x)
                if x[0][0]=="w":
                    wnew+=len(fil)
                else:
                    bnew+=len(fil)
        value=(wnew-wold)*0.1-(bnew-bold)*0.1
        return value


    mainvalue+=arzeshmohreha(makanha,newmakanha)
    if moving[0][1:]=="pawn":
        mainvalue+=piadedoobl(makanha,newmakanha)+makanpawn(moving)
    elif moving[0][1:]=="asb":
        mainvalue+=makanasb(makanha,newmakanha)
    elif moving[0][1:]=="fil":
        mainvalue+=makanfil(makanha,newmakanha)+bartaridofil(makanha,newmakanha)
    elif moving[0][1:]=="rokh":
        mainvalue+=makanrokh(makanha,newmakanha)
    elif moving[0][1:]=="vazir":
        mainvalue+=makanvazir(makanha,newmakanha)
    elif moving[0][1:]=="king":
        mainvalue+=makanshah(makanha,newmakanha)

    return mainvalue

def nextmove(makanha,movi):
    newmakanha=[]
    for x in makanha:
        if x[0]!=movi[0] and not(movi[1]==x[1] and movi[2]==x[2]):
            newmakanha.append(x)
    newmakanha.append(movi)
    return newmakanha


#print(nextmove(mainmakanha,["bfil",2,2]))

#print(kish(mainmakanha,["bfil",2,2]))
khar=[]
min=-10000
max=10000
khar.append(0)
khartamam=[]
def example(makanha,n):
    if n%2==0:
        for x in makanha:
            if x[0][0]=="b":
                ss=move(makanha,x)
                for y in ss:
                    jigar=nextmove(makanha,y)
                    if n-1>-1:
                        if len(khar)<4:
                            khar[0]=khar[0]+arzesh(makanha,y)
                            khar.append(y)
                            example(jigar,n-1)
                            cop=khar.copy()
                            khartamam.append(cop)
                            khar.pop()
                            khar[0]=0


    else:
            for x in makanha:
                if x[0][0]=="w":
                    ss=move(makanha,x)
                    for y in ss:
                        jigar=nextmove(makanha,y)
                        if n-1>-1:
                            if len(khar)<4:
                                khar[0]=khar[0]+arzesh(makanha,y)
                                khar.append(y)
                                example(jigar,n-1)
                                cop=khar.copy()
                                khartamam.append(cop)
                                khar.pop()
                                khar[0]=0





situations=[]
example(mainmakanha,3)
for x in khartamam:
    if len(x)==4:
        situations.append(x)
print(situations)

nomre=-1000
khat2=[]
bargozide=[]
for i in range(len(situations)-1):
    if situations[i][1]==situations[i+1][1] and situations[i][2]==situations[i+1][2] and situations[i][0]>nomre:
        nomre=situations[i][0]
        bargoz=situations[i]
    elif situations[i][1]!=situations[i+1][1] or situations[i][2]!=situations[i+1][2]:
        khat2.append(nomre)
        bargozide.append(bargoz)
        nomre=-1000
print(khat2)
print(bargozide)
bargozidetar=[]
khat1=[]
nomre=1000
for i in range(len(bargozide)-1):
    if bargozide[i][1]==bargozide[i+1][1] and bargozide[i][0]<nomre:
        nomre=bargozide[i][0]
        bargoz=bargozide[i]
    elif bargozide[i][1]!=bargozide[i+1][1]:
        khat1.append(nomre)
        bargozidetar.append(bargoz)
        nomre=1000
print(khat1)
print(bargozidetar)
minn=-1000

for x in khat1:
    if x>minn:
        minn=x
for x in bargozidetar:
    if x[0]==minn:
        print(x)
        break
