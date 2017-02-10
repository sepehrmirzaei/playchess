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
    mainvalue=0
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
                n.append(move(["wrokh",x[1],x[2]]))
        a=len(n)

        for x in newmakanha:
            if x[0]=="wrokh":
                m.append(move(["wrokh",x[1],x[2]]))
        b=len[n]
        for x in makanha:
            if x[0]=="brokh":
                w.append(move(["brokh",x[1],x[2]]))
        c=len(w)

        for x in newmakanha:
            if x[0]=="brokh":
                z.append(move(["brokh",x[1],x[2]]))
        d=len[z]
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

    def makanpawn(move):
        value=0
        if move[0][0]=="w":
            if x[1]<6 and x[1]>1 and x[2]>2:
                value+=0.05
            if x[1]>5 :
                value+=0.02
        if move[0][0]=="b":
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
                fil=move(x)
                if x[0][0]=="w":
                    wold+=len(fil)
                else:
                    bold+=len(fil)
        for x in newmakanha:
            if x[0][1:]=="fil":
                fil=move(x)
                if x[0][0]=="w":
                    wnew+=len(fil)
                else:
                    bnew+=len(fil)
        value=(wnew-wold)*0.1-(bnew-bold)*0.1
        return value


    mainvalue+=arzeshmohreha(makanha,newmakanha)
    if move[0][1:]=="pawn":
        mainvalue+=piadedoobl(makanha,newmakanha)+makanpawn(move)
    elif move[0][1:]=="asb":
        mainvalue+=makanasb(makanha,newmakanha)
    elif move[0][1:]=="fil":
        mainvalue+=makanfil(makanha,newmakanha)+bartaridofil(makanha,newmakanha)
    elif move[0][1:]=="rokh":
        mainvalue+=makanrokh(makanha,newmakanha)
    elif move[0][1:]=="vazir":
        mainvalue+=makanvazir(makanha,newmakanha)
    elif move[0][1:]=="king":
        mainvalue+=makanshah(makanha,newmakanha)
    natige=[mainvalue]
    natige=natige+newmakanha
    return natige                  
