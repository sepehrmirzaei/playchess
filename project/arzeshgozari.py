def kish(move):
    newmakanha=[]
    for x in makanha:
        if x[0]!=move[0] and not(move[1]==x[1] and move[2]==x[2]):
            newmakanha.append(x)
            newmakanha.append(move)
    for x in newmakanha:
        if x[0]="wking":
            w=newmakanha.index(x)
        elif x[0]="bking":
            b=newmakanha.index(x)
    iswchek="no"
    isbchek="no"
    for x in newmakanha:
        sm=move(x)
        if x[0][0]=="b":
            for y in sm:
                if y[1]==newmakanha[w][1] and y[2]==newmakanha[w][2]:
                    iswchek="yes"
        if x[0][0]=="w":
            for y in sm:
                if y[1]==newmakanha[b][1] and y[2]==newmakanha[b][2]:
                    isbchek="yes"
        achmaz="no"
        iskish="no"
        if move[0][0]=="w" and iswchek=="yes":
            achmaz="yes"
        if move[0][0]=="b" and isbchek=="yes":
            achmaz="yes"
        if move[0][0]=="w" and isbchek=="yes":
            iskish="yes"
        if move[0][0]=="b" and iswchek=="yes":
            iskish="yes"
    return (achmaz,iskish)


def arzesh(move):
    arzeshha={"wrokh":5 "wasb":3 "wfil":3.2 "wvazir":9 "wking":1000 "wpawn":1 "brokh":5 "basb":3 "bfil":3.2 "bvazir":9 "bking":1000 "bpawn":1}
    newmakanha=[]
    for x in makanha:
        if x[0]!=move[0] and not(move[1]==x[1] and move[2]==x[2]):
            newmakanha.append(x)
            newmakanha.append(move)
    def arzeshmohreha(makanha,newmakanha):
        oldw, oldb, neww, newb=0, 0, 0, 0
        for x in makanha:
            if x[0][0]=="w":
                oldw=oldw+arzeshha[x]
            else :oldb=oldb+arzeshha[x]
        for x in newmakanha:
            if x[0][0]=="w":
                neww=neww+arzeshha[x]
            else :newb=newb+arzeshha[x]
        return (oldw-oldb,neww-newb)
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



    def akharbazi():

    def bartaridofil():

    def rokhdoposhte():

    def makanvazir():

    def makanshah():
