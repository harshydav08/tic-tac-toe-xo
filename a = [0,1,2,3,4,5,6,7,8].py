def printSkeleton(lst):
  i=0
  while i<len(lst):
    print(f"{lst[i]} | {lst[i+1]} | {lst[i+2]}")
    if i<len(lst)-3:
      print("=========")
    i+=3
a = ['0','1','2','3','4','5','6','7','8']
all = []
dct = {"O":[],"X":[]}
check = True
play = ["O","X"]
start =0
win = False
whowin = None
wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
while check:
  print(f'Chance of {play[start]}')
  while True:
    printSkeleton(a)
    try:
      inpt = int(input("Please Enter your choice"))
      if inpt<=8 and inpt not in all:
        break
    except:
      continue
  a[inpt] = play[start]
  all.append(inpt)
  dct[play[start]].append(inpt)
  count = 0
  if len(all)>5:
    for i in wins:
      for j in i:
        for k in dct["O"]:
          if j==k:
            count+=1
        if count>=3:
          check=False
          win=True
          whowin="O"
        else:
          count=0
    for k in dct["X"]:
        if j==k:
            count+=1
    if count>=3:
          win=True
          check=False
          whowin="X"
    else:
          count=0
  elif len(all)==8:
    check=False
  if start==0:start+=1
  else:start=0
printSkeleton(a)
if win:
  print(f"Game WON BY {whowin}")
else:
  print("Game Tie")
