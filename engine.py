def move(makan):                                    #تابعی که اسم و مکان مهره ای را میگیرد و تمام حرکات ممکن را نمایش میدهد

    def asb(name,i,j):
        a=[]
        halatha=[[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1]]
        for x in halatha:
            if i+x[0]>=0 and i+x[0]<=7 and j+x[1]>=0 and j+x[1]<=7:
                a.append([name,i+x[0],j+x[1]])
        for x in makanha:
            for z in range(len(a)):
                w=x[0]
                q=a[z][0]
                if x[1]==a[z][1] and x[2]==a[z][2] and w[0]==q[0]:
                    del(a[z])

        return a

    def fil(name,i,j):
        f=[]
        y=i+j
        for x in range(y+1):
            if x!=i and y-x!=j:
                f.append([name,x,y-x])
        for z in range(8-(j-i)):
            if x!=i and j-i+z!=j:
                f.append([name,z,j-i+z])
        c=[]
        for x in makanha:
            for z in range(len(f)):
                w=x[0]
                q=f[z][0]
                if x[1]==f[z][1] and x[2]==f[z][2]:
                    c.append(x)
        print (f)
        print (c)
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
        if name[0]=="w":
            if j==6:
                

    #def king():

    #def vazir():



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


makanha=[["wrokh",3,3],["bpawn",3,5],["wpawn",5,3],["wpawn",2,5]]                                              #ماتریسی که مکان تمام مهره ها رو داره
print(move(["wrokh",3,3]))
