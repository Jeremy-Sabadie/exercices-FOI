nbpair=int(input())
for a in range(nbpair):
    absMin1=int(input())
    absMax1=int(input())
    ordoMin1=int(input())
    ordoMax1=int(input())
    absMin2=int(input())
    absMax2=int(input())
    ordoMin2=int(input())
    ordoMax2=int(input())
    condition=(absMax1 <= absMin2) or (absMax2 <= absMin1) or (ordoMax1 <= ordoMin2) or (ordoMax2 <= ordoMin1)
    if condition:
        print("NON")
    else:
        print("OUI")