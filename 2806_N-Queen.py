for z in range(int(input())):
 N=int(input());l=[[]for i in range(N)];l[0]=[[i]for i in range(N)]
 for i in range(1,N):
  for j in range(N):
   for p in l[i-1]:
    for y,x in enumerate(p):
     if j==x or j-x==i-y or x-j==i-y:break
    else:l[i]+=[p+[j]]
 print("#%d %d"%(z+1,len(l[-1])))