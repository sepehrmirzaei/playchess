def move(makan):                                    #تابعی که اسم و مکان مهره ای را میگیرد و تمام حرکات ممکن را نمایش میدهد

    def asb(name,i,j):
        a=[]
        halatha=[[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1]]
        for x in halatha:
            if i+x[0]>=0 and i+x[0]<=7 and j+x[1]>=0 and j+x[1]<=7:
                a.append([name,i+x[0],j+x[1]])
        return a

    def fil(name,i,j):
        f=[]
        y=i+j
        for x in range(y+1):
            f.append([name,x,y-x])
        for z in range(8-(j-i)):
            f.append([name,z,j-i+z])
        return f    

    def vazir():

    def pawn():

    def king():

    def rokh():



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
