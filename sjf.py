waitT=[]
tat=[]
total=0
brustT = []    
n =  input("Enter toal number of processes:")
print("\nEnter Burst Time:\n")
for i in range(0 , n):
	print("p:",i+1)
	a =input()
        brustT.append(a)
        process.append(i+1)                   
    
for i in range(0 , n):
        pos=i
	j = i+1
        for j in xrange(n):
            if brustT[j]<brustT[pos]:
                pos=j
        
 
        temp=brustT[i]
        brustT[i]=brustT[pos]
        temp=brustT[i]
        brustT[i]=brustT[pos]
        brustT[pos]=temp
 
        temp=process[i]
        process[i]=process[pos]
        process[pos]=temp
    
 
waitT.append(0)          
 
i = 1
for i in xrange(n):
        waitT.append(0)
	j = 0
        for j in xrange(i):
            waitT[i]+=brustT[j]
			 
        total+=waitT[i]
    
 
avg_wait=total/n  
total=0
 
print'\nProcess\t    Burst Time    \tWaiting Time\tTurnaround Time'
i = 0
for i in xrange(n):
        tat.append(brustT[i]+waitT[i])
        total+=tat[i]
        print'       ',process[i] ,  '       ' , brustT[i]  , '  	',waitT[i] , '	' ,tat[i]
    
 
avg_tat=total/n
print'\n\nAverage Waiting Time=',avg_wait
print'\nAverage Turnaround Time=\n',avg_tat