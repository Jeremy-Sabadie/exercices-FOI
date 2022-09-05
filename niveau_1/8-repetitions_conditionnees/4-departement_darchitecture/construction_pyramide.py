""fonctionne pas:
maxStones=int(input())

stage=1
nbStones=0
side=1
stageCount=0

while nbStones<maxStones:
  stage=side*side
  nbStones=nbStones+stage
  side=side+1
  stageCount=stageCount+1
print(stageCount)
print(nbStones)