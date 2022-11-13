house=int(input())
maxX=int(input())
minX=maxX
maxY=int(input())
minY=maxY
for pos in range(house-1):
    x = int(input())
    y = int(input())
    if x > maxX:
        maxX=x
    elif x < minX:
        minX=x
    if y > maxY:
        maxY=y
    elif y < minY:
        minY=y

perimeter=2*((maxX-minX)+(maxY-minY))
print(perimeter)