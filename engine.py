def move(makan):                                    #تابعی که اسم و مکان مهره ای را میگیرد و تمام حرکات ممکن را نمایش میدهد

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
            if z!=0 and z+i>=0 and z+i<=7 and j-z>=0 and j-z<=7:
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
                if x[1]<i and x[2]==j and x[1]>minx:
                    minx=x[1]+1
                elif x[1]>i and x[2]==j and x[1]<maxx:
                    maxx=x[1]-1
                elif x[1]==i and x[2]>j and x[2]<maxy:
                    maxy=x[2]-1
                elif x[1]==i and x[2]<j and x[2]>miny:
                    miny=x[2]+1
            else:
                if x[1]<i and x[2]==j and x[1]>minx:
                    minx=x[1]
                elif x[1]>i and x[2]==j and x[1]<maxx:
                    maxx=x[1]
                elif x[1]==i and x[2]>j and x[2]<maxy:
                    maxy=x[2]
                elif x[1]==i and x[2]<j and x[2]>miny:
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
        if i>0 and i<7 and j>0 and j<7:
            k=[[name,i-1,j-1],[name,i,j-1],[name,i+1,j-1],[name,i+1,j],[name,i+1,j+1],[name,i,j+1],[name,i-1,j+1],[name,i-1,j]]
        if (i==0 or i==7) and j>0 and j<7:
            k=k+[[name,i,j+1],[name,i,j-1]]
        if (j==0 or j==7) and i>0 and i<7:
            k=k+[[name,i+1,j],[name,i-1,j]]
        if (j==0 and i==0):
            k=k+[[name,i,j+1],[name,i+1,j]]
        if (j==7 and i==0):
            k=k+[[name,i,j-1],[name,i+1,j]]
        if (j==0 and i==7):
            k=k+[[name,i-1,j],[name,i,j+1]]
        if (j==7 and i==7):
            k=k+[[name,i,j-1],[name,i-1,j]]
        chek=[]
        for x in makanha:
            if x[0][0]!=name[0]:
                chek=chek+move(x)
        for x in chek:
            for y in range(len(k)):
                if x[1]==k[y][1] and x[2]==k[y][2]:
                    k[y]=[-5,-5,-5]
        s=[]
        for x in k:
            if x!=[-5,-5,-5]:
                s.append(x)
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


makanha=[["bking",5,5],["wasb",2,4],["wfil",3,6],["bpawn",3,3]]                                              #ماتریسی که مکان تمام مهره ها رو داره
print(move(["bking",5,5]))
