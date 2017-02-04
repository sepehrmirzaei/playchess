def move(makan):                                    #تابعی که اسم و مکان مهره ای را میگیرد و تمام حرکات ممکن را نمایش میدهد

    def asb():

    def fil():

    def vazir():

    def pawn():

    def king():

    def rokh():



    if makan[0]=="wasb" or makan[0]=="basb":
        harkat=asb(makan[1],makan[2])
    elif makan[0]=="wfil" or makan[0]=="bfil":
        harkat=fil(makan[1],makan[2])
    elif makan[0]=="wvazir" or makan[0]=="bvazir":
        harkat=vazir(makan[1],makan[2])
    elif makan[0]=="wpawn" or makan[0]=="bpawn":
        harkat=pawn(makan[1],makan[2])
    elif makan[0]=="wking" or makan[0]=="bking":
        harkat=king(makan[1],makan[2])
    elif makan[0]=="wrokh" or makan[0]=="brokh":
        harkat=rokh(makan[1],makan[2])
