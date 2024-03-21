res = []
dice = [res.append((i,j))for i in range(1,7) for j in range(1,7)]
total = len(res)
print("Probabilities of all possible sums of the outcome : \n")
c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=0
for i in res:
    if sum(i)==2:
        c1=c1+1
    elif sum(i)==3:
        c2+=1
    elif sum(i)==4:
        c3+=1
    elif sum(i)==5:
        c4+=1
    elif sum(i)==6:
        c5+=1
    elif sum(i)==7:
        c6+=1
    elif sum(i)==8:
        c7+=1 
    elif sum(i)==9:
        c8+=1 
    elif sum(i)==10:
        c9+=1 
    elif sum(i)==11:
        c10+=1 
    elif sum(i)==12:
        c11+=1 
    
print("P(sum=2) : ",round((c1/total),3))
print("P(sum=3) : ",round((c2/total),3))
print("P(sum=4) : ",round((c3/total),3))
print("P(sum=5) : ",round((c4/total),3))
print("P(sum=6) : ",round((c5/total),3))
print("P(sum=7) : ",round((c6/total),3))
print("P(sum=8) : ",round((c7/total),3))
print("P(sum=9) : ",round((c8/total),3))
print("P(sum=10) : ",round((c9/total),3))
print("P(sum=11) : ",round((c10/total),3))
print("P(sum=12) : ",round((c11/total),3))

        